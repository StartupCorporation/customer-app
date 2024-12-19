from sqlalchemy import select

from application.queries.get_catalogs.query import GetCategoriesQuery
from application.queries.get_catalogs.result import CategoryQueryResult, CategoryData
from infrastructure.bus.query.handler import QueryHandler
from infrastructure.database.connection import AsyncSQLDatabaseConnectionManager
from infrastructure.database.models.category import Category


class GetCategoriesQueryHandler(QueryHandler[CategoryQueryResult]):

    def __init__(
        self,
        connection_manager: AsyncSQLDatabaseConnectionManager,
    ):
        self._connection_manager = connection_manager

    async def __call__(
        self,
        message: GetCategoriesQuery,
    ) -> CategoryQueryResult:
        async with self._connection_manager.connect() as session:
            stmt = select(Category)
            results = await session.scalars(stmt)

        return [
            CategoryData(
                id=result.id,
                name=result.name,
                description=result.description,
                image=result.image,
            ) for result in results
        ]
