import os
import sys


if "SUMO_HOME" in os.environ:
    tools = os.path.join(os.environ["SUMO_HOME"], "tools")
    sys.path.append(tools)
else:
    sys.exit("Please declare the environment variable 'SUMO_HOME'")
import numpy as np
import pandas as pd
import ray
import traci
from ray import tune
from ray.rllib.algorithms.ppo import PPOConfig
#from ray.rllib.env.wrappers.pettingzoo_env import ParallelPettingZooEnv
from pettingzooenv import ParallelPettingZooEnv
from ray.tune.registry import register_env

import sumo_rl

def env_creator(args):
    env = sumo_rl.parallel_env(
        net_file="4x4-Lucas/4x4.net.xml",
        route_file="4x4-Lucas/4x4c1c2c1c2.rou.xml",
        out_csv_name="4x4-Lucas/ppo",
        use_gui=False,
        num_seconds=1800,
        begin_time=100
    )
    return env


if __name__ == "__main__":
    ray.init()

    env_name = "4x4grid"

    register_env(
        env_name,
        lambda config: ParallelPettingZooEnv(
            env_creator(config)   
        )
    )

    config = (
        PPOConfig()
        .environment(env=env_name, disable_env_checking=True)
        .rollouts(num_rollout_workers=13, rollout_fragment_length=128)
        .training(
            train_batch_size=1664, # 1664 
            lr=2e-5,
            gamma=0.95,
            lambda_=0.9,
            use_gae=True,
            clip_param=0.4,
            grad_clip=None,
            entropy_coeff=0.1,
            vf_loss_coeff=0.25,
            sgd_minibatch_size=64,
            num_sgd_iter=10,
        )
        .debugging(log_level="ERROR")
        .framework(framework="torch")
        .resources(num_gpus=int(os.environ.get("RLLIB_NUM_GPUS", "0")))
    )
    path = os.path.join(os.path.expanduser("~"), "ray_results", env_name)
    tune.run(
        "PPO",
        name="PPO",
        stop={"timesteps_total": 100000},
        checkpoint_freq=1,

        local_dir=path, # 
        config=config.to_dict(),
    )
