from abc import abstractmethod, ABC
from dataclasses import dataclass, field
from datetime import datetime
from typing import Self
from uuid import UUID, uuid4


type ModelEvent = DomainEvent | IntegrationEvent


@dataclass(frozen=True, slots=True, kw_only=True)
class DomainEvent(ABC):
    pass


@dataclass(frozen=True, slots=True, kw_only=True)
class IntegrationEvent(ABC):
    event_id: UUID = field(default_factory=uuid4)
    event_created_at: datetime = field(default_factory=datetime.now)

    @abstractmethod
    def serialize(self) -> dict: ...

    @classmethod
    @abstractmethod
    def deserialize(cls, data: dict) -> Self: ...
