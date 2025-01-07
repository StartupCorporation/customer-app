from typing import Annotated

from fastapi import APIRouter, Depends, status, Body

from infrastructure.bus.command.bus import CommandBus
from infrastructure.di.container import Container
from interface.web.dependencies.container import get_di_container
from interface.web.routes.callback_request.contracts.input.ask_for_callback_request import \
    AskForCallbackRequestInputContract
from interface.web.routes.callback_request.docs.ask_for_callback_request import ASK_FOR_CALLBACK_REQUEST


router = APIRouter(
    prefix='/callback_request',
    tags=['Callback Request'],
)


@router.post(
    '/',
    responses=ASK_FOR_CALLBACK_REQUEST,
    status_code=status.HTTP_201_CREATED,
)
async def ask_for_callback_request(
    container: Annotated[Container, Depends(get_di_container)],
    callback_request_info: Annotated[
        AskForCallbackRequestInputContract,
        Body(description="Information for communication with customer."),
    ],
) -> None:
    """
    Creates a callback request for client.
    """
    await container[CommandBus].handle(
        message=callback_request_info.to_command(),
    )
