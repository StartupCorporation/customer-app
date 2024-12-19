from abc import ABC
from dataclasses import dataclass


@dataclass(kw_only=True, frozen=True, slots=True)
class Message(ABC):
    pass
