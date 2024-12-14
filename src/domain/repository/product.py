from abc import ABC

from domain import Product, ProductID, CRUDRepository


class ProductRepository(ABC, CRUDRepository[ProductID, Product]): ...
