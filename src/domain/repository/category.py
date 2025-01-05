from abc import ABC, abstractmethod
from uuid import UUID

from domain.entities.category import Category
from domain.repository.base import CRUDRepository


class CategoryRepository(CRUDRepository[UUID, Category], ABC):

    @abstractmethod
    async def get_by_external_id(self, id_: UUID) -> Category | None: ...

    @abstractmethod
    async def category_name_exists(self, name: str) -> bool: ...
