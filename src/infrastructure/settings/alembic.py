from pydantic_settings import SettingsConfigDict

from infrastructure.settings.database import DatabaseSettings


class AlembicSettings(DatabaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="ALEMBIC_",
    )

    @property
    def db_url(self) -> str:
        return f'postgresql+asyncpg://{self.USERNAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}'

