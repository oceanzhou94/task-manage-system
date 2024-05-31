"""
@Auth ： youngZ
@File ：user.py
"""
from typing import Optional, Iterable

from tortoise import fields, BaseDBAsyncClient
from enum import Enum
from tortoise.models import Model

from core import get_password_hash


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
    password = fields.CharField(max_length=200, null=False, description="用户密码")
    nickname = fields.CharField(max_length=500,null=False,description="用户昵称")
    gender = fields.CharEnumField(enum_type=GenderEnum, description="性别")
    telephone = fields.CharField(max_length=20, null=True, description="手机号")

    class Meta:
        table = "tms_user"
        table_description = "用户信息表"

    async def save(
            self,
            using_db: Optional[BaseDBAsyncClient] = None,
            update_fields: Optional[Iterable[str]] = None,
            force_create: bool = False,
            force_update: bool = False,
    ) -> None:
        if force_create or "password" in update_fields:
            self.password = get_password_hash(self.password)

        await super(User, self).save(using_db, update_fields, force_create, force_update)
