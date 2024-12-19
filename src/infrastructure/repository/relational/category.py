from functools import cached_property
from uuid import UUID

from domain.entities.category import Category
from domain.repository.category import CategoryRepository
from infrastructure.repository.relational.base import CRUDSQLAlchemyRepository


class SQLAlchemyCategoryRepository(
    CRUDSQLAlchemyRepository[UUID, Category],
    CategoryRepository,
):

    @cached_property
    def entity_class(self) -> type[Category]:
        return Category
