from pydantic_settings import BaseSettings, SettingsConfigDict


class ApplicationSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="APPLICATION_",
    )

    DEBUG: bool
    DESCRIPTION: str
    VERSION: str
