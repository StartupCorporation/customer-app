from abc import ABC
from dataclasses import dataclass

from infrastructure.bus.base.message import Message


@dataclass(kw_only=True, slots=True, frozen=True)
class Query(Message, ABC):
    pass
