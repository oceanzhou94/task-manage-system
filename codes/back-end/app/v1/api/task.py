"""
@Auth ： youngZ
@File ：task.py
"""

from fastapi import APIRouter, Form
from models.task import Task
from schemas import TaskPydantic, TaskInPydantic, ResponseSuccess, ResponseFailed

task = APIRouter(tags=["任务模块"],prefix="/task")


@task.get("/list", summary="任务列表")  # 路径host:port/tms/task/list
async def get_task_list(limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    try:
        data = {
            "total": await Task.all().count(),
            "tasks": await TaskPydantic.from_queryset(Task.all().offset(skip).limit(limit).order_by('-id'))
        }
    except Exception as error:
        return ResponseFailed(data=error, message="查询失败")
    else:
        return ResponseSuccess(data=data, message="查询成功")


@task.post("/create", summary="新增任务")  # 路径host:port/tms/task/create
async def create_task(task_form: TaskInPydantic):
    try:
        data = await TaskInPydantic.from_tortoise_orm(
            await Task.create(**task_form.dict())
        )
    except Exception as error:
        return ResponseFailed(data=error, message="新增失败")
    else:
        return ResponseSuccess(data=data, message="新增成功")
