# Customer Microservice Application

## Setup

### Development

First of all, you have to create a virtual environment and install all necessary libraries. Follow these steps:
```shell
$ virtualenv venv -p 3.12  # Creates a virtual environment
$ . venv/bin/activate  # Activates the virtual environment
$ pip install pip-tools invoke  # Installs `pip-tools` library to manage project dependencies
$ inv packages.install  # Installs all necessary dependencies for the local development
$ pre-commit install  # Installs pre-commit hooks
```

After this, you can start developing.

## CLI Commands

During the development, we can utilize some CLI commands. We can run them using the `invoke` library.

### Packages

Commands in this section provide an opportunity to work with project dependencies:
```shell
$ inv packages.compile  # Compiles libraries into requirements file. The default output file is `requirements.local.txt`
$ inv packages.install  # Installs packages from the file with dependencies. The default dependency file is `requirements.local.txt`
```

## Development Flow

### Commits

Commits' messages should be written using the [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) specification.

Conventional commits [cheatsheet](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

### Branches

`main` branch:
* Contains tested and stable code.

Feature branches should be named using the following convention:
* `feature/create-order`
* `feature/delete-comment`
* `feature/base-code`

As a result, the branch describes what it should do:
* **Feature** will add functionality to **create order**...
* **Feature** will add functionality to **delete order**...
* **Feature** will add **base code**...

### Merge Requests

Use the following rules before creating a merge request:
* Code must be tested locally.
* The merge commit message must describe which feature was merged into `main`.
* Merge request must have a description.
