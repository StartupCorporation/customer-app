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

    async def publish_events(
        self,
        events_count: int,
    ) -> None:
        events = await self._transactional_outbox_repository.get_unpublished_events(
            events_count=events_count,
        )
        for event in events:
            for destination in self._integration_event_repository.get_event_destinations(
                event=event.__class__,
            ):
                await self._message_broker_publisher.publish(
                    message=json.dumps(event.serialize()).encode(),
                    destination=destination,
                )
            async with self._transaction_manager.begin():
                await self._transactional_outbox_repository.delete_by_id(
                    id_=event.__event_id__,
                )
