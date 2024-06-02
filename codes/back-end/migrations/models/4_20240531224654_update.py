from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `tms_user` MODIFY COLUMN `password` VARCHAR(200) NOT NULL  COMMENT '用户密码';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `tms_user` MODIFY COLUMN `password` VARCHAR(50) NOT NULL  COMMENT '用户密码';"""
