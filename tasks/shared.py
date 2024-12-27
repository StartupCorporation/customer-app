import os
from pathlib import Path

from invoke import task, Context


@task
def _change_to_root_dir(ctx):
    """
    Internal pre-task to change working directory to the root directory of the project.
    """
    os.chdir(Path(__file__).parent.parent)


def get_user_group_id(context: Context) -> tuple[str, str]:
    gid = context.run("id -g", hide=True).stdout.strip()
    uid = context.run("id -u", hide=True).stdout.strip()
    return uid, gid
