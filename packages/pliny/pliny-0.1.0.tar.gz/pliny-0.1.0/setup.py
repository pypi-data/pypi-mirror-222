# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pliny']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.9.0,<0.10.0']

setup_kwargs = {
    'name': 'pliny',
    'version': '0.1.0',
    'description': 'Pliny web framework (under construction)',
    'long_description': '# Pliny\n\nPliny is a **very** opinionated web framework and set of tools to help teams build modern web services and applications.\n\n## Commands\n\n### Platform commands\n\n    pliny platform:setup\n\nBootstraps the local pliny development platform. Installs and runs the core platform services and developer tools. You must have Docker Desktop installed first.\n\n    pliny platform:start\n\nStartup the pliny platform services. You must have run `platform:setup` before.\n\n    pliny platform:stop\n\nStop the pliny platform services.\n\n    pliny platform\n\nShow the current status of the local dev platform.\n\n### App commands\n\n    pliny create [app|service]\n\nCreates the skeleton for a new app or service. An "app" is full-stack with a React front-end and Python backend. A service is just a Python backend that serves an API.\n\n    pliny run\n\nRuns the app or service in the current directory. By default the app frontend and backend are run together in the foreground.\n\n## The runtime platform\n\nThe Pliny framework assumes that services run on a faily very rich runtime platform. This runtime allows us to build rich applications easily, rather than having to cobble together a service component, client library, and stitch it into our application.\n\nThe core services provided by the platform include:\n\n    - Database\n    - Message queue\n    - Config and secrets store\n    - Service discovery\n    - Email gateway\n\nIn order to support a faithful environment for local development and testing, Pliny includes a _local dev_ version of the runtime platform. Services run in Docker on the local machine. You can use the `pliny platform` commands to setup and manage the local runtime.\n\n\n\n',
    'author': 'Scott Persinger',
    'author_email': 'scottpersinger@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
