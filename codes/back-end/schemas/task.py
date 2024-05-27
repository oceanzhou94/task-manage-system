"""
@Auth ： youngZ
@File ：task.py
"""

from tortoise.contrib.pydantic import pydantic_model_creator

from models import Task

TaskPydantic = pydantic_model_creator(Task, name="Task")  # 模型序列化
TaskInPydantic = pydantic_model_creator(Task, name="TaskIn", exclude_readonly=True)  # 表单模型序列化
