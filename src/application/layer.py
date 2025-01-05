from application.commands.ask_quick_order.command import AskForQuickOrderCommand
from application.commands.ask_quick_order.handler import AskForQuickOrderCommandHandler
from application.commands.delete_category.command import DeleteCategoryCommand
from application.commands.delete_category.handler import DeleteCategoryCommandHandler
from application.commands.save_category.command import SaveCategoryCommand
from application.commands.save_category.handler import SaveCategoryCommandHandler
from application.event_subscribers.send_quick_order_to_admin import SendQuickOrderToAdmin
from application.queries.get_category_products.handler import GetCategoryProductsQueryHandler
from application.queries.get_category_products.query import GetCategoryProductsQuery
from application.queries.get_categories.handler import GetCategoriesQueryHandler
from application.queries.get_categories.query import GetCategoriesQuery
from application.queries.get_product_details.handler import GetProductDetailsQueryHandler
from application.queries.get_product_details.query import GetProductDetailsQuery
from domain.event_bus.bus.global_ import GlobalDomainEventBus
from domain.events.quick_order_created import QuickOrderCreated
from domain.repository.category import CategoryRepository
from domain.service.category import CategoryService
from domain.service.quick_order import QuickOrderService
from infrastructure.bus.command.bus import CommandBus
from infrastructure.bus.query.bus import QueryBus
from infrastructure.database.relational.connection import SQLDatabaseConnectionManager
from infrastructure.di.container import Container
from infrastructure.di.layer import Layer
from infrastructure.message_broker.base.manager import MessageBrokerPublisher
from infrastructure.settings.rabbitmq import RabbitMQSettings


class ApplicationLayer(Layer):

    def setup(self, container: Container) -> None:
        container[QueryBus].register(
            message=GetCategoriesQuery,
            handler=GetCategoriesQueryHandler(
                connection_manager=container[SQLDatabaseConnectionManager],
            ),
        )
        container[QueryBus].register(
            message=GetCategoryProductsQuery,
            handler=GetCategoryProductsQueryHandler(
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
            message=AskForQuickOrderCommand,
            handler=AskForQuickOrderCommandHandler(
                quick_order_service=container[QuickOrderService],
            ),
        )

        container[GlobalDomainEventBus].register(
            event=QuickOrderCreated,
            subscriber=SendQuickOrderToAdmin(
                message_broker_publisher=container[MessageBrokerPublisher],
                order_queue_config=container[RabbitMQSettings].ORDER_QUEUE,
            ),
        )
