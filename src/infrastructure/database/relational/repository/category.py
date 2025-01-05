from functools import cached_property
from uuid import UUID

from sqlalchemy import select, exists

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

    async def category_name_exists(
        self,
        name: str,
    ) -> bool:
        stmt = select(exists().where(Category.name == name))
        return await self._scalar(stmt)  # type: ignore

    @cached_property
    def entity_class(self) -> type[Category]:
        return Category
