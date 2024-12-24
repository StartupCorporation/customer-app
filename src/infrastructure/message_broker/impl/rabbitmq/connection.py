from contextlib import asynccontextmanager

import aio_pika
from aio_pika.abc import AbstractRobustChannel

from infrastructure.settings.rabbitmq import RabbitMQSettings


class RabbitMQConnectionManager:

    def __init__(
        self,
        settings: RabbitMQSettings,
    ):
        self._settings = settings

    @asynccontextmanager
    async def connect(self) -> AbstractRobustChannel:
        connection = await aio_pika.connect_robust(self._settings.connection_url, timeout=5)
        async with connection:
            yield await connection.channel()
