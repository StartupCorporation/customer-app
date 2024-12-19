from domain.repository.category import CategoryRepository
from domain.repository.product import ProductRepository
from infrastructure.database.connection import AsyncSQLDatabaseConnection
from infrastructure.database.mapper import DatabaseToEntityMapper
from infrastructure.di.container import Container
from infrastructure.di.module import Module
from infrastructure.repository.relational.category import SQLAlchemyCategoryRepository
from infrastructure.repository.relational.product import SQLAlchemyProductRepository
from infrastructure.settings.application import ApplicationSettings
from infrastructure.settings.database import DatabaseSettings


class InfrastructureModule(Module):

    def setup(
        self,
        container: Container,
    ) -> None:
        container[ApplicationSettings] = ApplicationSettings()
        container[DatabaseSettings] = DatabaseSettings()

        container[AsyncSQLDatabaseConnection] = AsyncSQLDatabaseConnection(
            settings=container[DatabaseSettings],
        )

        container[CategoryRepository] = SQLAlchemyCategoryRepository(
            connection_manager=container[AsyncSQLDatabaseConnection],
        )
        container[ProductRepository] = SQLAlchemyProductRepository(
            connection_manager=container[AsyncSQLDatabaseConnection],
        )

        container[DatabaseToEntityMapper] = DatabaseToEntityMapper()

        self._run_entity_to_database_mapping(
            mapper=container[DatabaseToEntityMapper],
        )

    @staticmethod
    def _run_entity_to_database_mapping(mapper: DatabaseToEntityMapper):
        mapper.map()
