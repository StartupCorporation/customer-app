from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.relational.models.base import Base
from infrastructure.database.relational.models.mixins.id import IDMixin


class ProductComment(Base, IDMixin):
    __tablename__ = 'product_comment'

    author: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column()
    created_at:  Mapped[datetime] = mapped_column()

    product_id: Mapped[int] = mapped_column(
        ForeignKey(
            column="product.id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    )
