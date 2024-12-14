from typing import Annotated, NewType

from pydantic import Field, UUID4

from domain import Entity, Comment


ProductID = NewType("ProductID", UUID4)


class Product(Entity[ProductID]):
    title: Annotated[str, Field(min_length=1)]
    description: Annotated[str, Field(min_length=1)]
    price: Annotated[float, Field(gt=0)]
    quantity: Annotated[int, Field(ge=0)]
    characteristic: dict

    comments: list[Comment]

    def add_new_comment(
        self,
        comment: Comment,
    ) -> None:
        self.comments.append(comment)

    def remove_comment(
        self,
        comment: Comment,
    ) -> None:
        self.comments.remove(comment)
