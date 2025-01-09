from domain.event_bus.bus import ModelEventBus
from domain.value_object.callback_request import CallbackRequest


class CallbackRequestService:

    def __init__(
        self,
        event_bus: ModelEventBus,
    ):
        self._event_bus = event_bus

    async def ask_for_callback_request(
        self,
        callback_request: CallbackRequest,
    ) -> None:
        callback_request.ask_for_callback_request()

        for event in callback_request.flush_events():
            await self._event_bus.publish(
                event=event,
            )
