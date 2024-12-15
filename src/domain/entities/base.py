from typing import TypeVar, Generic, Any

from pydantic import BaseModel


ID = TypeVar("ID")


class Entity(BaseModel, Generic[ID]):
    id: ID

    def __eq__(self, other: Any) -> bool:
        return other.id == self.id if isinstance(other, Entity) else False
