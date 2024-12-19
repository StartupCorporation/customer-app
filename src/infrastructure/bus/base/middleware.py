from abc import ABC, abstractmethod
from typing import Callable, Awaitable, Any

from infrastructure.bus.base.message import Message


class MessageHandlerMiddleware[RESULT](ABC):

    @abstractmethod
    async def __call__(self, message: Message, next_: Callable[[Message], Awaitable[Any]]) -> RESULT:
        ...
