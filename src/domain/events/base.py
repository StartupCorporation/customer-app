from datetime import datetime
from functools import cached_property
from uuid import uuid4

from pydantic import BaseModel, UUID4


class DomainEvent(BaseModel):

    @cached_property
    def __id__(self) -> UUID4:
        return uuid4()

    @cached_property
    def __created_at__(self) -> datetime:
        return datetime.now()
