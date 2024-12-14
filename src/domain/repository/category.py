from abc import ABC

from domain.entities.category import CategoryID, Category
from domain.repository.base import CRUDRepository


class CategoryRepository(CRUDRepository[CategoryID, Category], ABC):
    pass
