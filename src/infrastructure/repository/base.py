from abc import ABC, abstractmethod

from domain.repository.base import CRUDRepository


class SQLAlchemyRepository(ABC):

    def __init__(self):
        pass


class CRUDSQLAlchemyRepository[ID, ENTITY](
    SQLAlchemyRepository,
    CRUDRepository,
    ABC,
):

    async def get(self, id_: ID) -> ENTITY | None: ...

    async def create(self, entity: ENTITY) -> None: ...

    async def update(self, entity: ENTITY) -> None: ...

    async def delete(self, id_: ID) -> None: ...

    @property
    @abstractmethod
    def entity(self) -> ENTITY: ...
