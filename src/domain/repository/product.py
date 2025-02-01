from abc import ABC, abstractmethod
from uuid import UUID

from domain.entities.product import Product
from domain.repository.base import CRUDRepository


class ProductRepository(CRUDRepository[UUID, Product], ABC):

    @abstractmethod
    async def get_by_external_id(self, external_id: UUID) -> Product | None: ...
