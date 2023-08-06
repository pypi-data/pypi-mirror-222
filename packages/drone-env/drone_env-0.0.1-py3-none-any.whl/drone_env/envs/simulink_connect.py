import matlab.engine
import numpy as np


class MatlabProjectPlant:
    def __init__(self, project_name, input_register, output_register):
        # Establish Variable for Connecting Model
        self.eng = None
        self.project_name = project_name

        # Load Input and Output Index
        # input_index: {key: (object, parameter)}
        # output_index: {key: (workspace_address)}
        self.input_index = input_register
        self.output_index = output_register

        # Create Output Value Storage
        self.output_value = {key: None for key in output_register.keys()}

    def connect_to_matlab(self):
        # Connect to Matlab
        print("Starting Matlab...")
        self.eng = matlab.engine.start_matlab()

        # Open the Matlab Project
        print("Opening Matlab Project...")
        self.eng.eval('openProject("{}");'.format(self.project_name), nargout=0)

        print("SUCCESS")

    def sim_start(self):
        # Start the Simulation and Pause Instantly
        print("Starting Simulink Model...")
        self.eng.set_param(self.project_name, 'SimulationCommand', 'start', 'SimulationCommand', 'pause', nargout=0)

        print("SUCCESS")

    def sim_set_input(self, input_update):
        for key, value in input_update.items():
            try:
                self.eng.set_param(self.input_index[key][0], self.input_index[key][1], str(value), nargout=0)
            except KeyError:
                print("Input Update Failure:", key)

    def sim_get_output(self, output_lookup):
        # Look up Simulink Workspace for Target Output
        output_values = {}
        for key in output_lookup:
            try:
                output_values[key] = np.array(self.eng.eval("{};".format(self.output_index[key]), nargout=1)).squeeze()
            except KeyError:
                print("Input Update Failure:", key)
        return output_values

    def sim_step(self):
        # Step the Simulation Forward
        if self.sim_get_status() != ('stopped' or 'terminating'):
            self.eng.set_param(self.project_name, 'SimulationCommand', 'step', nargout=0)

    def sim_stop(self):
        # Stop the Simulation
        self.eng.set_param(self.project_name, 'SimulationCommand', 'stop', nargout=0)

        print("Simulink Stopped")

    def disconnect(self):
        # Quit the Matlab Engine
        self.eng.quit()

    def sim_get_status(self):
        self.eng.get_param(self.project_name, 'SimulationStatus', nargout=1)


if __name__ == "__main__":
    # Initializing MatlabProjectPlant Class
    prj_name = "parrotMinidroneCompetition"
    input_index = {"X": ("flightControlSystem/Control System/Path Planning/xValue", "Value")}
    output_index = {"est_pos": "out.estimatedStates.signals.values(end,1:3)"}
    plant = MatlabProjectPlant(prj_name, input_index, output_index)

    # Test Methods in MatlabProjectPlant
    plant.connect_to_matlab()
    plant.sim_start()
    plant.sim_step()
    print(plant.sim_get_output(["est_pos"]))
    plant.sim_set_input({"X": 1})
    plant.sim_stop()
    plant.disconnect()
