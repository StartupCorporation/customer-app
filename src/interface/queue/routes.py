from typing import Annotated

from faststream import Context
from faststream.rabbit import RabbitRouter, RabbitQueue

from infrastructure.bus.command.bus import CommandBus
from infrastructure.di.container import Container
from interface.queue.contracts.category.input.category_deleted import CategoryDeletedInputContract
from interface.queue.contracts.category.input.category_saved import CategorySavedInputContract
from interface.queue.config import config


router = RabbitRouter()


@router.subscriber(
    queue=RabbitQueue(
        name=config.CATEGORY_QUEUE.NAME,
        durable=config.CATEGORY_QUEUE.DURABLE,
    ),
    title="handleCategoryEvent",
    description="Handles events from the customer microservice category queue.",
)
async def handle_category_event(
    msg: CategorySavedInputContract | CategoryDeletedInputContract,
    container: Annotated[Container, Context()],
) -> None:
    await container[CommandBus].handle(msg.data.to_command())
