from abc import ABC, abstractmethod
from typing import Callable, Awaitable

from domain.events.base import DomainEvent


class DomainEventBus(ABC):

    @abstractmethod
    async def publish(self, event: type[DomainEvent]) -> None: ...

    @abstractmethod
    def register(self, event: type[DomainEvent], handler: Callable[[DomainEvent], Awaitable[None]]) -> None: ...
