from typing import Annotated

from fastapi import APIRouter, Depends, status, Body

from infrastructure.bus.command.bus import CommandBus
from infrastructure.di.container import Container
from interface.web.dependencies.container import get_di_container
from interface.web.routes.order.contracts.input.order import QuickOrderInputContract
from interface.web.routes.order.docs.create_quick_order import CREATE_QUICK_ORDER_RESPONSES


router = APIRouter(
    prefix='/order',
    tags=['Order'],
)


@router.post(
    '/quick/',
    responses=CREATE_QUICK_ORDER_RESPONSES,
    status_code=status.HTTP_201_CREATED,
)
async def create_quick_order(
    container: Annotated[Container, Depends(get_di_container)],
    order: Annotated[QuickOrderInputContract, Body(description="Quick order information.")],
) -> None:
    """
    Creates a quick order.
    """
    await container[CommandBus].handle(
        message=order.to_command(),
    )
