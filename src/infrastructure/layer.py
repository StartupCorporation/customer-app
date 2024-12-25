from domain.repository.category import CategoryRepository
from domain.repository.product import ProductRepository
from infrastructure.bus.command.bus import CommandBus
from infrastructure.bus.event.bus import EventBus
from infrastructure.bus.event.middleware.event_constructor import EventConstructorMiddleware
from infrastructure.bus.event.repository import EventHandlerRepository
from infrastructure.bus.middleware.transaction import TransactionMiddleware
from infrastructure.bus.query.bus import QueryBus
from infrastructure.database.relational.connection import SQLDatabaseConnectionManager
from infrastructure.database.relational.mapper import DatabaseToEntityMapper
from infrastructure.database.relational.transaction import SQLDatabaseTransactionManager
from infrastructure.di.container import Container
from infrastructure.di.layer import Layer
from infrastructure.database.relational.repository.category import SQLAlchemyCategoryRepository
from infrastructure.database.relational.repository.product import SQLAlchemyProductRepository
from infrastructure.message_broker.base.manager import MessageBrokerManager
from infrastructure.message_broker.rabbitmq.connection import RabbitMQConnectionManager
from infrastructure.message_broker.rabbitmq.manager import RabbitMQManager
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

        container[EventHandlerRepository] = EventHandlerRepository()

        container[TransactionMiddleware] = TransactionMiddleware(
            transaction_manager=container[SQLDatabaseTransactionManager],
        )
        container[EventConstructorMiddleware] = EventConstructorMiddleware(
            event_handler_repository=container[EventHandlerRepository],
        )

        container[CommandBus] = CommandBus(
            middlewares=(
                container[TransactionMiddleware],
            ),
        )
        container[QueryBus] = QueryBus()
        container[EventBus] = EventBus(
            event_handler_repository=container[EventHandlerRepository],
            middlewares=(
                container[EventConstructorMiddleware],
                container[TransactionMiddleware],
            ),
        )

        container[CategoryRepository] = SQLAlchemyCategoryRepository(
            connection_manager=container[SQLDatabaseConnectionManager],
        )
        container[ProductRepository] = SQLAlchemyProductRepository(
            connection_manager=container[SQLDatabaseConnectionManager],
        )

        container[DatabaseToEntityMapper] = DatabaseToEntityMapper()

        container[RabbitMQConnectionManager] = RabbitMQConnectionManager(
            settings=container[RabbitMQSettings],
        )
        container[MessageBrokerManager] = RabbitMQManager(
            connection_manager=container[RabbitMQConnectionManager],
        )

        self._run_entity_to_database_mapping(
            mapper=container[DatabaseToEntityMapper],
        )

    @staticmethod
    def _run_entity_to_database_mapping(mapper: DatabaseToEntityMapper):
        mapper.map()
