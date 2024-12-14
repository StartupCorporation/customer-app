from domain.repository.category import CategoryRepository
from domain.repository.product import ProductRepository
from infrastructure.di.container import Container
from infrastructure.di.module import Module
from infrastructure.repository.category import SQLAlchemyCategoryRepository
from infrastructure.repository.product import SQLAlchemyProductRepository
from infrastructure.settings.application import ApplicationSettings
from infrastructure.settings.database import DatabaseSettings


class InfrastructureModule(Module):

    def setup(
        self,
        container: Container,
    ) -> None:
        container[ApplicationSettings] = ApplicationSettings()
        container[DatabaseSettings] = DatabaseSettings()
        container[CategoryRepository] = SQLAlchemyCategoryRepository()
        container[ProductRepository] = SQLAlchemyProductRepository()
