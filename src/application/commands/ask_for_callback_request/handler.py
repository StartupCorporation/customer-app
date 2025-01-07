from application.commands.ask_for_callback_request.command import AskForCallbackRequestCommand
from domain.service.callback_request import CallbackRequestService
from domain.value_object.callback_request import CallbackRequest
from infrastructure.bus.command.handler import CommandHandler


class AskForCallbackRequestCommandHandler(CommandHandler):

    def __init__(
        self,
        callback_request_service: CallbackRequestService,
    ):
        self._callback_request_service = callback_request_service

    async def __call__(
        self,
        message: AskForCallbackRequestCommand,
    ) -> None:
        callback_request = CallbackRequest.new(
            comment=message.comment,
            contact_me=message.contact_me,
            customer_name=message.customer_name,
            customer_phone=message.customer_phone,
        )
        await self._callback_request_service.ask_for_callback_request(
            callback_request=callback_request,
        )
