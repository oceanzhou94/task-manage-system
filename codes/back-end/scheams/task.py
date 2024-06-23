"""
@Auth ： youngZ
@File ：task.py
"""

from tortoise.contrib.pydantic import pydantic_model_creator

from models import Task

TaskPydantic = pydantic_model_creator(cls=Task, name="Task", )  # 模型序列化
TaskInPydantic = pydantic_model_creator(cls=Task, name="TaskIn", exclude_readonly=True)  # 表单模型序列化
TaskWithPublisherPydantic = pydantic_model_creator(
    cls=Task,
    name="TaskWithPublisher",
    include=("id", "description", "detail", "type", "price", "publisher", "created_time", "updated_time")
)  # 包含外键的模型序列化
