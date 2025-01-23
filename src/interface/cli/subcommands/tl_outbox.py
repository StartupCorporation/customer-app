import asyncio
from typing import Annotated

from infrastructure.di.container import Container
from infrastructure.tl_outbox.service import TransactionalOutboxService
from typer import Context, Typer, Option

from interface.cli.decorator import async_command


app = Typer(
    name='tl-outbox',
)


@app.command()
@async_command
async def process(
    context: Context,
    events_count: Annotated[int, Option()],
    timeout: Annotated[int, Option()],
) -> None:
    container: Container = context.obj["container"]
    service = container[TransactionalOutboxService]

    while True:
        await asyncio.sleep(timeout)
        await service.publish_events(
            events_count=events_count,
        )
