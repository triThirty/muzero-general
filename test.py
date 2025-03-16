from dm_control import suite
from dm_control import viewer
import numpy as np

# 加载 Hopper 任务
env = suite.load(domain_name="walker", task_name="walk")

# print(env.reset().observation)
env.task.random.seed(0)
print(type(env.reset().observation["orientations"]))



# # 定义一个随机策略，让 Hopper 运动
# def random_policy(time_step):
#     return np.random.uniform(
#         env.action_spec().minimum, env.action_spec().maximum, env.action_spec().shape
#     )


# # 运行 viewer 并使用随机策略
# viewer.launch(env, policy=None)
