from domain.entities.product import ProductID, Product
from domain.repository.product import ProductRepository
from infrastructure.repository.base import CRUDSQLAlchemyRepository


class SQLAlchemyProductRepository(
    CRUDSQLAlchemyRepository[ProductID, Product],
    ProductRepository,
):

    @property
    def entity(self) -> type[Product]:
        return Product
