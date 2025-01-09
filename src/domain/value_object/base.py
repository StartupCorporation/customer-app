from dataclasses import dataclass

from domain.event_bus.mixin import EventBased


@dataclass(kw_only=True, slots=True)
class ValueObject(EventBased):
    pass
