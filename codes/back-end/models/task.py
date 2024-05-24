"""
@Auth ： youngZ
@File ：task.py
"""

from tortoise.models import Model
from tortoise import fields


class Task(Model):
    id = fields.IntField(pk=True, generated=True, description="唯一标识")
    description = fields.CharField(max_length=200, null=False, description="简要描述")
    detail = fields.TextField(null=False, description="详细描述")
    type = fields.CharField(max_length=100, description="类型")
    price = fields.FloatField(null=False)
    publisher = fields.ForeignKeyField(model_name="models.User")  # 外键

    class Meat:
        table = "tms_task"
        table_description = "任务信息表"
