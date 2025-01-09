from abc import ABC, abstractmethod
from typing import Any, Awaitable, Callable


class BusMiddleware(ABC):

    @abstractmethod
    async def __call__(self, message: Any, next_: Callable[[Any], Awaitable[Any]]) -> Any: ...
