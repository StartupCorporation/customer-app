import uuid
from datetime import datetime
from typing import Annotated

from pydantic import Field, UUID4

from interface.web.contracts import OutputContract


class ProductDetailsOutputContract(OutputContract):
    id: Annotated[
        UUID4,
        Field(
            description="The product `ID`",
            examples=[uuid.uuid4().hex],
        ),
    ]
    name: Annotated[
        str,
        Field(
            description="The product name",
            examples=["Bosch S4 60Ah 540A 12V"],
        ),
    ]
    description: Annotated[
        str,
        Field(
            description="The product description",
            examples=["Car SLA accumulator."],
        ),
    ]
    quantity: Annotated[
        int,
        Field(
            description="The product available quantity.",
            examples=[5],
        ),
    ]
    price: Annotated[
        float,
        Field(
            description="The product price in UAH.",
            examples=[3670.50],
        ),
    ]
    images: Annotated[
        list[str],
        Field(
            description="The list of product images.",
            examples=[[
                "bosch-s4-1.png",
                "bosch-s4-2.png",
                "bosch-s4-3.png",
            ]],
        ),
    ]
    comments: Annotated[
        list["ProductCommentOutputContract"],
        Field(
            description="Users' comments for this product.",
        ),
    ]


class ProductCommentOutputContract(OutputContract):
    author: Annotated[
        str,
        Field(
            description="Author name of the comment.",
            examples=["Ilya"],
        ),
    ]
    content: Annotated[
        str,
        Field(
            description="Text of the comment.",
            examples=["Awesome price!"],
        ),
    ]
    created_at: Annotated[
        datetime,
        Field(
            description="Date when the comment was created.",
            examples=[datetime.now()],
        ),
    ]
