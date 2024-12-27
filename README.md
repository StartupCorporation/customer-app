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
3. AsyncAPI Documentation - `localhost:8080/`

### Configuration

You can configure how the application is deployed locally via the `.env.local` file. Take a look:
```shell
## ======================================
## ==== INFRASTRUCTURE CONFIGURATION ====
## ======================================

## ==== DOCKER
export DOCKER_APPLICATION_EXPOSE_PORT=8000  # Exposed port number of the application container
export DOCKER_DATABASE_EXPOSE_PORT=6543  # Exposed port number of the database container
export DOCKER_RABBITMQ_EXPOSE_PORT=15672  # Exposed port number of the rabbitmq UI application
export DOCKER_ASYNCAPI_EXPOSE_PORT=8080  # Exposed port number of the AsyncAPI documentation page

## ==== DATABASE
export POSTGRES_USER=dev  # The user's name that will be created in the database container
export POSTGRES_PASSWORD=devdev  # The user's password in the database container
export POSTGRES_DB=database  # The database name in the database container

## ==== RABBITMQ
export RABBITMQ_DEFAULT_USER=dev  # User's name that will be created in the rabbitmq container
export RABBITMQ_DEFAULT_PASS=devdev  # User's password that will be created in the rabbitmq container
export RABBITMQ_COMMENTS_QUEUE=comments-queue  # RabbitMQ comments queue name
export RABBITMQ_PRODUCTS_QUEUE=products-queue  # RabbitMQ products queue name
export RABBITMQ_ORDERS_QUEUE=orders-queue  # RabbitMQ orders queue name
export RABBITMQ_CATEGORY_QUEUE=category-queue  # RabbitMQ category queue name

## ==== RABBITMQ SETUP
export SETUP_RABBITMQ_HOST=rabbitmq  # RabbitMQ host to connect
export SETUP_RABBITMQ_PORT=15672  # RabbitMQ port to connect
export SETUP_RABBITMQ_USERNAME=dev  # User's name to connect
export SETUP_RABBITMQ_PASSWORD=devdev  # User's password to connect

## ==== APPLICATION
export WEB_APPLICATION_PORT=8000  # What port is listening by the customer application

## ==== ASYNCAPI
export ASYNCAPI_DOCS_PORT=7000  # What port is used by AsyncAPI documentation page


## ===================================
## ==== APPLICATION CONFIGURATION ====
## ===================================

## ==== APPLICATION
export APPLICATION_DEBUG=1  # Is the application running in the debug mode
export APPLICATION_VERSION=0.0.1  # The application version
export APPLICATION_TITLE="Deye Web"  # The application title

## ==== DATABASE
export DATABASE_HOST=database  # Host to connect to the database
export DATABASE_PORT=5432  # Port number to connect to the database
export DATABASE_DATABASE=customer_app  # The database name to which application is connecting
export DATABASE_USERNAME=dev  # The database user to connect
export DATABASE_PASSWORD=devdev  # The database user's password to connect

## ==== RABBITMQ
export RABBITMQ_USERNAME=dev  # RabbitMQ User's name to connect
export RABBITMQ_PASSWORD=devdev  # RabbitMQ User's password to connect
export RABBITMQ_HOST=rabbitmq  # RabbitMQ host to connect
export RABBITMQ_PORT=5672  # RabbitMQ port to connect
```

## CLI Commands

During the development, we can utilize some CLI commands. We can run them using the `invoke` library.

### Packages

Commands in this section provide an opportunity to work with project dependencies:
```shell
$ inv packages.compile  # Compiles libraries into requirements file. The default output file is `requirements.local.txt`
$ inv packages.install  # Installs packages from the file with dependencies. The default dependency file is `requirements.local.txt`
```

### Infra

Commands in this section provide an opportunity to manage local infrastructure for the development:
```shell
$ inv infra.up  # Starts local infrastructure for the application: database, web-app, etc.
$ inv infra.down  # Stops and removes all docker containers used for the local infrastructure
$ inv infra.build  # Builds images that are described in the `docker-compose.local.yaml` file
```

### Migration
Handles logic of creating & applying database migrations files:
```shell
$ inv migration.run  # Applies migration files
$ inv migration.autogenerate  # Generates new migration file with the latest model changes
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
* Merge request must contain a link to the ticket.
