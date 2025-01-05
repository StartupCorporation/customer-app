from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class QueueConfig(BaseModel):
    NAME: str
    DURABLE: bool


class ConsumerSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="RABBITMQ_SUBSCRIBER_",
    )

    CATEGORY_QUEUE: QueueConfig


config = ConsumerSettings()
