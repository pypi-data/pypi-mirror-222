from .envs.drone_env import DroneEnv

from gymnasium.envs.registration import register

register(
    id="drone_env_v0",
    entry_point="drone_env.envs:DroneEnv",
)
