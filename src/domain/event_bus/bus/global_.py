from abc import abstractmethod
from typing import Awaitable, Callable

from domain.event_bus.bus.base import DomainEventBus
from domain.events.base import DomainEvent


class GlobalDomainEventBus(DomainEventBus):

    @abstractmethod
    async def publish(self, event: DomainEvent) -> None: ...

    @abstractmethod
    def register(self, event: type[DomainEvent], subscriber: Callable[[DomainEvent], Awaitable[None]]) -> None: ...
