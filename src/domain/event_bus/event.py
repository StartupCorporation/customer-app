from abc import abstractmethod, ABC
from dataclasses import dataclass, field
from datetime import datetime
from typing import Self, ClassVar
from uuid import UUID, uuid4


type ModelEvent = DomainEvent | IntegrationEvent


@dataclass(frozen=True, slots=True, kw_only=True)
class DomainEvent(ABC):
    pass


@dataclass(frozen=True, slots=True, kw_only=True)
class IntegrationEvent(ABC):
    __event_name__: ClassVar[str]
    __event_id__: UUID = field(default_factory=uuid4)
    __event_created_at__: datetime = field(default_factory=datetime.now)

    @abstractmethod
    def serialize(self) -> dict: ...

    @classmethod
    @abstractmethod
    def deserialize(cls, data: dict) -> Self: ...
