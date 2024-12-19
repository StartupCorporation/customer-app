import os
from pathlib import Path

from invoke import task


@task
def _change_to_root_dir(ctx):
    """
    Internal pre-task to change working directory to the root directory of the project.
    """
    os.chdir(Path(__file__).parent.parent)
