# Customer Microservice Application

## Setup

## Development

### Commits

Commits' messages should be written using the [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) specification.

### Feature

If a feature is under development, a new branch must be created. The branch name should be named using the following convention:
* `feature/create-order`
* `feature/delete-comment`
* `feature/base-code`

As a result, the branch describes what it should do:
* **Feature** will add functionality to **create order**...
* **Feature** will add functionality to **delete order**...
* **Feature** will add **base code**...

### Branches

`main` branch:
* Contains tested and stable code.

Feature branches:
* Must be tested locally before merging into the `main`.
* The merge request has to be created to merge into `main`.
* The merge commit message must describe which feature was merged into `main`.
