from functools import cached_property
from uuid import UUID

from sqlalchemy import select

from domain.entities.category import Category
from domain.repository.category import CategoryRepository
from infrastructure.database.relational.repository.base import CRUDSQLAlchemyRepository


class SQLAlchemyCategoryRepository(
    CRUDSQLAlchemyRepository[UUID, Category],
    CategoryRepository,
):

    async def get_by_external_id(
        self,
        id_: UUID,
    ) -> Category | None:
        stmt = select(Category).where(Category.external_id == id_)
        return await self._scalar(stmt)

    @cached_property
    def entity_class(self) -> type[Category]:
        return Category
