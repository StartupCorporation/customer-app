from domain.repository.category import CategoryRepository
from domain.repository.product import ProductRepository
from infrastructure.bus.command.bus import CommandBus
from infrastructure.bus.middleware.transaction import TransactionMiddleware
from infrastructure.bus.query.bus import QueryBus
from infrastructure.database.connection import AsyncSQLDatabaseConnectionManager
from infrastructure.database.mapper import DatabaseToEntityMapper
from infrastructure.database.transaction import TransactionManager
from infrastructure.di.container import Container
from infrastructure.di.layer import Layer
from infrastructure.repository.relational.category import SQLAlchemyCategoryRepository
from infrastructure.repository.relational.product import SQLAlchemyProductRepository
from infrastructure.settings.application import ApplicationSettings
from infrastructure.settings.database import DatabaseSettings


class InfrastructureModule(Layer):

    def setup(
        self,
        container: Container,
    ) -> None:
        container[ApplicationSettings] = ApplicationSettings()
        container[DatabaseSettings] = DatabaseSettings()

        container[AsyncSQLDatabaseConnectionManager] = AsyncSQLDatabaseConnectionManager(
            settings=container[DatabaseSettings],
        )
        container[TransactionManager] = TransactionManager(
            connection_manager=container[AsyncSQLDatabaseConnectionManager],
        )

        container[TransactionMiddleware] = TransactionMiddleware(
            transaction_manager=container[TransactionManager],
        )

        container[CommandBus] = CommandBus(
            middlewares=(
                container[TransactionMiddleware],
            ),
        )
        container[QueryBus] = QueryBus()

        container[CategoryRepository] = SQLAlchemyCategoryRepository(
            connection_manager=container[AsyncSQLDatabaseConnectionManager],
        )
        container[ProductRepository] = SQLAlchemyProductRepository(
            connection_manager=container[AsyncSQLDatabaseConnectionManager],
        )

        container[DatabaseToEntityMapper] = DatabaseToEntityMapper()

        self._run_entity_to_database_mapping(
            mapper=container[DatabaseToEntityMapper],
        )

    @staticmethod
    def _run_entity_to_database_mapping(mapper: DatabaseToEntityMapper):
        mapper.map()
