import numpy as np
import torch


def flat_observation(observation):
    return torch.from_numpy(
        np.concatenate(
            [
                observation["orientations"],  # orientations 数组
                np.array([observation["height"]]),  # height 数值（需要转换为一维数组）
                observation["velocity"],  # velocity 数组
            ]
        )
    )
