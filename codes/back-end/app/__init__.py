"""
@Auth ： youngZ
@File ：__init__.py.py
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from core import TITLE, DESCRIPTIONS, TORTOISE_ORM
from .api import task

# 创建APP
app = FastAPI(title=TITLE, description=DESCRIPTIONS)

# 路由注册
app.include_router(task, prefix="/task")

# 跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 连接数据库
register_tortoise(
    app=app,
    config=TORTOISE_ORM,
    # generate_schemas=True,  # 如果数据库为空，则自动生成对应表单，生产环境不要开
    # add_exception_handlers=True,  # 生产环境不要开，会泄露调试信息
)
