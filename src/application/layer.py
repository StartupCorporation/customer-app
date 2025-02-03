from application.commands.ask_for_callback_request.command import AskForCallbackRequestCommand
from application.commands.ask_for_callback_request.handler import AskForCallbackRequestCommandHandler
from application.commands.delete_category.command import DeleteCategoryCommand
from application.commands.delete_category.handler import DeleteCategoryCommandHandler
from application.commands.delete_product.command import DeleteProductCommand
from application.commands.delete_product.handler import DeleteProductCommandHandler
from application.commands.save_category.command import SaveCategoryCommand
from application.commands.save_category.handler import SaveCategoryCommandHandler
from application.commands.save_product.command import SaveProductCommand
from application.commands.save_product.handler import SaveProductCommandHandler
from application.queries.get_products.handler import GetProductsQueryHandler
from application.queries.get_products.query import GetProductsQuery
from application.queries.get_categories.handler import GetCategoriesQueryHandler
from application.queries.get_categories.query import GetCategoriesQuery
from application.queries.get_product_details.handler import GetProductDetailsQueryHandler
from application.queries.get_product_details.query import GetProductDetailsQuery
from domain.repository.category import CategoryRepository
from domain.repository.product import ProductRepository
from domain.service.callback_request import CallbackRequestService
from domain.service.category import CategoryService
from domain.service.product import ProductService
from infrastructure.bus.command.bus import CommandBus
from infrastructure.bus.query.bus import QueryBus
from infrastructure.database.relational.connection import SQLDatabaseConnectionManager
from infrastructure.di.container import Container
from infrastructure.di.layer import Layer


class ApplicationLayer(Layer):

    def setup(self, container: Container) -> None:
        container[QueryBus].register(
            message=GetCategoriesQuery,
            handler=GetCategoriesQueryHandler(
                connection_manager=container[SQLDatabaseConnectionManager],
            ),
        )
        container[QueryBus].register(
            message=GetProductsQuery,
            handler=GetProductsQueryHandler(
                connection_manager=container[SQLDatabaseConnectionManager],
            ),
        )
        container[QueryBus].register(
            message=GetProductDetailsQuery,
            handler=GetProductDetailsQueryHandler(
                connection_manager=container[SQLDatabaseConnectionManager],
            ),
        )

        container[CommandBus].register(
            message=DeleteCategoryCommand,
            handler=DeleteCategoryCommandHandler(
                category_repository=container[CategoryRepository],
            ),
        )
        container[CommandBus].register(
            message=SaveCategoryCommand,
            handler=SaveCategoryCommandHandler(
                category_service=container[CategoryService],
            ),
        )
        container[CommandBus].register(
            message=AskForCallbackRequestCommand,
            handler=AskForCallbackRequestCommandHandler(
                callback_request_service=container[CallbackRequestService],
            ),
        )
        container[CommandBus].register(
            message=DeleteProductCommand,
            handler=DeleteProductCommandHandler(
                product_repository=container[ProductRepository],
            ),
        )
        container[CommandBus].register(
            message=SaveProductCommand,
            handler=SaveProductCommandHandler(
                product_service=container[ProductService],
            ),
        )
