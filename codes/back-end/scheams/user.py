"""
@Auth ： youngZ
@File ：task.py
"""

from tortoise.contrib.pydantic import pydantic_model_creator

from models import User

UserPydantic = pydantic_model_creator(User, name="User", exclude=("password",))  # 模型序列化
UserInPydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)  # 表单模型序列化
UserUpdatePydantic = pydantic_model_creator(
    cls=User,
    name="UserUpdate",
    exclude=("id", "password", "created_time", "updated_time",)
)  # 用户修改模型
