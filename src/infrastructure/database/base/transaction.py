from abc import ABC
from contextlib import asynccontextmanager


class DatabaseTransactionManager(ABC):

    @asynccontextmanager
    async def begin(self) -> None: ...
