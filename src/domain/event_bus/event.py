from abc import abstractmethod, ABC
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


type ModelEvent = DomainEvent | IntegrationEvent


@dataclass(frozen=True, slots=True, kw_only=True)
class DomainEvent(ABC):
    pass


@dataclass(frozen=True, slots=True, kw_only=True)
class IntegrationEvent(ABC):
    _id: UUID = field(default_factory=uuid4)
    _created_at: datetime = field(default_factory=datetime.now)

    @abstractmethod
    def serialize(self) -> bytes: ...
