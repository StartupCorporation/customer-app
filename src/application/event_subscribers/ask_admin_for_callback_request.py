from domain.events.callback_request_asked import CallbackRequestAsked
from infrastructure.bus.event.subscriber import EventSubscriber
from infrastructure.message_broker.base.manager import MessageBrokerPublisher
from infrastructure.settings.rabbitmq import QueueConfig


class AskAdminForCallbackRequest(EventSubscriber):

    def __init__(
        self,
        message_broker_publisher: MessageBrokerPublisher,
        callback_request_queue_config: QueueConfig,
    ):
        self._message_broker_publisher = message_broker_publisher
        self._callback_request_queue_config = callback_request_queue_config

    async def __call__(
        self,
        event: CallbackRequestAsked,
    ) -> None:
        await self._message_broker_publisher.publish(
            destination=self._callback_request_queue_config.NAME,
            exchange=self._callback_request_queue_config.EXCHANGE,
            message={
                "id": event.__id__,
                "created_at": event.__created_at__,
                "event_type": "CALLBACK_REQUEST_ASKED",
                "data": event.model_dump(
                    mode='json',
                ),
            },
        )
