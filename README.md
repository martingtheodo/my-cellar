# My Cellar

## Index

1. [Dependencies](#dependencies)
1. [Installation](#installation)
1. [Database](#database)
   1. [Migrations](#migrations)
1. [Main Command Lines](#main-command-lines)
1. [Application Structure](#application-structure)
1. [Development](#development)
1. [Swagger](#swagger)
1. [Testing](#testing)

## Dependencies

You will need [docker](https://docs.docker.com/engine/installation/), [docker-compose](https://docs.docker.com/compose/install/) (or [docker-for-mac](https://docs.docker.com/docker-for-mac/) for Mac OS X).

## Installation

First, clone the project:

Then install dependencies and check that it works

```bash
# Start Docker for Mac if you are on Mac OS X
make install    # Install the pip dependencies and the environment variables on the docker container
make start      # Run the container containing your local python server
```

If everything works, you should see the available routes at http://127.0.0.1:5044/my-cellar/routes.

The API runs locally on docker containers.

## Database

### Migrations

Whenever you need to update the db:

```bash
make db/migrate # generate a migration
vim migrations/versions/<migration_id>.py # check file + remove comment + improve file if needed
make db/upgrade # test migration by upgrading db to lastest migration
make db/downgrade # test migration by downgrading one migration
make db/upgrade # set the db to where we want
```

We do a downgrade to verify that everything works as expected and no errors are thrown.

## Main Command Lines

While developing, you will probably rely mostly on `make start`; however, there are additional commands at your disposal:

| `make <command>` | Description                                                                  |
| ---------------- | ---------------------------------------------------------------------------- |
| `install`        | Install the pip dependencies on the server's container.                      |
| `start`          | Run your local server in it's own docker container.                          |
| `daemon`         | Run your local server in it's own docker container as a daemon.              |
| `connect`        | Connect to your local server.                                                |
| `db/connect`     | Connect to your docker database.                                             |
| `db/migrate`     | Generate a database migration file using alembic, based on your model files. |
| `db/upgrade`     | Run the migrations until your database is up to date.                        |
| `db/downgrade`   | Downgrade your database by one migration.                                    |
| `test`           | Run unit tests with unittest in it's own container.                          |

## Application Structure

The application structure presented in this boilerplate is grouped primarily by file type. Please note, however, that this structure is only meant to serve as a guide, it is by no means prescriptive.

```
.
├── migrations                  # Database's migrations settings
│   └── versions                # Database's migrations versions generated by alembic
├── src                         # Application source code
│   ├── models                  # Python classes modeling the database
│   │   └── user.py             # Definition of the user model
│   ├── repositories            # Python classes allowing you to interact with your models
│   │   └── user.py             # Methods to easily handle user models
│   ├── resources               # Python classes containing the HTTP verbs of your routes
│   │   └── user.py             # Rest verbs related to the user routes
│   ├── routes                  # Routes definitions and links to their associated resources
│   │   ├── __init__.py         # Contains every blueprint of your API
│   │   ├── user.py             # The blueprint related to the user
│   │   └── routes.py           # The routes blueprints exposing your routes and HTTP verbs
│   ├── util                    # Some helpfull, non-business Python functions for your project
│   ├── config.py               # Project configuration settings
│   ├── manage.py               # Project commands
│   └── server.py               # Server configuration
└── test                        # Unit tests source code
```

## Development

To develop locally, here are your two options:

```bash
$ make start    # Create the containers containing your python server in your terminal
$ make daemon   # Create the containers containing your python server as a daemon
```

The containers will reload by themselves as your source code is changed.
You can check the logs in the `./server.log` file.

## Swagger

Your API might need a description of its routes and how to interact with them. Swagger helps you do it just fine.

## Testing

To add a unit test, simply create a `test_*.py` file anywhere in `./test/`, prefix your test classes with `Test` and your testing methods with `test_`. Unittest will run them automaticaly with the `make test` command.
