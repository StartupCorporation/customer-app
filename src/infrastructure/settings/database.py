from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="DATABASE_",
    )

    HOST: str
    PORT: int
    DATABASE: str
    USERNAME: str
    PASSWORD: str
