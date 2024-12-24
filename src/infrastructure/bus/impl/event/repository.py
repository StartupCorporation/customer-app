from collections import defaultdict

from infrastructure.bus.impl.event.exception.event_name_duplication import EventNameDuplication
from infrastructure.bus.impl.event.handler import EventHandler
from infrastructure.bus.impl.event.message import Event


class EventHandlerRepository:

    def __init__(self):
        self._events = defaultdict(list)

    def add(
        self,
        event: type[Event],
        handler: EventHandler,
    ) -> None:
        if any(map(lambda existing_event: event.__event_name__ == existing_event.__event_name__, self._events)):
            raise EventNameDuplication(
                detail=f"Event with name {event.__event_name__} already exists.",
            )

        self._events[event].append(handler)

    def find_event_by_name(
        self,
        name: str,
    ) -> type[Event] | None:
        for event in self._events:
            if event.__event_name__ == name:
                return event

    def find_handler_by_event(
        self,
        event: type[Event],
    ) -> list[EventHandler]:
        return self._events.get(event, [])
