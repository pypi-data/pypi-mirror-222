# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cloudwatcher']

package_data = \
{'': ['*'], 'cloudwatcher': ['presets/*']}

install_requires = \
['boto3>=1.26.62,<1.27.0',
 'matplotlib>=3.5.1,<3.6.0',
 'pydantic>=1.10.2,<1.11.0',
 'pytz>=2022.1,<2022.2',
 'rich>=12.2.0,<12.3.0']

entry_points = \
{'console_scripts': ['cloudwatcher = cloudwatcher.__main__:main']}

setup_kwargs = {
    'name': 'cloudwatcher',
    'version': '0.2.0',
    'description': 'A tool for monitoring AWS CloudWatch metrics',
    'long_description': None,
    'author': 'Michal Stolarczyk',
    'author_email': 'stolarczyk.michal93@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
