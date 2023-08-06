# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mqa']

package_data = \
{'': ['*']}

install_requires = \
['einops>=0.3.2,<0.4.0',
 'flash-attn==1.0.3.post0',
 'torch>=1.10.0,<2.0.0',
 'triton-pre-mlir @ '
 'git+https://github.com/vchiley/triton.git@triton_pre_mlir#subdirectory=python',
 'triton==2.0.0.dev20221202']

setup_kwargs = {
    'name': 'mqa',
    'version': '0.1.0',
    'description': 'Multi Query Attention package',
    'long_description': 'None',
    'author': 'kyegomez',
    'author_email': 'kyegomez@github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
