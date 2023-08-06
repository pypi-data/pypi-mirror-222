# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ipfabric',
 'ipfabric.diagrams',
 'ipfabric.diagrams.input_models',
 'ipfabric.diagrams.input_models.factory_defaults',
 'ipfabric.diagrams.output_models',
 'ipfabric_diagrams']

package_data = \
{'': ['*']}

install_requires = \
['ipfabric>=6.3.0', 'pydantic-extra-types>=2.0.0,<3.0.0']

extras_require = \
{':python_version < "3.9"': ['typing-extensions>=4.7.1,<5.0.0'],
 'examples': ['rich>=13.4.2,<14.0.0']}

setup_kwargs = {
    'name': 'ipfabric-diagrams',
    'version': '6.3.0',
    'description': 'Python package for interacting with IP Fabric Diagrams',
    'long_description': "# IP Fabric\n\nipfabric_diagrams is a Python module for connecting to and graphing topologies against an IP Fabric instance.\n\n## About\n\nFounded in 2015, [IP Fabric](https://ipfabric.io/) develops network infrastructure visibility and analytics solution to\nhelp enterprise network and security teams with network assurance and automation across multi-domain heterogeneous\nenvironments. From in-depth discovery, through graph visualization, to packet walks and complete network history, IP\nFabric enables to confidently replace manual tasks necessary to handle growing network complexity driven by relentless\ndigital transformation.\n\n## v6.3.1 Deprecation Notices\n\nIn `ipfabric>=v6.3.1` Python 3.7 support will be removed.  This was originally\nplanned for `v7.0.0` however to add new functionality of Pandas Dataframe we\nare required to move this forward.\n\n**Python 3.7 is now End of Life as of June 27th 2023**\n\n## v7.0.0 Deprecation Notices\n\nIn `ipfabric>=v7.0.0` the following will be deprecated:\n\n- `ipfabric_diagrams` package will move to `ipfabric.diagrams`\n- The use of `token='<TOKEN>'` or `username='<USER>', password='<PASS>'` in `IPFClient()` will be removed:\n  - Token: `IPFClient(auth='TOKEN')`\n  - User/Pass: `IPFClient(auth=('USER', 'PASS'))`\n  - `.env` file will only accept `IPF_TOKEN` or (`IPF_USERNAME` and `IPF_PASSWORD`) and not `auth`\n\n## Versioning\n\nStarting with IP Fabric version 5.0.x the python-ipfabric and python-ipfabric-diagrams will need to\nmatch your IP Fabric version.  The API's are changing and instead of `api/v1` they will now be `api/v5.0`.\n\nVersion 5.1 will have backwards compatability with version 5.0 however 6.0 will not support any 5.x versions.\nBy ensuring that your ipfabric SDK's match your IP Fabric Major Version will ensure compatibility and will continue to work.\n\n## Installation\n\n```\npip install ipfabric-diagrams\n```\n\n## Introduction\n\nThis package is used for diagramming via the API for IP Fabric v4.3.0.  \nExamples can be located under [examples](examples/) directory.\n\n## Authentication\nPlease take a look at [python-ipfabric](https://gitlab.com/ip-fabric/integrations/python-ipfabric#authentication) \nfor all authentication options.\n\n```python\nfrom ipfabric.diagrams import IPFDiagram\nipf = IPFDiagram(base_url='https://demo3.ipfabric.io/', auth='token', verify=False, timeout=15)\n```\n\n## Development\n\nIPFabric uses poetry for the python packaging module. Install poetry globally:\n\n```\npip install poetry\n```\n\nTo install a virtual environment run the following command in the root of this directory.\n\n```\npoetry install\n```\n\nTo test and build:\n\n```\npoetry run pytest\npoetry build\n```\n\nPrior to pushing changes run:\n```\npoetry run black ipfabric_diagrams ipfabric\npoetry update\n```\n",
    'author': 'Justin Jeffery',
    'author_email': 'justin.jeffery@ipfabric.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/ip-fabric/integrations/python-ipfabric-diagrams',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
