from typing import Callable, Awaitable

from infrastructure.bus.base.message import Message
from infrastructure.bus.base.middleware import MessageHandlerMiddleware
from infrastructure.bus.impl.event.message import RawEvent
from infrastructure.bus.impl.event.repository import EventHandlerRepository


class EventConstructorMiddleware(MessageHandlerMiddleware[None]):

    def __init__(
        self,
        event_handler_repository: EventHandlerRepository,
    ):
        self._event_handler_repository = event_handler_repository

    async def __call__(
        self,
        message: Message | RawEvent,
        next_: Callable[[Message], Awaitable[None]],
    ) -> None:
        if isinstance(message, RawEvent):
            event_class = self._event_handler_repository.find_event_by_name(
                name=message.event_name,
            )

            if not event_class:
                return

            message = event_class.model_validate(message.payload)

        await next_(message)
