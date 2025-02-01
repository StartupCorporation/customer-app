from domain.event_bus.bus import ModelEventBus
from domain.events.callback_request_asked import CallbackRequestAsked
from domain.repository.category import CategoryRepository
from domain.repository.product import ProductRepository
from domain.service.callback_request import CallbackRequestService
from domain.service.category import CategoryService
from domain.service.product import ProductService
from infrastructure.bus.command.bus import CommandBus
from infrastructure.bus.event.bus import EventBus
from infrastructure.bus.event.middleware.event_dispatcher import ModelEventDispatcherMiddleware
from infrastructure.bus.event.repository import IntegrationEventRepository
from infrastructure.bus.middleware.transaction import TransactionMiddleware
from infrastructure.bus.query.bus import QueryBus
from infrastructure.database.base.transaction import DatabaseTransactionManager
from infrastructure.database.relational.connection import SQLDatabaseConnectionManager
from infrastructure.database.relational.mapper import DatabaseToEntityMapper
from infrastructure.database.relational.repository.transactional_outbox import SQLAlchemyTransactionalOutboxRepository
from infrastructure.database.relational.transaction import SQLDatabaseTransactionManager
from infrastructure.di.container import Container
from infrastructure.di.layer import Layer
from infrastructure.database.relational.repository.category import SQLAlchemyCategoryRepository
from infrastructure.database.relational.repository.product import SQLAlchemyProductRepository
from infrastructure.message_broker.base.manager import MessageBrokerPublisher
from infrastructure.message_broker.rabbitmq.connection import RabbitMQConnectionManager
from infrastructure.message_broker.rabbitmq.destination import RabbitMQDEventDestination
from infrastructure.message_broker.rabbitmq.manager import RabbitMQPublisher
from infrastructure.settings.application import ApplicationSettings
from infrastructure.settings.database import DatabaseSettings
from infrastructure.settings.rabbitmq import RabbitMQSettings
from infrastructure.tl_outbox.repository import TransactionalOutboxRepository
from infrastructure.tl_outbox.service import TransactionalOutboxService


class InfrastructureLayer(Layer):

    def setup(
        self,
        container: Container,
    ) -> None:
        container[ApplicationSettings] = ApplicationSettings()  # type: ignore
        container[DatabaseSettings] = DatabaseSettings()  # type: ignore
        container[RabbitMQSettings] = RabbitMQSettings()  # type: ignore

        container[SQLDatabaseConnectionManager] = SQLDatabaseConnectionManager(
            settings=container[DatabaseSettings],
        )
        container[DatabaseTransactionManager] = SQLDatabaseTransactionManager(
            connection_manager=container[SQLDatabaseConnectionManager],
        )

        container[CategoryRepository] = SQLAlchemyCategoryRepository(
            connection_manager=container[SQLDatabaseConnectionManager],
        )
        container[ProductRepository] = SQLAlchemyProductRepository(
            connection_manager=container[SQLDatabaseConnectionManager],
        )
        container[IntegrationEventRepository] = IntegrationEventRepository()
        container[TransactionalOutboxRepository] = SQLAlchemyTransactionalOutboxRepository(
            connection_manager=container[SQLDatabaseConnectionManager],
            integration_event_repository=container[IntegrationEventRepository],
        )

        container[RabbitMQConnectionManager] = RabbitMQConnectionManager(
            settings=container[RabbitMQSettings],
        )
        container[MessageBrokerPublisher] = RabbitMQPublisher(
            connection_manager=container[RabbitMQConnectionManager],
        )

        container[ModelEventDispatcherMiddleware] = ModelEventDispatcherMiddleware(
            transactional_outbox_repository=container[TransactionalOutboxRepository],
        )
        container[TransactionMiddleware] = TransactionMiddleware(
            transaction_manager=container[DatabaseTransactionManager],
        )
        container[TransactionalOutboxService] = TransactionalOutboxService(
            transactional_outbox_repository=container[TransactionalOutboxRepository],
            message_broker_publisher=container[MessageBrokerPublisher],
            integration_event_repository=container[IntegrationEventRepository],
            transaction_manager=container[DatabaseTransactionManager],
        )

        container[QueryBus] = QueryBus()
        container[CommandBus] = CommandBus(
            middlewares=(
                container[TransactionMiddleware],
            ),
        )
        container[ModelEventBus] = EventBus(
            middlewares=(
                container[TransactionMiddleware],
                container[ModelEventDispatcherMiddleware],
            ),
        )

        container[CallbackRequestService] = CallbackRequestService(
            event_bus=container[ModelEventBus],
        )
        container[CategoryService] = CategoryService(
            category_repository=container[CategoryRepository],
        )
        container[ProductService] = ProductService(
            category_repository=container[CategoryRepository],
            product_repository=container[ProductRepository],
        )

        container[DatabaseToEntityMapper] = DatabaseToEntityMapper()

        self._run_entity_to_database_mapping(
            mapper=container[DatabaseToEntityMapper],
        )
        self._init_integration_events(
            container=container,
        )

    @staticmethod
    def _run_entity_to_database_mapping(mapper: DatabaseToEntityMapper):
        mapper.map()

    @staticmethod
    def _init_integration_events(container: Container):
        container[IntegrationEventRepository].add_event(
            event=CallbackRequestAsked,
        )

        container[IntegrationEventRepository].add_event_destination(
            event=CallbackRequestAsked,
            destination=RabbitMQDEventDestination(
                routing_key=container[RabbitMQSettings].ADMIN_CALLBACK_REQUEST_QUEUE.NAME,
                exchange=container[RabbitMQSettings].ADMIN_CALLBACK_REQUEST_QUEUE.EXCHANGE,
            ),
        )
