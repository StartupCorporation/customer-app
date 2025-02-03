from sqlalchemy import select

from application.queries.get_products.query import GetProductsQuery
from application.queries.get_products.result import GetProductsQueryResult, ProductShortInfo
from infrastructure.bus.query.handler import QueryHandler
from infrastructure.database.relational.connection import SQLDatabaseConnectionManager
from infrastructure.database.relational.models.product import Product


class GetProductsQueryHandler(QueryHandler[GetProductsQuery, GetProductsQueryResult]):

    def __init__(
        self,
        connection_manager: SQLDatabaseConnectionManager,
    ):
        self._connection_manager = connection_manager

    async def __call__(
        self,
        query: GetProductsQuery,  # noqa: ARG002
    ) -> GetProductsQueryResult:
        async with self._connection_manager.session() as session:
            stmt = select(
                Product.id,
                Product.category_id,
                Product.name,
                Product.images,
                Product.price,
            )
            results = await session.execute(stmt)

        return [
            ProductShortInfo(
                id=result.id,
                category_id=result.category_id,
                name=result.name,
                images=result.images,
                price=result.price,
            ) for result in results
        ]
