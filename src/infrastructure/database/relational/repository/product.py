from functools import cached_property
from uuid import UUID

from domain.entities.product import Product
from domain.repository.product import ProductRepository
from infrastructure.database.relational.repository.base import CRUDSQLAlchemyRepository


class SQLAlchemyProductRepository(
    CRUDSQLAlchemyRepository[UUID, Product],
    ProductRepository,
):

    @cached_property
    def entity_class(self) -> type[Product]:
        return Product
