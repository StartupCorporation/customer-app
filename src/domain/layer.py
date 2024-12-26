from domain.repository.category import CategoryRepository
from domain.service.category import CategoryService
from infrastructure.di.container import Container
from infrastructure.di.layer import Layer


class DomainLayer(Layer):

    def setup(
        self,
        container: Container,
    ) -> None:
        container[CategoryService] = CategoryService(
            category_repository=container[CategoryRepository],
        )
