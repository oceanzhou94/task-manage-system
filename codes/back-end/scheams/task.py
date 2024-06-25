"""
@Auth ： youngZ
@File ：task.py
"""

from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise import Tortoise
from models import Task

Tortoise.init_models(["models"], app_label="models")  # 解决序列化后的模型缺失外键字段的问题

TaskPydantic = pydantic_model_creator(cls=Task, name="Task", )  # 模型序列化
TaskInPydantic = pydantic_model_creator(cls=Task, name="TaskIn", exclude_readonly=True)  # 表单模型序列化
