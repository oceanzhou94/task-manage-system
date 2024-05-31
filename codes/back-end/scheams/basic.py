"""
@Auth ： youngZ
@File ：basic.py
"""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class CodeEnum(int, Enum):
    """业务状态码"""
    SUCCESS = 200
    FAILED = 400


class ResponseSuccess(BaseModel):
    code: CodeEnum = CodeEnum.SUCCESS
    message: str = "请求成功"
    data: Any = None


class ResponseFailed(BaseModel):
    code: CodeEnum = CodeEnum.FAILED
    message: str = "请求失败"
    data: Any = None


class ResponseToken(ResponseSuccess):
    access_token: str
    token_type: str = Field(default="bearer")
