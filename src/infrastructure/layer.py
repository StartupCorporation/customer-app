from domain.event_bus.bus.global_ import GlobalDomainEventBus
from domain.repository.category import CategoryRepository
from domain.repository.product import ProductRepository
from infrastructure.bus.command.bus import CommandBus
from infrastructure.bus.event.bus import EventBus
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

        container[TransactionMiddleware] = TransactionMiddleware(
            transaction_manager=container[SQLDatabaseTransactionManager],
        )

        container[QueryBus] = QueryBus()
        container[CommandBus] = CommandBus(
            middlewares=(
                container[TransactionMiddleware],
            ),
        )
        container[GlobalDomainEventBus] = EventBus(
            middlewares=(
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
        container[MessageBrokerPublisher] = RabbitMQPublisher(
            connection_manager=container[RabbitMQConnectionManager],
        )

        self._run_entity_to_database_mapping(
            mapper=container[DatabaseToEntityMapper],
        )

    @staticmethod
    def _run_entity_to_database_mapping(mapper: DatabaseToEntityMapper):
        mapper.map()
