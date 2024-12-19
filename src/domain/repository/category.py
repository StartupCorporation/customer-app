from abc import ABC
from uuid import UUID

from domain.entities.category import Category
from domain.repository.base import CRUDRepository


class CategoryRepository(CRUDRepository[UUID, Category], ABC):
    pass
