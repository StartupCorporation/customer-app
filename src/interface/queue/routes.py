from typing import Annotated

from faststream import Context
from faststream.rabbit import RabbitRouter, RabbitQueue

from infrastructure.bus.event.bus import EventBus
from infrastructure.di.container import Container
from interface.queue.contracts.category.input.category_deleted import CategoryDeletedInputContract
from interface.queue.contracts.category.input.category_saved import CategorySavedInputContract


router = RabbitRouter()


@router.subscriber(
    queue=RabbitQueue(
        name="category-queue",
        durable=True,
    ),
    title="handleCategoryEvent",
    description="Handles events from the category queue.",
)
async def handle_category_event(
    msg: CategorySavedInputContract | CategoryDeletedInputContract,
    container: Annotated[Container, Context()],
) -> None:
    await container[EventBus].handle(msg.to_event())
