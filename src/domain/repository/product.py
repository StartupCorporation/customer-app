from abc import ABC
from uuid import UUID

from domain.entities.product import Product
from domain.repository.base import CRUDRepository


class ProductRepository(CRUDRepository[UUID, Product], ABC):
    pass
