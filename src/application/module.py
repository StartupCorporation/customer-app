from application.queries.get_catalog_products.handler import GetCategoryProductsQueryHandler
from application.queries.get_catalog_products.query import GetCategoryProductsQuery
from application.queries.get_catalogs.handler import GetCategoriesQueryHandler
from application.queries.get_catalogs.query import GetCategoriesQuery
from application.queries.get_product_details.handler import GetProductDetailsQueryHandler
from application.queries.get_product_details.query import GetProductDetailsQuery
from infrastructure.bus.query.bus import QueryBus
from infrastructure.database.connection import AsyncSQLDatabaseConnectionManager
from infrastructure.di.container import Container
from infrastructure.di.layer import Layer


class ApplicationModule(Layer):

    def setup(self, container: Container) -> None:
        container[QueryBus].register(
            message=GetCategoriesQuery,
            handler=GetCategoriesQueryHandler(
                connection_manager=container[AsyncSQLDatabaseConnectionManager],
            ),
        )
        container[QueryBus].register(
            message=GetCategoryProductsQuery,
            handler=GetCategoryProductsQueryHandler(
                connection_manager=container[AsyncSQLDatabaseConnectionManager],
            ),
        )
        container[QueryBus].register(
            message=GetProductDetailsQuery,
            handler=GetProductDetailsQueryHandler(
                connection_manager=container[AsyncSQLDatabaseConnectionManager],
            ),
        )
