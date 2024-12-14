from datetime import datetime
from typing import NewType, Annotated

from pydantic import UUID4, Field

from domain import Entity, ProductID


CommentID = NewType('CommentID', UUID4)


class Comment(Entity[CommentID]):
    author: Annotated[str, Field(min_length=1)]
    content: Annotated[str, Field(min_length=1)]
    created_at: datetime

    product_id: ProductID
