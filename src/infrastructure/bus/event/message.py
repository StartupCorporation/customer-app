from abc import ABC

from infrastructure.bus.base.message import Message


class Event(Message, ABC):
    pass
