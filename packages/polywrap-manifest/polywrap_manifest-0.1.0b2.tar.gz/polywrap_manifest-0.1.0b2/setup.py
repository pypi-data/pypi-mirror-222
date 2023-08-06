# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['polywrap_manifest']

package_data = \
{'': ['*']}

install_requires = \
['polywrap-msgpack>=0.1.0b2,<0.2.0', 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'polywrap-manifest',
    'version': '0.1.0b2',
    'description': 'WRAP manifest',
    'long_description': '# polywrap-manifest\n\nPython implementation of the WRAP manifest schema at https://github.com/polywrap/wrap\n\n## Usage\n\n### Deserialize WRAP manifest\n\n```python\nfrom polywrap_manifest import deserialize_wrap_manifest, WrapManifest_0_1\n\nwith open("<path to WRAP package>/wrap.info", "rb") as f:\n    raw_manifest = f.read()\n\nmanifest = deserialize_wrap_manifest(raw_manifest)\nassert isinstance(manifest, WrapManifest_0_1)\n```\n',
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
