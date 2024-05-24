"""
@Auth ： youngZ
@File ：task.py
"""

from fastapi import APIRouter
from models.task import Task

task = APIRouter(tags=["任务模块"])


@task.get("/list")  # 路径host:port/task/list
async def task_index():
    try:
        data = await Task.all()
    except Exception as error:
        return {
            "code": 400,
            "message": "query failed",
            "data": None
        }
    else:
        return {
            "code": 200,
            "message": "query success",
            "data": data
        }
