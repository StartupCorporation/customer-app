from domain.event_bus.bus.global_ import GlobalDomainEventBus
from domain.event_bus.bus.local import LocalDomainEventBus
from domain.repository.category import CategoryRepository
from domain.service.category import CategoryService
from domain.service.quick_order import QuickOrderService
from infrastructure.di.container import Container
from infrastructure.di.layer import Layer


class DomainLayer(Layer):

    def setup(
        self,
        container: Container,
    ) -> None:
        container[LocalDomainEventBus] = LocalDomainEventBus()

        container[CategoryService] = CategoryService(
            category_repository=container[CategoryRepository],
        )
        container[QuickOrderService] = QuickOrderService(
            global_event_bus=container[GlobalDomainEventBus],
        )
