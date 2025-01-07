from collections import defaultdict
from typing import Callable, Awaitable

from domain.event_bus.bus.base import DomainEventBus
from domain.events.base import DomainEvent


class LocalDomainEventBus(DomainEventBus):

    def __init__(self):
        self._event_handlers: dict[
            type[DomainEvent],
            list[Callable[[DomainEvent], Awaitable[None]]],
        ] = defaultdict(list)

    async def publish(
        self,
        event: DomainEvent,
    ) -> None:
        for handler in self._event_handlers[event.__class__]:
            await handler(event)

    def register(
        self,
        event: type[DomainEvent],
        handler: Callable[[DomainEvent], Awaitable[None]],
    ) -> None:
        self._event_handlers[event].append(handler)
