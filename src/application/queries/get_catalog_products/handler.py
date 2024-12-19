from sqlalchemy import select

from application.queries.get_catalog_products.query import GetCategoryProductsQuery
from application.queries.get_catalog_products.result import GetCategoryProductsQueryResult, CategoryProduct
from infrastructure.bus.query.handler import QueryHandler
from infrastructure.database.connection import AsyncSQLDatabaseConnectionManager
from infrastructure.database.models.product import Product


class GetCategoryProductsQueryHandler(QueryHandler[GetCategoryProductsQueryResult]):

    def __init__(
        self,
        connection_manager: AsyncSQLDatabaseConnectionManager,
    ):
        self._connection_manager = connection_manager

    async def __call__(
        self,
        message: GetCategoryProductsQuery,
    ) -> GetCategoryProductsQueryResult:
        async with self._connection_manager.connect() as session:
            stmt = select(
                Product.id,
                Product.name,
                Product.images,
            ).where(
                Product.category_id == message.category_id,
            )
            results = await session.execute(stmt)

        return [
            CategoryProduct(
                id=result.id,
                name=result.name,
                images=result.images,
            ) for result in results
        ]
