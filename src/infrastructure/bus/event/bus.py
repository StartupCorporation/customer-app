from collections import defaultdict
from typing import Callable, Awaitable, Iterable

from domain.event_bus.bus import ModelEventBus
from domain.event_bus.event import ModelEvent
from infrastructure.bus.event.subscriber import EventSubscriber
from infrastructure.bus.middleware.base import BusMiddleware


class EventBus(ModelEventBus):

    def __init__(
        self,
        middlewares: Iterable[BusMiddleware] | None = None,
    ):
        self._event_subscribers: dict[type[ModelEvent], list[EventSubscriber]] = defaultdict(list)
        self._middleware_chain = self._build_middleware_chain(
            middlewares=middlewares or [],
        )

    def register(
        self,
        event: type[ModelEvent],
        subscriber: EventSubscriber,
    ) -> None:
        self._event_subscribers[event].append(subscriber)

    async def publish(
        self,
        event: ModelEvent,
    ) -> None:
        await self._middleware_chain(event)

    def _build_middleware_chain(
        self,
        middlewares: Iterable[BusMiddleware],
    ) -> Callable[[ModelEvent], Awaitable[None]]:
        async def event_executor(message: ModelEvent) -> None:
            for handler in self._event_subscribers[message.__class__]:
                await handler(
                    event=message,
                )

        def wrapped_middleware(
            middleware: BusMiddleware,
            next_handler: Callable[[ModelEvent], Awaitable[None]],
        ) -> Callable[[ModelEvent], Awaitable[None]]:
            async def wrapped_handler(event: ModelEvent) -> None:
                return await middleware(
                    message=event,
                    next_=next_handler,
                )

            return wrapped_handler

        for mdl in middlewares[::-1]:
            event_executor = wrapped_middleware(
                middleware=mdl,
                next_handler=event_executor,
            )

        return event_executor
