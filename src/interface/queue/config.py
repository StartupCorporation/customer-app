from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class QueueConfig(BaseModel):
    NAME: str
    DURABLE: bool


class ConsumerSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="RABBITMQ_QUEUE_",
        env_nested_delimiter='__',
    )

    CATEGORY: QueueConfig


config = ConsumerSettings()
