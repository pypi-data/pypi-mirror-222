# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['polywrap_web3_config_bundle']

package_data = \
{'': ['*']}

install_requires = \
['polywrap-client-config-builder>=0.1.0b2,<0.2.0',
 'polywrap-core>=0.1.0b2,<0.2.0',
 'polywrap-ethereum-provider>=0.1.0b2,<0.2.0',
 'polywrap-manifest>=0.1.0b2,<0.2.0',
 'polywrap-sys-config-bundle>=0.1.0b2,<0.2.0',
 'polywrap-uri-resolvers>=0.1.0b2,<0.2.0',
 'polywrap-wasm>=0.1.0b2,<0.2.0']

setup_kwargs = {
    'name': 'polywrap-web3-config-bundle',
    'version': '0.1.0b2',
    'description': 'Polywrap System Client Config Bundle',
    'long_description': '# polywrap-web3-config-bundle',
    'author': 'Niraj',
    'author_email': 'niraj@polywrap.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
