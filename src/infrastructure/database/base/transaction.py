from abc import ABC
from contextlib import asynccontextmanager
from typing import Any, Coroutine


class DatabaseTransactionManager(ABC):

    @asynccontextmanager # type: ignore
    async def begin(self) -> Coroutine[Any, Any, None]: ...
