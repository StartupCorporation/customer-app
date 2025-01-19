from typing import Callable, Awaitable, Any

from domain.event_bus.event import ModelEvent, IntegrationEvent, DomainEvent
from infrastructure.bus.middleware.base import BusMiddleware
from infrastructure.tl_outbox.repository import TransactionalOutboxRepository


class ModelEventDispatcherMiddleware(BusMiddleware):

    def __init__(
        self,
        transactional_outbox_repository: TransactionalOutboxRepository,
    ):
        self._transactional_outbox_repository = transactional_outbox_repository

    async def __call__(
        self,
        message: ModelEvent,
        next_: Callable[[ModelEvent], Awaitable[Any]],
    ) -> Any:
        if isinstance(message, IntegrationEvent):
            await self._transactional_outbox_repository.create(
                event=message,
            )
        if isinstance(message, DomainEvent):
            await next_(message)
