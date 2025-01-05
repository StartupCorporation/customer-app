from domain.events.quick_order_created import QuickOrderCreated
from infrastructure.bus.event.subscriber import EventSubscriber
from infrastructure.message_broker.base.manager import MessageBrokerPublisher
from infrastructure.settings.rabbitmq import QueueConfig


class SendQuickOrderToAdmin(EventSubscriber):

    def __init__(
        self,
        message_broker_publisher: MessageBrokerPublisher,
        order_queue_config: QueueConfig,
    ):
        self._message_broker_publisher = message_broker_publisher
        self._order_queue_config = order_queue_config

    async def __call__(
        self,
        event: QuickOrderCreated,
    ) -> None:
        await self._message_broker_publisher.publish(
            destination=self._order_queue_config.NAME,
            exchange=self._order_queue_config.EXCHANGE,
            message={
                "id": event.__id__,
                "created_at": event.__created_at__,
                "event_type": "ASKED_FOR_QUICK_ORDER",
                "data": event.model_dump(
                    mode='json',
                ),
            },
        )
