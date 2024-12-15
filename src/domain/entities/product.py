from datetime import datetime
from typing import Annotated, NewType

from pydantic import Field, UUID4

from domain.entities.base import Entity
from domain.exception.product.invalid_image_link import InvalidImageLink


ProductID = NewType("ProductID", UUID4)
CommentID = NewType('CommentID', UUID4)


class Product(Entity[ProductID]):
    title: Annotated[str, Field(min_length=1)]
    description: Annotated[str, Field(min_length=1)]
    price: Annotated[float, Field(gt=0)]
    quantity: Annotated[int, Field(ge=0)]
    characteristic: dict
    images: list[str]

    comments: list["Comment"]

    def add_new_image(
        self,
        image_link: str,
    ) -> None:
        if not image_link:
            raise InvalidImageLink(
                "Image link cannot be zero-length."
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


class Comment(Entity[CommentID]):
    author: Annotated[str, Field(min_length=1)]
    content: Annotated[str, Field(min_length=1)]
    created_at: datetime

    product_id: ProductID
