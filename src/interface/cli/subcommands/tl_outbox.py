import asyncio

from infrastructure.di.container import Container
from infrastructure.tl_outbox.service import TransactionalOutboxService
from typer import Context, Typer


app = Typer()


@app.command()
async def process(
    context: Context,
    message_count: int,  # noqa: ARG001
    timeout: int,  # noqa: ARG001
) -> None:
    container: Container = context.obj["container"]
    service = container[TransactionalOutboxService]

    while True:
        await asyncio.sleep(10)
        await service.publish_events()
