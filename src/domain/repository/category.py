from abc import ABC, abstractmethod

from domain.entities.category import CategoryID, Category
from domain.repository.base import CRUDRepository


class CategoryRepository(CRUDRepository[CategoryID, Category], ABC):

    @abstractmethod
    async def get_all(self) -> list[Category]: ...
