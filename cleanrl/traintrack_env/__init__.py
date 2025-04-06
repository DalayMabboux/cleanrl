from gymnasium.envs.registration import register

register(
    id="traintrack_env/Railway-v0",
    entry_point="traintrack_env.envs:RailwayEnv",
)
