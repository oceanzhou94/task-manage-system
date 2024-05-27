"""
@Auth ： youngZ
@File ：user.py
"""

from tortoise import fields
from enum import Enum
from tortoise.models import Model


class BaseModel(Model):
    """基础模型，添加创建时间和更新时间"""
    created_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    updated_time = fields.DatetimeField(auto_now=True, description="更新时间")

    class Meta:
        abstract = True  # 抽象模型，将不会在数据库中创建表


class GenderEnum(Enum):
    """性别枚举类"""
    MALE = "男"
    FEMALE = "女"
    SECRET = "保密"


class User(BaseModel):
    id = fields.IntField(pk=True, generated=True, description="唯一标识")
    username = fields.CharField(max_length=50, null=False, description="用户名")
    password = fields.CharField(max_length=50, null=False, description="用户密码")
    gender = fields.CharEnumField(enum_type=GenderEnum, description="性别")
    telephone = fields.CharField(max_length=20, null=True, description="手机号")

    class Meat:
        table = "tms_user"
        table_description = "用户信息表"
