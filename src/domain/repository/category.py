from abc import ABC

from domain import CRUDRepository, CategoryID, Category


class CategoryRepository(ABC, CRUDRepository[CategoryID, Category]): ...
