from sqlalchemy import select

from application.queries.get_categories.query import GetCategoriesQuery
from application.queries.get_categories.result import CategoryQueryResult, CategoryData
from infrastructure.bus.query.handler import QueryHandler
from infrastructure.database.relational.connection import SQLDatabaseConnectionManager
from infrastructure.database.relational.models.category import Category


class GetCategoriesQueryHandler(QueryHandler[CategoryQueryResult]):

    def __init__(
        self,
        connection_manager: SQLDatabaseConnectionManager,
    ):
        self._connection_manager = connection_manager

    async def __call__(
        self,
        message: GetCategoriesQuery,  # noqa: ARG002
    ) -> CategoryQueryResult:
        async with self._connection_manager.session() as session:
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
