import uuid
from typing import Annotated
from uuid import uuid4

from pydantic import Field, UUID4

from interface.web.contracts import OutputContract


class CategoryOutputContract(OutputContract):
    id: Annotated[
        UUID4,
        Field(
            examples=[uuid.uuid4()],
            description="The category `ID` from the admin application.",
        ),
    ]
    name: Annotated[
        str,
        Field(
            examples=["Accumulator"],
            description="The category name.",
        ),
    ]
    description: Annotated[
        str,
        Field(
            examples=["Accumulators are rechargeable energy storage devices."],
            description="The category description.",
        ),
    ]
    image: Annotated[
        str,
        Field(
            examples=["accumulator.png."],
            description="The image link of the category.",
        ),
    ]


class CategoryProductOutputContract(OutputContract):
    id: Annotated[
        UUID4,
        Field(
            description="The product `ID`.",
            examples=[uuid4().hex],
        ),
    ]
    name: Annotated[
        str,
        Field(
            examples=["Bosch S4 60Ah 540A 12V"],
            description="The product name.",
        ),
    ]
    images: Annotated[
        list[str],
        Field(
            description="The product images list.",
            examples=[[
                "bosch-s4-1.png",
                "bosch-s4-2.png",
                "bosch-s4-3.png",
            ]],
        ),
    ]
