from infrastructure.database.models.base import Base
from infrastructure.database.models.comment import ProductComment
from infrastructure.database.models.mixins.id import IDMixin

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Product(Base, IDMixin):
    __tablename__ = 'product'

    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    characteristics: Mapped[dict] = mapped_column()
    quantity: Mapped[int] = mapped_column()
    price: Mapped[float] = mapped_column()
    images: Mapped[list] = mapped_column()

    category_id: Mapped[int] = mapped_column(
        ForeignKey(
            column="category.id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    )

    comments: Mapped[list[ProductComment]] = relationship()
