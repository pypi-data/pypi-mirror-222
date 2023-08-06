# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['polywrap_msgpack', 'polywrap_msgpack.extensions']

package_data = \
{'': ['*']}

install_requires = \
['msgpack>=1.0.4,<2.0.0']

setup_kwargs = {
    'name': 'polywrap-msgpack',
    'version': '0.1.0b2',
    'description': 'WRAP msgpack encoding',
    'long_description': '# polywrap-msgpack\n\nPython implementation of the WRAP MsgPack encoding standard.\n\n## Usage\n\n### Encoding-Decoding Native types and objects\n\n```python\nfrom polywrap_msgpack import msgpack_decode, msgpack_encode\n\ndictionary = {\n  "foo": 5,\n  "bar": [True, False],\n  "baz": {\n    "prop": "value"\n  }\n}\n\nencoded = msgpack_encode(dictionary)\ndecoded = msgpack_decode(encoded)\n\nassert dictionary == decoded\n```\n\n### Encoding-Decoding Extension types\n\n```python\nfrom polywrap_msgpack import msgpack_decode, msgpack_encode, GenericMap\n\ncounter: GenericMap[str, int] = GenericMap({\n  "a": 3,\n  "b": 2,\n  "c": 5\n})\n\nencoded = msgpack_encode(counter)\ndecoded = msgpack_decode(encoded)\n\nassert counter == decoded\n```',
    'author': 'Cesar',
    'author_email': 'cesar@polywrap.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
