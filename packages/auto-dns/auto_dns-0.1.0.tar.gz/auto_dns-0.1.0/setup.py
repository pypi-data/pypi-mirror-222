# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['auto_dns', 'auto_dns.dns_providers']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0.1,<7.0.0', 'requests>=2.31.0,<3.0.0', 'typer>=0.9.0,<0.10.0']

entry_points = \
{'console_scripts': ['autodns = auto_dns:app']}

setup_kwargs = {
    'name': 'auto-dns',
    'version': '0.1.0',
    'description': 'A DNS Python Library.',
    'long_description': '===================\nAuto DNS Python CLI\n===================\n\nAuto DNS is a Python command line application which automatically updates the DNS records of your domain using various DNS providers.\n\nSupported DNS providers:\n\n- Arvan\n- Cloudflare\n\nThis library is intended to be used on a system with a dynamic public IP that you want to map to a static domain name.\n\nInstallation\n============\n\nThe package can be installed using pip:\n\n.. code-block:: shell\n\n   $ pip install auto-dns\n\nOr if you prefer, you can use Poetry:\n\n.. code-block:: shell\n\n   $ poetry add auto-dns\n\nConfiguration\n=============\n\nTo configure a DNS provider API key, use the following command:\n\n.. code-block:: shell\n\n   $ autodns set_api_key <provider> <api_key>\n\nUsage\n=====\n\nTo update a DNS record with your current public IP, use the following command:\n\n.. code-block:: shell\n\n   $ autodns update <domain> <record_type> <provider>\n\nContributing\n============\n\nContributions are welcome! Please feel free to submit a Pull Request.\n\nLicense\n=======\n\nAuto DNS is released under the MIT License.\n',
    'author': 'Ali Tavallaie',
    'author_email': 'a.tavallaie@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
