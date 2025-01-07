from typing import Annotated

from pydantic import Field

from application.commands.ask_for_callback_request.command import AskForCallbackRequestCommand
from interface.web.contracts import InputContract


class AskForCallbackRequestInputContract(InputContract):
    customer: "AskForCallbackRequestCustomerInputContract"
    comment: Annotated[
        str | None,
        Field(
            description="The client's comment for the callback request.",
            examples=["I want to order the Bosch S4 60Ah 540A 12V. Do you have it?"],
        ),
    ]
    contact_me: Annotated[
        bool,
        Field(
            description="Whether the administrator have to contact the client or not.",
            examples=[True],
        ),
    ]

    def to_command(self) -> AskForCallbackRequestCommand:
        return AskForCallbackRequestCommand(
            customer_name=self.customer.name,
            customer_phone=self.customer.phone,
            comment=self.comment,
            contact_me=self.contact_me,
        )


class AskForCallbackRequestCustomerInputContract(InputContract):
    name: Annotated[
        str,
        Field(
            description="The client's name.",
            examples=["Oleh"],
        ),
    ]
    phone: Annotated[
        str,
        Field(
            description="The client's phone number.",
            examples=["+380731111111"],
        ),
    ]
