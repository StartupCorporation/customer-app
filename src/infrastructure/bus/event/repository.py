from collections import defaultdict

from domain.event_bus.event import IntegrationEvent
from infrastructure.message_broker.base.destination import MessageDestination


class IntegrationEventRepository:

    def __init__(self):
        self._mapper: dict[type[IntegrationEvent], list[MessageDestination]] = defaultdict(list)

    def add_event_destination(
        self,
        event: type[IntegrationEvent],
        destination: MessageDestination,
    ) -> None:
        self._mapper[event].append(destination)

    def get_destinations(
        self,
        event: type[IntegrationEvent],
    ) -> list[MessageDestination]:
        return self._mapper[event]
