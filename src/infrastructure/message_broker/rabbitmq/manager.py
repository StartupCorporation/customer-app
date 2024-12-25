from typing import AsyncIterator

from infrastructure.message_broker.base.manager import MessageBrokerManager
from infrastructure.message_broker.rabbitmq.connection import RabbitMQConnectionManager


class RabbitMQManager(MessageBrokerManager):

    def __init__(
        self,
        connection_manager: RabbitMQConnectionManager,
    ):
        self._connection_manager = connection_manager

    async def consume(
        self,
        queue_name: str,
    ) -> AsyncIterator[bytes]:
        async with self._connection_manager.connect() as channel:
            await channel.set_qos(prefetch_count=10)

            queue = await channel.declare_queue(queue_name, passive=True)

            async with queue.iterator() as queue_iter:
                async for message in queue_iter:
                    async with message.process():
                        yield message.body
