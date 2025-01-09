from typing import Callable, Awaitable, Any

from domain.event_bus.event import ModelEvent, IntegrationEvent, DomainEvent
from infrastructure.bus.event.repository import IntegrationEventRepository
from infrastructure.bus.middleware.base import BusMiddleware
from infrastructure.message_broker.base.manager import MessageBrokerPublisher


class ModelEventDispatcherMiddleware(BusMiddleware):

    def __init__(
        self,
        message_broker_publisher: MessageBrokerPublisher,
        integration_event_repository: IntegrationEventRepository,
    ):
        self._message_broker_publisher = message_broker_publisher
        self._integration_event_repository = integration_event_repository

    async def __call__(
        self,
        message: ModelEvent,
        next_: Callable[[ModelEvent], Awaitable[Any]],
    ) -> Any:
        if isinstance(message, IntegrationEvent):
            for destination in self._integration_event_repository.get_destinations(
                event=message.__class__,
            ):
                await self._message_broker_publisher.publish(
                    destination=destination,
                    message=message.serialize(),
                )
        if isinstance(message, DomainEvent):
            await next_(message)
