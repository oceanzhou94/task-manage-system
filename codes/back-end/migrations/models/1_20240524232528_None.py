from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `user` (
    `created_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `updated_time` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '唯一标识',
    `username` VARCHAR(50) NOT NULL  COMMENT '用户名',
    `password` VARCHAR(50) NOT NULL  COMMENT '用户密码',
    `gender` VARCHAR(2) NOT NULL  COMMENT '性别',
    `telephone` VARCHAR(20)   COMMENT '手机号'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `task` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '唯一标识',
    `description` VARCHAR(200) NOT NULL  COMMENT '简要描述',
    `detail` LONGTEXT NOT NULL  COMMENT '详细描述',
    `type` VARCHAR(100) NOT NULL  COMMENT '类型',
    `price` DOUBLE NOT NULL,
    `publisher_id` INT NOT NULL,
    CONSTRAINT `fk_task_user_67d3244c` FOREIGN KEY (`publisher_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
