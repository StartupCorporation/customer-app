from domain import Product, ProductID, ProductRepository
from infrastructure import CRUDSQLAlchemyRepository


class SQLAlchemyProductRepository(
    CRUDSQLAlchemyRepository[ProductID, Product],
    ProductRepository,
):

    @property
    def entity(self) -> type[Product]:
        return Product
