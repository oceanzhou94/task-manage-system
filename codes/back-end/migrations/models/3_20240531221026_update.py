from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `task` RENAME TO `tms_task`;
        ALTER TABLE `user` RENAME TO `tms_user`;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `tms_task` RENAME TO `task`;
        ALTER TABLE `tms_user` RENAME TO `user`;"""
