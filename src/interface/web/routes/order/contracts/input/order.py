from typing import Annotated

from pydantic import Field

from application.commands.ask_quick_order.command import AskForQuickOrderCommand, AskForQuickOrderCommandCustomer
from interface.web.contracts import InputContract


class QuickOrderInputContract(InputContract):
    customer: "QuickOrderCustomerInputContract"
    comment: Annotated[
        str | None,
        Field(
            description="The client's comment for the quick order.",
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

    def to_command(self) -> AskForQuickOrderCommand:
        return AskForQuickOrderCommand(
            customer=self.customer.to_input(),
            comment=self.comment,
            contact_me=self.contact_me,
        )


class QuickOrderCustomerInputContract(InputContract):
    name: Annotated[
        str,
        Field(
            description="The client's name.",
            examples=["Oleh"],
        ),
    ]
    phone: Annotated[
        int,
        Field(
            description="The client's phone number.",
            examples=["380731090986"],
        ),
    ]
    email: Annotated[
        str | None,
        Field(
            description="The client's email.",
            examples=["some@email.com"],
        ),
    ]

    def to_input(self) -> AskForQuickOrderCommandCustomer:
        return AskForQuickOrderCommandCustomer(
            name=self.name,
            phone=str(self.phone),
            email=self.email,
        )
