from abc import ABC, abstractmethod


class CRUDRepository[ID, ENTITY](ABC):

    @abstractmethod
    async def get(self, id_: ID) -> ENTITY | None: ...

    @abstractmethod
    async def save(self, entity: ENTITY) -> None: ...

    @abstractmethod
    async def delete(self, entity: ENTITY) -> None: ...
