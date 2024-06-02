"""
@Auth ： youngZ
@File ：configs.py
"""
import secrets

TITLE = "任务管理系统"

DESCRIPTIONS = "基于fastapi和tortoise-orm的任务管理系统"

TORTOISE_ORM = {
    "connections": {
        "default": {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': '127.0.0.1',
                'port': '3306',
                'user': 'root',
                'password': 'zhou123456',
                'database': 'task_manage_system_db',
                'minsize': 1,
                'maxsize': 5,
                'charset': 'utf8mb4',
                'echo': True
            }
        }
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        }
    },
    "use_tz": False,  # 建议不要开启，不然存储日期时会有很多坑，时区转换在项目中手动处理更稳妥。
    "timezone": "Asia/Shanghai"
}

# JWT
# token相关
ALGORITHM: str = "HS256"  # 加密算法
SECRET_KEY: str = secrets.token_urlsafe(32)  # 随机生成的base64位字符串
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # token的时效 7 天 = 60 * 24 * 7
