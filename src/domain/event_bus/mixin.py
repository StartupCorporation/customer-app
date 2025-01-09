from abc import ABC
from dataclasses import dataclass, field

from domain.event_bus.event import ModelEvent


@dataclass(kw_only=True)
class EventBased(ABC):
    __events: list[ModelEvent] = field(default_factory=list)

    def flush_events(self) -> list[ModelEvent]:
        flushed_events, self.__events = self.__events, []
        return flushed_events

    def _add_event(
        self,
        event: ModelEvent,
    ) -> None:
        self.__events.append(event)
