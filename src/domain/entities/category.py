from dataclasses import dataclass
from uuid import UUID

from domain.entities.base import Entity
from domain.entities.product import Product
from domain.exception.product.invalid_image_link import InvalidImageLink


@dataclass(kw_only=True)
class Category(Entity[UUID]):
    name: str
    description: str
    image: str

    products: list[Product]

    def set_new_image(
        self,
        image: str,
    ) -> None:
        if not image:
            raise InvalidImageLink(
                "Image link cannot be zero-length.",
            )

        self.image = image
