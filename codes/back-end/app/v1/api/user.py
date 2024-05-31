from fastapi import APIRouter, Depends, Body

from core import deps

from scheams import UserPydantic, UserInPydantic, ResponseSuccess, ResponseFailed
from models import User

user = APIRouter(tags=["用户相关"], prefix="/user")


@user.get("/me", summary="当前用户")  # 路径host:port/tms/user/me
async def user_info(user_obj: User = Depends(deps.get_current_user)):
    """
    - username: str 必传
    - password: str 必传
    """
    data = await UserPydantic.from_tortoise_orm(user_obj)
    return ResponseSuccess(data=data, message="查询成功")


@user.get("/list", summary="全部用户")  # 路径host:port/tms/user/list
async def user_list(limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    data = {
        "total": await User.all().count(),
        "tasks": await UserPydantic.from_queryset(User.all().offset(skip).limit(limit).order_by('id'))
    }
    return ResponseSuccess(data=data, message="查询成功")


@user.put("/update", summary="修改信息")  # 路径host:port/tms/user/update
async def user_update(user_form: UserInPydantic, user_obj: User = Depends(deps.get_current_user)):
    """
    修改当前用户信息
    """

    update_data = user_form.dict(exclude_unset=True)
    await User.filter(username=user_obj.username).update(**update_data)
    updated_user = await User.get(username=user_obj.username)
    data = await UserPydantic.from_tortoise_orm(updated_user)
    return ResponseSuccess(message="修改成功", data=data)
