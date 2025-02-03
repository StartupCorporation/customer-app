from typing import Annotated
from uuid import uuid4
from pydantic import UUID4, BaseModel, Field


type ProductsOutputContract = list[ProductShortInfoOutputContract]


class ProductShortInfoOutputContract(BaseModel):
    id: Annotated[
        UUID4,
        Field(
            description="The product `ID`.",
            examples=[str(uuid4())],
        ),
    ]
    category_id: Annotated[
        UUID4,
        Field(
            description="The category `ID`.",
            examples=[str(uuid4())],
        ),
    ]
    price: Annotated[
        float,
        Field(
            description="The product price.",
            examples=[50_000.55],
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
