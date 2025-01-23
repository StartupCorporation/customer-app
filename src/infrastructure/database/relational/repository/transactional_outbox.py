from typing import Iterable
from uuid import UUID

from infrastructure.bus.event.repository import IntegrationEventRepository
from sqlalchemy import delete, select

from domain.event_bus.event import IntegrationEvent
from infrastructure.database.relational.models.transactional_outbox import TransactionalOutbox
from infrastructure.database.relational.repository.base import SQLAlchemyRepository
from infrastructure.tl_outbox.repository import TransactionalOutboxRepository


class SQLAlchemyTransactionalOutboxRepository(SQLAlchemyRepository, TransactionalOutboxRepository):

    def __init__(
        self,
        *args,
        integration_event_repository: IntegrationEventRepository,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self._integration_event_repository = integration_event_repository

    async def create(
        self,
        event: IntegrationEvent,
    ) -> None:
        async with self._connection_manager.session() as session:
            record = TransactionalOutbox(
                id=event.__event_id__,
                payload=event.serialize(),
                name=event.__event_name__,
            )
            session.add(record)

    async def delete_by_id(
        self,
        id_: UUID,
    ) -> None:
        async with self._connection_manager.session() as session:
            await session.execute(delete(TransactionalOutbox).where(TransactionalOutbox.id == id_))

    async def get_unpublished_events(
        self,
        events_count: int,
    ) -> Iterable[IntegrationEvent]:
        async with self._connection_manager.session() as session:
            stmt = select(TransactionalOutbox).limit(events_count)
            events = (await session.scalars(stmt)).unique().all()

        unpublished_events = []
        for event in events:
            event_class = self._integration_event_repository.get_event_by_name(name=event.name)

            if event_class:
                unpublished_events.append(
                    event_class.deserialize(
                        data=event.payload,
                    ),
                )

        return unpublished_events
