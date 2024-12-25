from abc import ABC

from infrastructure.bus.base.message import Message


class Event(Message, ABC):

    @classmethod
    @property
    def __event_name__(cls) -> str:
        return cls.__name__


class RawEvent(Message):
    event_name: str
    data: dict
