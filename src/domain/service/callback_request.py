from domain.event_bus.bus.global_ import GlobalDomainEventBus
from domain.value_object.callback_request import CallbackRequest


class CallbackRequestService:

    def __init__(
        self,
        global_event_bus: GlobalDomainEventBus,
    ):
        self._global_event_bus = global_event_bus

    async def ask_for_callback_request(
        self,
        callback_request: CallbackRequest,
    ) -> None:
        callback_request.ask_for_callback_request()

        for event in callback_request.flush_events():
            await self._global_event_bus.publish(
                event=event,
            )
