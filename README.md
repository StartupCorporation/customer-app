# Customer Microservice Application

## Setup

### Development

First of all, you have to create a virtual environment and install all necessary libraries. Follow these steps:
```shell
$ virtualenv venv -p 3.12  # Create a virtual environment
$ . venv/bin/activate  # Activate the virtual environment
$ pip install pip-tools  # Install `pip-tools` library to manage project dependencies
$ inv packages.install  # Install all necessary dependencies for the local development
```

After this, you can start developing.

### Run Application Locally

After you've completed all the prerequisites, you can start the application locally. Just run this command:
```shell
$ inv infra.up  # Starts all infrastructure locally: database, application, migration service
```

Now, you can access the application on `localhost:8000`. Here are some useful links:
1. OpenAPI Documentation - `localhost:8000/docs/`
2. Redoc Documentation - `localhost:8000/redoc/`

### Configuration

You can configure how the application is deployed locally via the `.env.local` file. Take a look:
```shell
## ======================================
## ==== INFRASTRUCTURE CONFIGURATION ====
## ======================================

## ==== DOCKER
export DOCKER_APPLICATION_EXPOSE_PORT=8000  # Exposed port number of the application container 
export DOCKER_DATABASE_EXPOSE_PORT=6543  # Exposed port number of the database container

## ==== DATABASE
export POSTGRES_USER=dev  # The user's name that will be created in the database container
export POSTGRES_PASSWORD=devdev  # The user's password in the database container
export POSTGRES_DB=database  # The database name in the database container

## ==== APPLICATION
export WEB_APPLICATION_PORT=8000  # What port is listening by the application


## ===================================
## ==== APPLICATION CONFIGURATION ====
## ===================================

## ==== APPLICATION
export APPLICATION_DEBUG=1  # Is the application running in the debug mode
export APPLICATION_VERSION=0.0.1  # The application version
export APPLICATION_DESCRIPTION="The customer microservice application."  # Application description

## ==== DATABASE
export DATABASE_HOST=database  # Host to connect to the database
export DATABASE_PORT=5432  # Port number to connect to the database
export DATABASE_DATABASE=customer_app  # The database name to which application is connecting
export DATABASE_USERNAME=dev  # The database user to connect
export DATABASE_PASSWORD=devdev  # The database user's password to connect
```

## Development Flow

### Commits

Commits' messages should be written using the [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) specification.

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
* Merge request must contain a link to the ticket.
