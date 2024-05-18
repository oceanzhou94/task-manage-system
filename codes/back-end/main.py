"""
@Auth ： youngZ
@File ：main.py
"""
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def main():
    return {
        "code": 200,
        "message": "请求成功",
        "data": "null",
    }


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
