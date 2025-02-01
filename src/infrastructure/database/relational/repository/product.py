from functools import cached_property
from uuid import UUID

from sqlalchemy import select

from domain.entities.product import Product
from domain.repository.product import ProductRepository
from infrastructure.database.relational.repository.base import CRUDSQLAlchemyRepository


class SQLAlchemyProductRepository(
    CRUDSQLAlchemyRepository[UUID, Product],
    ProductRepository,
):

    async def get_by_external_id(
        self,
        external_id: UUID,
    ) -> Product | None:
        stmt = select(Product).where(Product.external_id == external_id)  # type: ignore
        return await self._scalar(stmt)

    @cached_property
    def entity_class(self) -> type[Product]:
        return Product
