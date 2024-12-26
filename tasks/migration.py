import os
from pathlib import Path

from invoke import task, Context

from tasks.shared import _change_to_root_dir


@task(
    pre=[_change_to_root_dir],
)
def _change_to_migrations_root(ctx):
    """
    Internal pre-task to change working directory to the database migrations directory.
    """
    os.chdir(Path() / "src" / "infrastructure" / "database" / "relational" / "migrations")


@task(
    pre=[_change_to_migrations_root],
)
def run(
    context: Context,
) -> None:
    """
    Runs all existing migration files.
    """
    context.run("alembic upgrade head")


@task(
    pre=[_change_to_migrations_root],
)
def autogenerate(
    context: Context,
) -> None:
    """
    Autogenerate a new migration file.
    """
    context.run("alembic revision --autogenerate")
