import uuid
from typing import Annotated

from pydantic import Field

from domain.entities.category import CategoryID
from domain.entities.product import ProductID
from interface.web.contracts import OutputContract


class CategoryOutputContract(OutputContract):
    id: Annotated[CategoryID, Field(examples=[uuid.uuid4().hex])]
    title: Annotated[str, Field(examples=["Accumulators"])]
    description: Annotated[str, Field(examples=["Accumulators are rechargeable energy storage devices."])]
    image: Annotated[str, Field(examples=["accumulator.png"])]


class CategoryProductOutputContract(OutputContract):
    id: Annotated[ProductID, Field(examples=[uuid.uuid4().hex])]
    name: Annotated[str, Field(examples=["Bosch S4 60Ah 540A 12V"])]
    images: Annotated[
        list[str],
        Field(examples=[[
            "bosch-s4-1.png",
            "bosch-s4-2.png",
            "bosch-s4-3.png",
        ]])
    ]
