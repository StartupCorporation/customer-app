import json

from infrastructure.bus.event.repository import IntegrationEventRepository
from infrastructure.database.base.transaction import DatabaseTransactionManager
from infrastructure.message_broker.base.manager import MessageBrokerPublisher
from infrastructure.tl_outbox.repository import TransactionalOutboxRepository


class TransactionalOutboxService:

    def __init__(
        self,
        transactional_outbox_repository: TransactionalOutboxRepository,
        message_broker_publisher: MessageBrokerPublisher,
        integration_event_repository: IntegrationEventRepository,
        transaction_manager: DatabaseTransactionManager,
    ):
        self._transactional_outbox_repository = transactional_outbox_repository
        self._message_broker_publisher = message_broker_publisher
        self._integration_event_repository = integration_event_repository
        self._transaction_manager = transaction_manager

    async def publish_events(self) -> None:
        async with self._transaction_manager.begin():
            events = await self._transactional_outbox_repository.get_unpublished_events()

            for event in events:
                for destination in self._integration_event_repository.get_event_destinations(
                    event=event.__class__,
                ):
                    await self._message_broker_publisher.publish(
                        message=json.dumps(event).encode(),
                        destination=destination,
                    )

            await self._transactional_outbox_repository.delete_by_ids((event.event_id for event in events))