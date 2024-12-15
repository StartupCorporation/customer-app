from abc import ABC, abstractmethod


class CRUDRepository[ID, ENTITY](ABC):

    @abstractmethod
    async def get(self, id_: ID) -> ENTITY | None: ...

    @abstractmethod
    async def create(self, entity: ENTITY) -> None: ...

    @abstractmethod
    async def update(self, entity: ENTITY) -> None: ...

    @abstractmethod
    async def delete(self, id_: ID) -> None: ...
