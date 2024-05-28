"""
@Auth ： youngZ
@File ：__init__.py.py
"""

from fastapi import APIRouter
from .api import task


v1 = APIRouter(prefix="/tms")

v1.include_router(task)