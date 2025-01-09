from dataclasses import dataclass
from typing import Any

from domain.event_bus.mixin import EventBased


@dataclass(kw_only=True)
class Entity[ID](EventBased):
    id: ID

    def __eq__(self, other: Any) -> bool:
        return other.id == self.id if isinstance(other, Entity) else False
