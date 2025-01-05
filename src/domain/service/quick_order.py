from domain.event_bus.bus.global_ import GlobalDomainEventBus
from domain.value_object.quick_order import QuickOrder


class QuickOrderService:

    def __init__(
        self,
        global_event_bus: GlobalDomainEventBus,
    ):
        self._global_event_bus = global_event_bus

    async def ask_for_quick_order(
        self,
        quick_order: QuickOrder,
    ) -> None:
        for event in quick_order.flush_events():
            await self._global_event_bus.publish(
                event=event,
            )
