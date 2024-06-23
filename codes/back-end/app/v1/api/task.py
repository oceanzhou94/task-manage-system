"""
@Auth ： youngZ
@File ：task.py
"""
from core import deps
from fastapi import APIRouter, Depends
from models import User, Task
from scheams import TaskPydantic, TaskInPydantic, TaskWithPublisherPydantic
from scheams import ResponseSuccess, ResponseFailed

task = APIRouter(tags=["任务模块"], prefix="/task")


@task.get("/list", summary="查询所有任务")  # 路径host:port/tms/task/list
async def get_task_list(limit: int = 10, page: int = 1, user_obj: User = Depends(deps.get_current_user)):
    skip = (page - 1) * limit
    data = {
        "total": await Task.all().count(),
        "tasks": await TaskWithPublisherPydantic.from_queryset(
            Task.all().prefetch_related("publisher").offset(skip).limit(limit).order_by('id'))
    }

    return ResponseSuccess(message="查询成功", data=data)


@task.get("/info/{id}", summary="查询任务详细信息")  # 路径host:port/tms/task/info/1
async def get_task_by_id(id: int, user_obj: User = Depends(deps.get_current_user)):
    exist: bool = await Task.filter(id=id).exists()
    if not exist:
        return ResponseFailed(message="任务不存在", data=None)

    query_task = await TaskWithPublisherPydantic.from_tortoise_orm(await Task.get(id=id).prefetch_related("publisher"))
    return ResponseSuccess(message="查询成功", data=query_task)


@task.post("/create", summary="新增一条任务")  # 路径host:port/tms/task/create
async def create_task(task_form: TaskInPydantic, user_obj: User = Depends(deps.get_current_user)):
    created_task = await TaskInPydantic.from_tortoise_orm(await Task.create(**task_form.dict(), publisher=user_obj))

    return ResponseSuccess(message="新增成功", data=created_task)


@task.put("/update/{id}", summary="修改任务")  # 路径host:port/tms/task/update/1
async def update_task_by_id(id: int, task_form: TaskInPydantic, user_obj: User = Depends(deps.get_current_user)):
    exist: bool = await Task.filter(id=id).exists()
    if not exist:
        return ResponseFailed(message="任务不存在", data=None)

    old_task = await TaskPydantic.from_tortoise_orm(await Task.get(id=id))
    await Task.filter(id=id).update(**task_form.dict())  # 执行修改操作
    new_task = await TaskPydantic.from_tortoise_orm(await Task.get(id=id))

    return ResponseSuccess(message="修改成功", data={"old task": old_task, "new task": new_task})


@task.delete("/delete/{id}", summary="删除任务")  # 路径host:port/tms/task/delete/1
async def delete_task_by_id(id: int, user_obj: User = Depends(deps.get_current_user)):
    exist: bool = await Task.filter(id=id).exists()
    if not exist:
        return ResponseFailed(message="删除失败，任务不存在", data=None)

    delete_count = await Task.filter(id=id).delete()

    return ResponseSuccess(message="删除成功", data={"delete count": delete_count})
