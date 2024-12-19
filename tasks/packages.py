from invoke import task, Context

from tasks.shared import _change_to_root_dir


@task(
    name="compile",
    help={
        "extra": "The additional packages section to install.",
        "output_file": "The output file where compiled packages will be written.",
    },
    optional=['extra'],
    pre=[_change_to_root_dir]
)
def compile_(
    context: Context,
    extra: str | None = None,
    output_file: str = "requirements.local.txt",
) -> None:
    """
    Compiles packages from the pyproject.toml file to the output file.
    """
    args = [
        "-q",
        f"-o {output_file}",
        "--no-header",
        "--no-annotate",
        "--no-strip-extras",
        "pyproject.toml",
    ]

    if extra:
        args.insert(0, f"--extra {extra}")

    context.run(f"pip-compile {' '.join(args)}")
    context.run(f"rm -rf src/customer_app.egg-info")
    print(f"Successfully compiled packages to the '{output_file}'.")


@task(
    help={
        "file": "The file containing the packages to install.",
    },
    pre=[_change_to_root_dir]
)
def install(
    context: Context,
    file: str = "requirements.local.txt",
) -> None:
    """
    Install packages from the provided requirements file.
    """
    context.run(f"pip-sync {file} -q")
    print(f"Successfully installed packages from the '{file}'.")
