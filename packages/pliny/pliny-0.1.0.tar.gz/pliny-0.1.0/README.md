# Pliny

Pliny is a **very** opinionated web framework and set of tools to help teams build modern web services and applications.

## Commands

### Platform commands

    pliny platform:setup

Bootstraps the local pliny development platform. Installs and runs the core platform services and developer tools. You must have Docker Desktop installed first.

    pliny platform:start

Startup the pliny platform services. You must have run `platform:setup` before.

    pliny platform:stop

Stop the pliny platform services.

    pliny platform

Show the current status of the local dev platform.

### App commands

    pliny create [app|service]

Creates the skeleton for a new app or service. An "app" is full-stack with a React front-end and Python backend. A service is just a Python backend that serves an API.

    pliny run

Runs the app or service in the current directory. By default the app frontend and backend are run together in the foreground.

## The runtime platform

The Pliny framework assumes that services run on a faily very rich runtime platform. This runtime allows us to build rich applications easily, rather than having to cobble together a service component, client library, and stitch it into our application.

The core services provided by the platform include:

    - Database
    - Message queue
    - Config and secrets store
    - Service discovery
    - Email gateway

In order to support a faithful environment for local development and testing, Pliny includes a _local dev_ version of the runtime platform. Services run in Docker on the local machine. You can use the `pliny platform` commands to setup and manage the local runtime.



