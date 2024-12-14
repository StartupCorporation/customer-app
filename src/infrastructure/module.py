from domain import CategoryRepository, ProductRepository
from infrastructure import (
    Module, Container, ApplicationSettings, DatabaseSettings, SQLAlchemyCategoryRepository,
    SQLAlchemyProductRepository,
)


class InfrastructureModule(Module):

    def setup(
        self,
        container: Container,
    ) -> None:
        container[ApplicationSettings] = ApplicationSettings()
        container[DatabaseSettings] = DatabaseSettings()
        container[CategoryRepository] = SQLAlchemyCategoryRepository()
        container[ProductRepository] = SQLAlchemyProductRepository()
