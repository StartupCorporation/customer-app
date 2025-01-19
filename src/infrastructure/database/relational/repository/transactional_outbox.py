from typing import Iterable
from uuid import UUID

from sqlalchemy import delete, select

from domain.event_bus.event import IntegrationEvent
from infrastructure.database.relational.models.transactional_outbox import TransactionalOutbox
from infrastructure.database.relational.repository.base import SQLAlchemyRepository
from infrastructure.tl_outbox.repository import TransactionalOutboxRepository


class SQLAlchemyTransactionalOutboxRepository(SQLAlchemyRepository, TransactionalOutboxRepository):

    async def create(
        self,
        event: IntegrationEvent,
    ) -> None:
        async with self._connection_manager.session() as session:
            record = TransactionalOutbox(
                id=event.event_id,
                payload=event.serialize(),
            )
            session.add(record)

    async def delete_by_ids(
        self,
        ids: Iterable[UUID],
    ) -> None:
        async with self._connection_manager.session() as session:
            await session.execute(delete(TransactionalOutbox).where(TransactionalOutbox.id.in_(ids)))

    async def get_unpublished_events(self) -> Iterable[IntegrationEvent]:
        async with self._connection_manager.session() as session:
            return (await session.scalars(select(TransactionalOutbox))).unique().all()
