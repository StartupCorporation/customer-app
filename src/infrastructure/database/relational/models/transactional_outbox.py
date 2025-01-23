from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.relational.models.base import Base


class TransactionalOutbox(Base):
    __tablename__ = 'tl_outbox'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    payload: Mapped[dict] = mapped_column()
    name: Mapped[str] = mapped_column()
