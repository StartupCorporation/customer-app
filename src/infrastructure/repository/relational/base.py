from abc import ABC, abstractmethod
from functools import cached_property

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.base import Entity
from domain.repository.base import CRUDRepository
from infrastructure.database.connection import AsyncSQLDatabaseConnection


class SQLAlchemyRepository(ABC):

    def __init__(
        self,
        connection_manager: AsyncSQLDatabaseConnection,
    ):
        self._connection_manager = connection_manager


class CRUDSQLAlchemyRepository[ID, ENTITY: Entity](
    SQLAlchemyRepository,
    CRUDRepository,
    ABC,
):

    async def get(self, id_: ID) -> ENTITY | None:
        stmt = select(self.entity_class).where(self.entity_class.id == id_)
        return await self._scalar(stmt)

    async def save(self, entity: ENTITY) -> None:
        async with self._connection_manager.connect() as session:
            session.add(entity)

    async def delete_by_id(self, id_: ID) -> None:
        stmt = delete(self.entity_class).where(self.entity_class.id == id_)
        await self._execute(stmt)

    async def _scalars(self, *args, **kwargs) -> list[ENTITY]:
        session: AsyncSession

        async with self._connection_manager.connect() as session:
            return (await session.scalars(*args, **kwargs)).unique().all()  # type: ignore

    async def _scalar(self, *args, **kwargs) -> ENTITY | None:
        session: AsyncSession

        async with self._connection_manager.connect() as session:
            return await session.scalar(*args, **kwargs)

    async def _execute(self, *args, **kwargs) -> None:
        session: AsyncSession

        async with self._connection_manager.connect() as session:
            await session.execute(*args, **kwargs)

    @cached_property
    @abstractmethod
    def entity_class(self) -> type[ENTITY]: ...
