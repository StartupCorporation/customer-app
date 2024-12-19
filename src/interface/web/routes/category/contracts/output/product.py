import uuid
from datetime import datetime
from typing import Annotated

from pydantic import Field, UUID4

from interface.web.contracts import OutputContract


class ProductOutputContract(OutputContract):
    id: Annotated[UUID4, Field(examples=[uuid.uuid4().hex])]
    name: Annotated[str, Field(examples=["Bosch S4 60Ah 540A 12V"])]
    description: Annotated[str, Field(examples=["Car SLA accumulator."])]
    quantity: Annotated[int, Field(examples=[5])]
    price: Annotated[float, Field(examples=[3670.50])]
    characteristics: Annotated[
        dict,
        Field(
            examples=[{
                "brand": "Bosch",
                "type": "SLA",
                "voltage": "12 V",
                "amperage": "540 A",
                "made in": "Germany",
            }],
        )]
    images: Annotated[
        list[str],
        Field(
            examples=[[
                "bosch-s4-1.png",
                "bosch-s4-2.png",
                "bosch-s4-3.png",
            ]],
        ),
    ]
    comments: list["ProductCommentOutputContract"]


class ProductCommentOutputContract(OutputContract):
    author: Annotated[str, Field(examples=["Ilya"])]
    content: Annotated[str, Field(examples=["Awesome price!"])]
    created_at: datetime
