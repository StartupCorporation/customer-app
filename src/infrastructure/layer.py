from domain.event_bus.bus import ModelEventBus
from domain.events.callback_request_asked import CallbackRequestAsked
from domain.repository.category import CategoryRepository
from domain.repository.product import ProductRepository
from infrastructure.bus.command.bus import CommandBus
from infrastructure.bus.event.bus import EventBus
from infrastructure.bus.event.middleware.event_dispatcher import ModelEventDispatcherMiddleware
from infrastructure.bus.event.repository import IntegrationEventRepository
from infrastructure.bus.middleware.transaction import TransactionMiddleware
from infrastructure.bus.query.bus import QueryBus
from infrastructure.database.relational.connection import SQLDatabaseConnectionManager
from infrastructure.database.relational.mapper import DatabaseToEntityMapper
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


class InfrastructureLayer(Layer):

    def setup(
        self,
        container: Container,
    ) -> None:
        container[ApplicationSettings] = ApplicationSettings()
        container[DatabaseSettings] = DatabaseSettings()
        container[RabbitMQSettings] = RabbitMQSettings()

        container[SQLDatabaseConnectionManager] = SQLDatabaseConnectionManager(
            settings=container[DatabaseSettings],
        )
        container[SQLDatabaseTransactionManager] = SQLDatabaseTransactionManager(
            connection_manager=container[SQLDatabaseConnectionManager],
        )

        container[CategoryRepository] = SQLAlchemyCategoryRepository(
            connection_manager=container[SQLDatabaseConnectionManager],
        )
        container[ProductRepository] = SQLAlchemyProductRepository(
            connection_manager=container[SQLDatabaseConnectionManager],
        )
        container[IntegrationEventRepository] = IntegrationEventRepository()

        container[RabbitMQConnectionManager] = RabbitMQConnectionManager(
            settings=container[RabbitMQSettings],
        )
        container[MessageBrokerPublisher] = RabbitMQPublisher(
            connection_manager=container[RabbitMQConnectionManager],
        )

        container[ModelEventDispatcherMiddleware] = ModelEventDispatcherMiddleware(
            message_broker_publisher=container[MessageBrokerPublisher],
            integration_event_repository=container[IntegrationEventRepository],
        )
        container[TransactionMiddleware] = TransactionMiddleware(
            transaction_manager=container[SQLDatabaseTransactionManager],
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

        container[DatabaseToEntityMapper] = DatabaseToEntityMapper()

        self._run_entity_to_database_mapping(
            mapper=container[DatabaseToEntityMapper],
        )
        self._map_integration_events_to_destinations(
            container=container,
        )

    @staticmethod
    def _run_entity_to_database_mapping(mapper: DatabaseToEntityMapper):
        mapper.map()

    @staticmethod
    def _map_integration_events_to_destinations(container: Container):
        container[IntegrationEventRepository].add_event_destination(
            event=CallbackRequestAsked,
            destination=RabbitMQDEventDestination(
                routing_key=container[RabbitMQSettings].ADMIN_CALLBACK_REQUEST_QUEUE.NAME,
                exchange=container[RabbitMQSettings].ADMIN_CALLBACK_REQUEST_QUEUE.EXCHANGE,
            ),
        )
