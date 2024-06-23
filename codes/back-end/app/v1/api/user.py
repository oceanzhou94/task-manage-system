from fastapi import APIRouter, Depends, Body

from core import deps

from scheams import UserPydantic, UserUpdatePydantic, ResponseSuccess
from models import User

user = APIRouter(tags=["用户相关"], prefix="/user")


@user.get("/me", summary="查询当前用户信息")  # 路径host:port/tms/user/me
async def user_info(user_obj: User = Depends(deps.get_current_user)):
    """
    - username: str 必传
    - password: str 必传
    """
    data = await UserPydantic.from_tortoise_orm(user_obj)
    return ResponseSuccess(message="查询成功", data=data)


@user.get("/list", summary="查询全部用户信息")  # 路径host:port/tms/user/list
async def user_list(limit: int = 10, page: int = 1, user_obj: User = Depends(deps.get_current_user)):
    skip = (page - 1) * limit
    data = {
        "total": await User.all().count(),
        "users": await UserPydantic.from_queryset(User.all().offset(skip).limit(limit).order_by('id'))
    }
    return ResponseSuccess(message="查询成功", data=data)


@user.put("/update", summary="修改当前用户信息")  # 路径host:port/tms/user/update
async def user_update(user_form: UserUpdatePydantic, user_obj: User = Depends(deps.get_current_user)):
    """
    修改当前用户信息
    """
    old_user_info = await UserPydantic.from_tortoise_orm(await User.get(id=user_obj.id))
    await User.filter(id=user_obj.id).update(**user_form.dict())
    new_user_info = await UserPydantic.from_tortoise_orm(await User.get(id=user_obj.id))
    data = {"old user": old_user_info, "new user": new_user_info}
    return ResponseSuccess(message="修改成功", data=data)
