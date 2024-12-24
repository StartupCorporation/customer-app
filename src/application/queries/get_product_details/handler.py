from sqlalchemy import select

from application.exception.product_not_found import ProductNotFoundException
from application.queries.get_product_details.query import GetProductDetailsQuery
from application.queries.get_product_details.result import (
    GetProductDetailsQueryResult,
    ProductDetails,
    ProductDetailsComment,
)
from infrastructure.bus.impl.query.handler import QueryHandler
from infrastructure.database.relational.connection import AsyncSQLDatabaseConnectionManager
from infrastructure.database.relational.models.comment import ProductComment
from infrastructure.database.relational.models.product import Product


class GetProductDetailsQueryHandler(QueryHandler[GetProductDetailsQueryResult]):

    def __init__(
        self,
        connection_manager: AsyncSQLDatabaseConnectionManager,
    ):
        self._connection_manager = connection_manager

    async def __call__(
        self,
        message: GetProductDetailsQuery,
    ) -> GetProductDetailsQueryResult:
        async with self._connection_manager.connect() as session:
            product_stmt = select(
                Product.name,
                Product.description,
                Product.quantity,
                Product.price,
                Product.characteristics,
                Product.images,
            ).where(
                Product.id == message.product_id,
            )
            product = (await session.execute(product_stmt)).one_or_none()

            if not product:
                raise ProductNotFoundException(f"Product with id '{message.product_id}' is not found.")

            comments_stmt = select(
                ProductComment.created_at,
                ProductComment.author,
                ProductComment.content,
            ).where(
                ProductComment.product_id == message.product_id,
            ).order_by(
                ProductComment.created_at.desc(),
            )
            comments = await session.execute(comments_stmt)

        return ProductDetails(
            id=message.product_id,
            name=product.name,
            description=product.description,
            quantity=product.quantity,
            price=product.price,
            characteristics=product.characteristics,
            images=product.images,
            comments=[
                ProductDetailsComment(
                    author=comment.author,
                    content=comment.content,
                    created_at=comment.created_at,
                ) for comment in comments
            ],
        )
