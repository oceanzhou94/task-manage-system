"""
@Auth ： youngZ
@File ：login.py
"""
import tortoise
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.requests import Request

from models import User
from core import verify_password, create_access_token, deps
from scheams import (
    UserInPydantic,
    UserPydantic,
    ResponseSuccess,
    ResponseFailed,
    ResponseToken,
)

login = APIRouter(tags=["认证相关"])


@login.post("/login", summary="用户登录")  # 路径host:port/tms/login
async def user_login(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        user = await User.get(username=form_data.username)
    except tortoise.exceptions.DoesNotExist:
        return ResponseFailed(message="用户名不存在", data={"username": form_data.username})

    if not verify_password(form_data.password, user.password):
        return ResponseFailed(message="用户密码错误", data={"username": form_data.username})

    token = create_access_token({"sub": user.username})
    return ResponseSuccess(
        message="登录成功",
        data={
            "username": user.username,
            "token": f"bearer {token}",
            "access_token":token,
        }
    )


@login.put("/logout", summary="退出登录")  # 路径host:port/tms/logout
async def user_logout(request: Request, user: User = Depends(deps.get_current_user)):
    request.app.state.redis.delete(user.username)
    return ResponseSuccess(message="退出成功", data=user)


@login.post("/register", summary="用户注册")  # 路径host:port/tms/register
async def user_create(user: UserInPydantic):
    is_exist = await User.filter(username=user.username)
    if is_exist:
        return ResponseFailed(message="用户名已存在",data={"username":user.username})
    user = await UserPydantic.from_tortoise_orm(await User.create(**user.dict()))
    return ResponseSuccess(message="注册成功", data=user)
