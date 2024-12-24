import asyncio
from typing import Annotated

from typer import Argument, Typer, Context

from infrastructure.bus.impl.event.bus import EventBus
from infrastructure.bus.impl.event.message import RawEvent
from infrastructure.message_broker.base.manager import MessageBrokerManager


app = Typer(
    name="queue",
)


@app.command()
def consume(
    context: Context,
    queue: Annotated[str, Argument(help="Queue name to be listen.")],
) -> None:
    """
    Start listening to the provided queue and process messages from it.
    """

    async def _():
        consumer = context.obj["container"][MessageBrokerManager]
        event_bus = context.obj["container"][EventBus]

        async for raw_event in consumer.consume(queue):
            await event_bus.handle(message=RawEvent.model_validate_json(raw_event))

    asyncio.run(_())
