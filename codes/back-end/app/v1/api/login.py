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
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token({"sub": user.username})
    return ResponseSuccess(
        message="登录成功",
        data={
            "token": f"bearer {token}",
            "access_token":token,
            "username": user.username
        }
    )


@login.put("/logout", summary="用户注销")  # 路径host:port/tms/logout
async def user_logout(request: Request, user: User = Depends(deps.get_current_user)):
    request.app.state.redis.delete(user.username)
    return ResponseSuccess(message="注销成功", data=user)


@login.post("/register", summary="用户注册")  # 路径host:port/tms/register
async def user_create(user: UserInPydantic):
    if await User.filter(username=user.username):
        return ResponseFailed(message="用户名已存在")
    user = await UserPydantic.from_tortoise_orm(await User.create(**user.dict()))
    return ResponseSuccess(message="注册成功", data=user)
