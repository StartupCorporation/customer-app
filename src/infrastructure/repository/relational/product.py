from functools import cached_property

from domain.entities.product import ProductID, Product
from domain.repository.product import ProductRepository
from infrastructure.repository.relational.base import CRUDSQLAlchemyRepository


class SQLAlchemyProductRepository(
    CRUDSQLAlchemyRepository[ProductID, Product],
    ProductRepository,
):

    @cached_property
    def entity_class(self) -> type[Product]:
        return Product
