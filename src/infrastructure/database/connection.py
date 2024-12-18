from asyncio import current_task
from contextlib import asynccontextmanager
from functools import cached_property
from typing import AsyncContextManager

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    AsyncSession, AsyncEngine, create_async_engine, async_sessionmaker,
    async_scoped_session,
)

from infrastructure.settings.database import DatabaseSettings


class AsyncSQLDatabaseConnectionManager:

    def __init__(
        self,
        settings: DatabaseSettings,
    ) -> None:
        self._settings = settings

    @asynccontextmanager
    async def connect(self) -> AsyncContextManager[AsyncSession]:
        yield self._session()

    @cached_property
    def _engine(self) -> AsyncEngine:
        return create_async_engine(
            URL.create(
                drivername="postgresql+asyncpg",
                username=self._settings.USERNAME,
                password=self._settings.PASSWORD,
                database=self._settings.DATABASE,
                host=self._settings.HOST,
                port=self._settings.PORT,
            ),
        )

    @cached_property
    def _session_factory(self) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(
            bind=self._engine,
            expire_on_commit=True,
        )

    @cached_property
    def _session(self) -> async_scoped_session[AsyncSession]:
        return async_scoped_session(
            session_factory=self._session_factory,
            scopefunc=current_task,
        )
