from invoke import task, Context

from tasks.shared import _change_to_root_dir


@task(
    pre=[_change_to_root_dir]
)
def up(
    context: Context,
) -> None:
    """
    Starts the infrastructure for the local development.
    """
    uid, gid = _get_user_group_id(context=context)
    context.run(f"export GROUP_ID={gid} && export USER_ID={uid} && docker compose -f docker-compose.local.yaml up")


@task(
    pre=[_change_to_root_dir]
)
def build(
    context: Context,
) -> None:
    """
    Builds services images for the local development.
    """
    uid, gid = _get_user_group_id(context=context)
    context.run(f"export GROUP_ID={gid} && export USER_ID={uid} && docker compose -f docker-compose.local.yaml build")


@task(
    help={
        "save_volumes": "To remove docker volumes created by the infrastructure.",
    },
    pre=[_change_to_root_dir]
)
def down(
    context: Context,
    save_volumes: bool = True,
) -> None:
    """
    Stops ande removes docker containers that were used by the local infrastructure.
    """
    uid, gid = _get_user_group_id(context=context)
    command = f"export GROUP_ID={gid} && export USER_ID={uid} && docker compose -f docker-compose.local.yaml down"
    if not save_volumes:
        command += " -v"
    context.run(command)


def _get_user_group_id(context: Context) -> tuple[str, str]:
    gid = context.run("id -g", hide=True).stdout.strip()
    uid = context.run("id -u", hide=True).stdout.strip()
    return uid, gid
