from typing import Annotated
from uuid import uuid4

from pydantic import Field, UUID4

from interface.web.contracts import OutputContract


class CategoryOutputContract(OutputContract):
    id: Annotated[UUID4, Field(examples=[uuid4().hex])]
    name: Annotated[str, Field(examples=["Accumulators"])]
    description: Annotated[str, Field(examples=["Accumulators are rechargeable energy storage devices."])]
    image: Annotated[str, Field(examples=["accumulator.png"])]


class CategoryProductOutputContract(OutputContract):
    id: Annotated[UUID4, Field(examples=[uuid4().hex])]
    name: Annotated[str, Field(examples=["Bosch S4 60Ah 540A 12V"])]
    images: Annotated[
        list[str],
        Field(examples=[[
            "bosch-s4-1.png",
            "bosch-s4-2.png",
            "bosch-s4-3.png",
        ]]),
    ]
