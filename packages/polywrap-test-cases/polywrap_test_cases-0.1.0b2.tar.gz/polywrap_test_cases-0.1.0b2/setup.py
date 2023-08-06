# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['polywrap_test_cases']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'polywrap-test-cases',
    'version': '0.1.0b2',
    'description': 'Plugin package',
    'long_description': '# polywrap-test-cases\n\nThis package allows fetching wrap test-cases from the wrap-test-harness.\n',
    'author': 'Cesar',
    'author_email': 'cesar@polywrap.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
