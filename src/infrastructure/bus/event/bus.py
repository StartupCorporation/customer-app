from collections import defaultdict
from typing import Callable, Awaitable, Iterable

from domain.event_bus.bus.global_ import GlobalDomainEventBus
from domain.events.base import DomainEvent
from infrastructure.bus.base.middleware import MessageHandlerMiddleware
from infrastructure.bus.event.subscriber import EventSubscriber


class EventBus(GlobalDomainEventBus):

    def __init__(
        self,
        middlewares: Iterable[MessageHandlerMiddleware] | None = None,
    ):
        self._event_subscribers = defaultdict(list)
        self._middleware_chain: Callable[[DomainEvent], Awaitable[None]] = self._build_middleware_chain(
            middlewares=middlewares or [],
        )

    def register(
        self,
        event: type[DomainEvent],
        subscriber: EventSubscriber,
    ) -> None:
        self._event_subscribers[event].append(subscriber)

    async def publish(self, event: DomainEvent) -> None:
        await self._middleware_chain(event)

    def _build_middleware_chain(
        self,
        middlewares: Iterable[MessageHandlerMiddleware],
    ) -> Callable[[DomainEvent], Awaitable[None]]:
        async def event_executor(message: DomainEvent) -> None:
            for handler in self._event_subscribers[message.__class__]:
                await handler(event=message)

        def wrapped_middleware(
            middleware: MessageHandlerMiddleware,
            next_handler: Callable[[DomainEvent], Awaitable[None]],
        ) -> Callable[[DomainEvent], Awaitable[None]]:
            async def wrapped_handler(message: DomainEvent) -> None:
                return await middleware(
                    message=message,
                    next_=next_handler,  # type: ignore
                )

            return wrapped_handler

        for mdl in middlewares[::-1]:
            event_executor = wrapped_middleware(
                middleware=mdl,
                next_handler=event_executor,
            )

        return event_executor
