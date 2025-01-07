from abc import ABC, abstractmethod
from typing import AsyncIterator


class MessageBrokerPublisher(ABC):

    @abstractmethod
    async def publish(
        self,
        destination: str,
        message: dict,
        **kwargs,
    ) -> AsyncIterator[bytes]: ...
