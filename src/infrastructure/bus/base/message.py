from abc import ABC

from pydantic import BaseModel


class Message(BaseModel, ABC):
    pass
