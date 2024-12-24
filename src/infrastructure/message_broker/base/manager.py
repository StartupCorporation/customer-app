from abc import ABC, abstractmethod
from typing import AsyncIterator


class MessageBrokerManager(ABC):

    @abstractmethod
    async def consume(self, queue: str) -> AsyncIterator[bytes]: ...
