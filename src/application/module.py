from application.events.category_deleted.event import CategoryDeletedEvent
from application.events.category_deleted.handler import CategoryDeletedEventHandler
from application.events.category_saved.event import CategorySavedEvent
from application.events.category_saved.handler import CategorySavedEventHandler
from application.queries.get_category_products.handler import GetCategoryProductsQueryHandler
from application.queries.get_category_products.query import GetCategoryProductsQuery
from application.queries.get_categories.handler import GetCategoriesQueryHandler
from application.queries.get_categories.query import GetCategoriesQuery
from application.queries.get_product_details.handler import GetProductDetailsQueryHandler
from application.queries.get_product_details.query import GetProductDetailsQuery
from domain.repository.category import CategoryRepository
from domain.service.category import CategoryService
from infrastructure.bus.impl.event.bus import EventBus
from infrastructure.bus.impl.query.bus import QueryBus
from infrastructure.database.relational.connection import AsyncSQLDatabaseConnectionManager
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

        container[EventBus].register(
            message=CategoryDeletedEvent,
            handler=CategoryDeletedEventHandler(
                category_repository=container[CategoryRepository],
            ),
        )
        container[EventBus].register(
            message=CategorySavedEvent,
            handler=CategorySavedEventHandler(
                category_repository=container[CategoryRepository],
                category_service=container[CategoryService],
            ),
        )
