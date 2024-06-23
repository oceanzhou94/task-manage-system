"""
@Auth ： youngZ
@File ：login.py
"""

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.requests import Request

from models import User
from core import verify_password, create_access_token, deps
from scheams import (
    UserInPydantic,
    UserPydantic,
    ResponseSuccess,
    ResponseFailed,
)

login = APIRouter(tags=["认证相关"])


@login.post("/login", summary="用户登录")  # 路径host:port/tms/login
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    exist: bool = await User.filter(username=form_data.username).exists()
    if not exist:  # 判断用户名存在
        return ResponseFailed(message="用户名不存在", data={"username": form_data.username})

    user: User = await User.get(username=form_data.username)

    if not verify_password(form_data.password, user.password):  # 用户登录密码校验
        return ResponseFailed(message="用户名或密码错误", data={"username": form_data.username})

    token = create_access_token({"sub": user.username})
    return ResponseSuccess(
        message="登录成功",
        data={
            "username": user.username,
            "token": f"bearer {token}",
            "access_token": token,
        }
    )


@login.put("/logout", summary="退出登录")  # 路径host:port/tms/logout
async def user_logout(request: Request, user_obj: User = Depends(deps.get_current_user)):
    request.app.state.redis.delete(user_obj.username)
    return ResponseSuccess(message="退出成功", data=user_obj)


@login.post("/register", summary="用户注册")  # 路径host:port/tms/register
async def user_create(user_form: UserInPydantic):
    exist: bool = await User.filter(username=user_form.username).exists()
    if exist:  # 判断用户名存在
        return ResponseFailed(message="用户名已存在", data={"username": user_form.username})

    created_user = await UserPydantic.from_tortoise_orm(await User.create(**user_form.dict()))
    return ResponseSuccess(message="注册成功", data=created_user)
