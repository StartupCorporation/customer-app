from invoke import task, Context

from tasks.shared import _change_to_root_dir, get_user_group_id


@task(
    pre=[_change_to_root_dir],
)
def run(
    context: Context,
) -> None:
    """
    Runs all existing migration files.
    """
    uid, gid = get_user_group_id(context=context)
    context.run(
        f"export GROUP_ID={gid} && export USER_ID={uid} && "
        "docker compose -f docker-compose.local.yaml restart migration-service",
        hide=True,
    )


@task(
    pre=[_change_to_root_dir],
)
def autogenerate(
    context: Context,
) -> None:
    """
    Autogenerate a new migration file.
    """
    uid, gid = get_user_group_id(context=context)
    context.run(
        f"export GROUP_ID={gid} && export USER_ID={uid} && "
        "docker compose -f docker-compose.local.yaml run migration-service "
        "sh -c 'cd infrastructure/database/relational/migrations && alembic revision --autogenerate'",
        hide=True,
    )
