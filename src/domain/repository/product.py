from abc import ABC

from domain.entities.product import ProductID, Product
from domain.repository.base import CRUDRepository


class ProductRepository(CRUDRepository[ProductID, Product], ABC):
    pass
