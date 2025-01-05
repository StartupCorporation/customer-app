from application.commands.ask_quick_order.command import AskForQuickOrderCommand
from domain.service.quick_order import QuickOrderService
from domain.value_object.quick_order import QuickOrder, QuickOrderCustomer
from infrastructure.bus.command.handler import CommandHandler


class AskForQuickOrderCommandHandler(CommandHandler):

    def __init__(
        self,
        quick_order_service: QuickOrderService,
    ):
        self._quick_order_service = quick_order_service

    async def __call__(
        self,
        message: AskForQuickOrderCommand,
    ) -> None:
        await self._quick_order_service.ask_for_quick_order(
            quick_order=QuickOrder(
                customer=QuickOrderCustomer(
                    name=message.customer.name,
                    phone=message.customer.phone,
                    email=message.customer.email,
                ),
                comment=message.comment,
                contact_me=message.contact_me,
            ),
        )
