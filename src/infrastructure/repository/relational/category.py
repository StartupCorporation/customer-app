from functools import cached_property

from sqlalchemy import select

from domain.entities.category import CategoryID, Category
from domain.repository.category import CategoryRepository
from infrastructure.repository.relational.base import CRUDSQLAlchemyRepository


class SQLAlchemyCategoryRepository(
    CRUDSQLAlchemyRepository[CategoryID, Category],
    CategoryRepository,
):

    async def get_all(self) -> list[Category]:
        stmt = select(self.entity_class)
        return await self._scalars(stmt)

    @cached_property
    def entity_class(self) -> type[Category]:
        return Category
