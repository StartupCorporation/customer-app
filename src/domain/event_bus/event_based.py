from abc import ABC
from dataclasses import dataclass, field

from domain.events.base import DomainEvent


@dataclass(kw_only=True)
class EventBased(ABC):
    __events: list[DomainEvent] = field(default_factory=list)

    def _add_event(
        self,
        event: DomainEvent,
    ) -> None:
        self.__events.append(event)

    def flush_events(self) -> list[DomainEvent]:
        flushed_events, self.__events = self.__events, []
        return flushed_events
