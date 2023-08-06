from gymnasium.envs.registration import register

register(
    id="drone_env/DroneEnv-v0",
    entry_point="drone_env.envs:DroneEnv",
    max_episode_steps=100000
)