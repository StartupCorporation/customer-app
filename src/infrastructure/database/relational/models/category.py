from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.relational.models.base import Base
from infrastructure.database.relational.models.mixins.id import IDMixin
from infrastructure.database.relational.models.product import Product


class Category(Base, IDMixin):
    __tablename__ = 'category'

    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column()
    image: Mapped[str] = mapped_column()
    external_id: Mapped[UUID] = mapped_column()

    products: Mapped[list[Product]] = relationship()
