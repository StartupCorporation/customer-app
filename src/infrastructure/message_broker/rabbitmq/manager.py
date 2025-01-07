import json

from aio_pika import Message
from aio_pika.abc import AbstractExchange, DeliveryMode

from infrastructure.message_broker.base.manager import MessageBrokerPublisher
from infrastructure.message_broker.rabbitmq.connection import RabbitMQConnectionManager


class RabbitMQPublisher(MessageBrokerPublisher):

    def __init__(
        self,
        connection_manager: RabbitMQConnectionManager,
    ):
        self._connection_manager = connection_manager

    async def publish(
        self,
        destination: str,
        message: dict,
        **kwargs,
    ) -> None:
        exchange = kwargs.get('exchange')

        async with self._connection_manager.connect() as channel:
            exchange: AbstractExchange = await channel.get_exchange(exchange)
            await exchange.publish(
                message=Message(
                    body=json.dumps(message, default=str).encode(),
                    delivery_mode=DeliveryMode.PERSISTENT,
                ),
                routing_key=destination,
            )
