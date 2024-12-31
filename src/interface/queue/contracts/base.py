from datetime import datetime
from typing import TypeVar, Generic

from pydantic import BaseModel, UUID4


EventType = TypeVar('EventType', bound=str)
EventData = TypeVar('EventData', bound=BaseModel)


class MessageBrokerEvent(BaseModel, Generic[EventType, EventData]):
    id: UUID4
    created_at: datetime
    event_type: EventType
    data: EventData
