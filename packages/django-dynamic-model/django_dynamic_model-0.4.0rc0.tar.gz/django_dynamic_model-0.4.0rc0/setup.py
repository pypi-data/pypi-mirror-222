# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dynamic_models', 'dynamic_models.migrations']

package_data = \
{'': ['*']}

install_requires = \
['Django>=2.2.24']

setup_kwargs = {
    'name': 'django-dynamic-model',
    'version': '0.4.0rc0',
    'description': 'Dynamic Django models allow users to define, edit, and populate their own database schema.',
    'long_description': 'None',
    'author': 'Ryan Vinzent',
    'author_email': 'ryan.vinzent@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
