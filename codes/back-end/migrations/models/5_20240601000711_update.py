from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `tms_user` ADD `nickname` VARCHAR(500) NOT NULL  COMMENT '用户昵称';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `tms_user` DROP COLUMN `nickname`;"""
