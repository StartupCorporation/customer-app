from domain.repository.category import CategoryRepository
from domain.repository.product import ProductRepository
from infrastructure.bus.impl.command.bus import CommandBus
from infrastructure.bus.impl.event.bus import EventBus
from infrastructure.bus.impl.event.middleware.event_constructor import EventConstructorMiddleware
from infrastructure.bus.impl.event.repository import EventHandlerRepository
from infrastructure.bus.impl.query.bus import QueryBus
from infrastructure.bus.middleware.transaction import TransactionMiddleware
from infrastructure.database.relational.connection import AsyncSQLDatabaseConnectionManager
from infrastructure.database.relational.mapper import DatabaseToEntityMapper
from infrastructure.database.relational.transaction import TransactionManager
from infrastructure.di.container import Container
from infrastructure.di.layer import Layer
from infrastructure.database.relational.repository.category import SQLAlchemyCategoryRepository
from infrastructure.database.relational.repository.product import SQLAlchemyProductRepository
from infrastructure.message_broker.base.manager import MessageBrokerManager
from infrastructure.message_broker.impl.rabbitmq.connection import RabbitMQConnectionManager
from infrastructure.message_broker.impl.rabbitmq.manager import RabbitMQManager
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

        container[AsyncSQLDatabaseConnectionManager] = AsyncSQLDatabaseConnectionManager(
            settings=container[DatabaseSettings],
        )
        container[TransactionManager] = TransactionManager(
            connection_manager=container[AsyncSQLDatabaseConnectionManager],
        )

        container[EventHandlerRepository] = EventHandlerRepository()

        container[TransactionMiddleware] = TransactionMiddleware(
            transaction_manager=container[TransactionManager],
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
            connection_manager=container[AsyncSQLDatabaseConnectionManager],
        )
        container[ProductRepository] = SQLAlchemyProductRepository(
            connection_manager=container[AsyncSQLDatabaseConnectionManager],
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
