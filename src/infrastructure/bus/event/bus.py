from collections import defaultdict
from typing import Callable, Awaitable, Iterable

from infrastructure.bus.base.bus import MessageBus
from infrastructure.bus.base.middleware import MessageHandlerMiddleware
from infrastructure.bus.event.handler import EventHandler
from infrastructure.bus.event.message import Event


class EventBus(MessageBus[None]):

    def __init__(
        self,
        middlewares: Iterable[MessageHandlerMiddleware] | None = None,
    ):
        self._event_handlers = defaultdict(list)
        self._middleware_chain: Callable[[Event], Awaitable[None]] = self._build_middleware_chain(
            middlewares=middlewares or [],
        )

    def register(
        self,
        message: type[Event],
        handler: EventHandler,
    ) -> None:
        self._event_handlers[message].append(handler)

    async def handle(self, message: Event) -> None:
        await self._middleware_chain(message)

    def _build_middleware_chain(
        self,
        middlewares: Iterable[MessageHandlerMiddleware],
    ) -> Callable[[Event], Awaitable[None]]:
        async def event_executor(message: Event) -> None:
            for handler in self._event_handlers[message.__class__]:
                await handler(message=message)

        def wrapped_middleware(
            middleware: MessageHandlerMiddleware,
            next_handler: Callable[[Event], Awaitable[None]],
        ) -> Callable[[Event], Awaitable[None]]:
            async def wrapped_handler(message: Event) -> None:
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
