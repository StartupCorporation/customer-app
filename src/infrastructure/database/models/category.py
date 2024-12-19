from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.models.base import Base
from infrastructure.database.models.mixins.id import IDMixin
from infrastructure.database.models.product import Product


class Category(Base, IDMixin):
    __tablename__ = 'category'

    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column()
    image: Mapped[str] = mapped_column()

    products: Mapped[list[Product]] = relationship()
