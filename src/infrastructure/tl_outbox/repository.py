from abc import ABC, abstractmethod
from typing import Iterable
from uuid import UUID

from domain.event_bus.event import IntegrationEvent


class TransactionalOutboxRepository(ABC):

    @abstractmethod
    async def create(self, event: IntegrationEvent) -> None: ...

    @abstractmethod
    async def delete_by_id(self, id_: UUID) -> None: ...

    @abstractmethod
    async def get_unpublished_events(self, events_count: int) -> Iterable[IntegrationEvent]: ...
