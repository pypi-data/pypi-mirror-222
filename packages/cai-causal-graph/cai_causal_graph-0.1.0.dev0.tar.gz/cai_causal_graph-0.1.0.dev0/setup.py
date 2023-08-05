# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cai_causal_graph']

package_data = \
{'': ['*']}

install_requires = \
['networkx>=3.0.0,<4.0.0', 'numpy>=1.18.0,<2.0.0', 'pandas>=1.0.0,<3.0.0']

setup_kwargs = {
    'name': 'cai-causal-graph',
    'version': '0.1.0.dev0',
    'description': 'A causal graph package.',
    'long_description': '# cai-causal-graph: A package for causal graphs\n\nLink to docs site coming imminently.\n\n![TEST](https://github.com/causalens/cai-causal-graph/workflows/MAIN-CHECKS/badge.svg?branch=main)\n![DEPENDENCIES](https://github.com/causalens/cai-causal-graph/workflows/DEPENDENCIES-CHECKS/badge.svg?branch=main) \n![RELEASE](https://github.com/causalens/cai-causal-graph/workflows/RELEASE/badge.svg) \n![POST-RELEASE](https://github.com/causalens/cai-causal-graph/workflows/POST-RELEASE/badge.svg?branch=main) \n![INTERROGATE](./docs/interrogate_badge.svg)\n[![LICENSE](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)\n\n> **Note**  \n> The current development cycle of this branch is `v0.0.x`.\n',
    'author': 'causaLens',
    'author_email': 'opensource@causalens.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://causalgraph.causalens.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.0,<3.12.0',
}


setup(**setup_kwargs)
