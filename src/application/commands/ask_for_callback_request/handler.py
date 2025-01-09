from application.commands.ask_for_callback_request.command import AskForCallbackRequestCommand
from domain.service.callback_request import CallbackRequestService
from domain.value_object.callback_request import CallbackRequest
from infrastructure.bus.command.handler import CommandHandler


class AskForCallbackRequestCommandHandler(CommandHandler[AskForCallbackRequestCommand]):

    def __init__(
        self,
        callback_request_service: CallbackRequestService,
    ):
        self._callback_request_service = callback_request_service

    async def __call__(
        self,
        command: AskForCallbackRequestCommand,
    ) -> None:
        callback_request = CallbackRequest.new(
            comment=command.comment,
            message_customer=command.message_customer,
            customer_name=command.customer_name,
            customer_phone=command.customer_phone,
        )
        await self._callback_request_service.ask_for_callback_request(
            callback_request=callback_request,
        )
