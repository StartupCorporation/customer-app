from pydantic_settings import BaseSettings, SettingsConfigDict


class ConsumerSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="RABBITMQ_CUSTOMER_",
    )

    CATEGORY_QUEUE: str


config = ConsumerSettings()  # type: ignore
