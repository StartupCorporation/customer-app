from abc import ABC

from infrastructure.bus.base.message import Message


class Query(Message, ABC):
    pass
