"""
@Auth ： youngZ
@File ：task.py
"""

from tortoise import fields
from tortoise.models import Model


class BaseModel(Model):
    """基础模型，添加创建时间和更新时间"""
    created_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    updated_time = fields.DatetimeField(auto_now=True, description="更新时间")

    class Meta:
        abstract = True  # 抽象模型，将不会在数据库中创建表


class Task(BaseModel):
    id = fields.IntField(pk=True, generated=True, description="唯一标识")
    description = fields.CharField(max_length=200, null=False, description="简要描述")
    detail = fields.TextField(null=False, description="详细描述")
    type = fields.CharField(max_length=100, description="类型")
    price = fields.FloatField(null=False)
    publisher = fields.ForeignKeyField(model_name="models.User")  # 外键

    class Meta:
        table = "tms_task"
        table_description = "任务信息表"
