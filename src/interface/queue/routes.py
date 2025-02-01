from typing import Annotated

from faststream import Context
from faststream.rabbit import RabbitRouter, RabbitQueue

from infrastructure.bus.command.bus import CommandBus
from infrastructure.di.container import Container
from interface.queue.config import config
from interface.queue.contracts.category.category_deleted import CategoryDeletedInputContract
from interface.queue.contracts.category.category_saved import CategorySavedInputContract
from interface.queue.contracts.product.product_deleted import ProductDeletedInputContract
from interface.queue.contracts.product.product_saved import ProductSavedInputContract


router = RabbitRouter()


@router.subscriber(
    queue=RabbitQueue(
        name=config.CATEGORY_QUEUE,
        passive=True,
    ),
    description="Handles events for the categories.",
)
async def handle_category_event(
    msg: CategorySavedInputContract | CategoryDeletedInputContract,
    container: Annotated[Container, Context()],
) -> None:
    await container[CommandBus].handle(msg.data.to_command())


@router.subscriber(
    queue=RabbitQueue(
        name=config.PRODUCT_QUEUE,
        passive=True,
    ),
    description="Handles events for the products.",
)
async def handle_product_event(
    msg: ProductSavedInputContract | ProductDeletedInputContract,
    container: Annotated[Container, Context()],
) -> None:
    await container[CommandBus].handle(msg.data.to_command())
