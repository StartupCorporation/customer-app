from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from domain.entities.base import Entity
from domain.exception.product.invalid_image_link import InvalidImageLink


@dataclass(kw_only=True)
class Product(Entity[UUID]):
    name: str
    description: str
    price: float
    quantity: int
    characteristics: dict
    images: list[str]
    external_id: UUID

    comments: list["Comment"]

    def add_new_image(
        self,
        image_link: str,
    ) -> None:
        if not image_link:
            raise InvalidImageLink(
                "Image link cannot be zero-length.",
            )

        if image_link in self.images:
            return

        self.images.append(image_link)

    def add_new_comment(
        self,
        comment: "Comment",
    ) -> None:
        self.comments.append(comment)

    def remove_comment(
        self,
        comment: "Comment",
    ) -> None:
        self.comments.remove(comment)


@dataclass(kw_only=True)
class Comment(Entity[UUID]):
    author: str
    content: str
    created_at: datetime

    product_id: UUID
