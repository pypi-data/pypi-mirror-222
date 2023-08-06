import gymnasium as gym
import numpy as np
from gymnasium import spaces
from simulink_connect import MatlabProjectPlant
from track_generation import TrackGenerator
from utils import separation, projection, offtrack


class DroneEnv(gym.Env):
    metadata = {"render.modes": ["human"]}

    def __init__(self):
        super().__init__()

        # Define Observation Space
        self.observation_space = spaces.Box(
                low=0,
                high=255,
                shape=(4, 120, 160),
                dtype=np.uint8
        )

        # Define Action Space
        self.action_space = spaces.Box(
            low=-1,
            high=1,
            shape=(2,),
            dtype=np.float32
        )

        # Define Evaluation Properties
        self.yaw = 0
        self.position = (0, 0)
        self.displacement = (0, 0)
        self.height = 0
        self.target_height = 2.0
        self.off_track_threshold = 0.1
        self.progress_reward_factor = 1000
        self.finish_dist_threshold = 0.2
        self.finish_flag = False
        self.finish_reward = 1000

        # Establish Simulink Connect Plant
        self.plant = MatlabProjectPlant(
            project_name="parrotMinidroneCompetition",
            input_register={
                "disp_x": ("flightControlSystem/Control System/Path Planning/Guidepost/disp_x", "Value"),
                "disp_y": ("flightControlSystem/Control System/Path Planning/Guidepost/disp_y", "Value"),
                "target_z": ("flightControlSystem/Control System/Path Planning/Guidepost/target_z", "Value")
            },
            output_register={
                "position": "out.position(end,:)",
                "img_batch": "out.img_batch",
            }
        )

        # Connect to Matlab
        self.plant.connect_to_matlab()

        # Build Track Generator
        self.track_gen = TrackGenerator(
            size=(3, 3),
            border=(0.5, 0.5),
            collinear_threshold=np.pi * (15 / 180),
            separation_threshold=(0.4, 2.4),
            segment_count=4
        )
        self.way_points = None

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        # Stop Simulink Model
        self.plant.sim_stop()

        # Randomize Flight Track
        self.track_update()

        # Start Simulink Model
        self.plant.sim_start()

        # Initialize Model Inputs
        self.plant.sim_set_input({key: 0 for key in ["disp_x", "disp_y", "target_z"]})

        # Run until Height reaches 1.1
        self.height = 0
        self.drone_launch(self.target_height)

        # Get Initial Observation
        observation = self._get_obs()
        info = self._get_info()
        self._update_eval_info()
        self.step((0, 0))

        return observation, info

    def step(self, action):
        # Execute Action
        self._exe_act(action)
        self.plant.sim_step()

        # Do Observation
        self._update_eval_info()
        observation = self._get_obs()
        info = self._get_info()

        # Evaluate Reward
        reward = self._get_reward()

        # Check Termination Status
        terminated = (self.plant.sim_get_status() == ('stopped' or 'terminating')) or self.finish_flag

        return observation, reward, terminated, False, info

    def render(self):
        # The Visualization is Handled by Matlab
        pass

    def close(self):
        # Zero Inputs to Simulink
        self.plant.sim_set_input({key: 0 for key in ["disp_x", "disp_y", "target_z"]})

        # Stop Simulink Session
        self.plant.sim_stop()

        # Disconnect from Matlab
        self.plant.disconnect()

    def drone_launch(self, target_height):
        # Ascend
        self.plant.sim_set_input({"target_z": -target_height})
        while abs(self.height - target_height) > 0.01:
            self.plant.sim_step()
            self.height = - self.plant.sim_get_output(["position"])["position"][2]

    def track_update(self):
        # Randomize the Track
        self.way_points = self.track_gen.track_generate()

        # Process Numpy Array into String Understandable to Matlab
        wp_cmd = "TrackBuild(["
        for point in self.way_points:
            # Load Points into String with ";" Separating Rows
            wp_cmd += (str(point)[1:-1] + ";")
        # Remove the Redundant ";" and Finish the Command
        wp_cmd = wp_cmd[:-1] + "])"

        # Update the arena
        self.plant.eng.eval(wp_cmd, nargout=0)

        # Reformat way_points to match evaluation definition
        self.way_points = list((self.way_points[j][1], self.way_points[j][0]) for j in range(len(self.way_points)))
        wp_l1 = self.way_points[-1]
        wp_l2 = self.way_points[-2]
        end_track = (wp_l1[0]-wp_l2[0], wp_l1[1]-wp_l2[1])
        wp_l1 = (end_track[0]/separation(wp_l1, wp_l2)*0.25+wp_l1[0],
                 end_track[1]/separation(wp_l1, wp_l2)*0.25+wp_l1[1])
        self.way_points = tuple(self.way_points[:-1]+[wp_l1])

    def _exe_act(self, action):

        input_values = {
            "disp_x": action[0],
            "disp_y": action[1],
        }
        self.plant.sim_set_input(input_values)

    def _get_obs(self):
        observation = np.moveaxis(self.plant.sim_get_output(["img_batch"])["img_batch"], [2], [0])
        print(observation.shape)
        return observation

    def _get_info(self):
        info = {
            "distance": separation(self.position, self.way_points[-1])
        }

        return info

    def _get_reward(self):
        reward = 0

        # Check Distance from Each Track Segment
        distance = [offtrack(self.way_points[j], self.way_points[j + 1], self.position)
                    for j in range(len(self.way_points)-1)]
        off_track = min(distance)
        print("="*10, "Reward Debug", "="*10)
        print("Way Points:", self.way_points)
        print("Position", self.position)
        print("Distance:", distance)

        if off_track < self.off_track_threshold:
            # Reward Progress along Track
            reward += projection(self.way_points[np.argmin(distance)],
                                 self.way_points[np.argmin(distance) + 1],
                                 self.displacement) * self.progress_reward_factor
        else:
            # Punish Off_Track
            reward -= 1

        if separation(self.position, self.way_points[-1]) <= self.finish_dist_threshold:
            self.finish_flag = True
            reward += self.finish_reward
            print("finish!")

        print("Reward:", reward)

        return reward

    def _update_eval_info(self):
        update_temp = self.plant.sim_get_output(["position"])

        self.displacement = (update_temp["position"][0]-self.position[0], update_temp["position"][1]-self.position[1])
        self.position = (update_temp["position"][0], update_temp["position"][1])
        self.height = -update_temp["position"][2]


if __name__ == "__main__":
    EnvTest = DroneEnv()

    while True:
        act = input("Drone ENV Test Agent:\n"
                    "\t1: reset environment\n"
                    "\t2: step environment\n"
                    "\t0: exit\n"
                    "action?\n")

        if act == "1":
            EnvTest.reset()
        elif act == "2":
            while True:
                k = input("Number of Steps:")
                try:
                    k = int(k)
                    break
                except ValueError:
                    continue
            while True:
                a1 = input("Displacement X:")
                try:
                    a1 = float(a1)
                    break
                except ValueError:
                    continue
            while True:
                a2 = input("Displacement Y:")
                try:
                    a2 = float(a2)
                    break
                except ValueError:
                    continue
            for i in range(k):
                EnvTest.step((a1, a2))
        elif act == "0":
            EnvTest.close()
            break
        else:
            continue
