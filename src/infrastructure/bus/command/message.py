from abc import ABC

from infrastructure.bus.base.message import Message


class Command(Message, ABC):
    pass
