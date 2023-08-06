# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['polywrap_fs_plugin', 'polywrap_fs_plugin.wrap']

package_data = \
{'': ['*']}

install_requires = \
['polywrap-core>=0.1.0b2,<0.2.0',
 'polywrap-manifest>=0.1.0b2,<0.2.0',
 'polywrap-msgpack>=0.1.0b2,<0.2.0',
 'polywrap-plugin>=0.1.0b2,<0.2.0']

setup_kwargs = {
    'name': 'polywrap-fs-plugin',
    'version': '0.1.0b2',
    'description': '',
    'long_description': '# polywrap-fs-plugin\n\nThe Filesystem plugin enables wraps running within the Polywrap client to interact with the local filesystem.\n\n## Interface\n\nThe FileSystem plugin implements an existing wrap interface at `wrap://ens/wraps.eth:file-system@1.0.0`.\n\n## Usage\n\n``` python\nfrom polywrap_client import PolywrapClient\nfrom polywrap_client_config_builder import PolywrapClientConfigBuilder\nfrom polywrap_fs_plugin import file_system_plugin\n\nfs_interface_uri = Uri.from_str("wrap://ens/wraps.eth:file-system@1.0.0")\nfs_plugin_uri = Uri.from_str("plugin/file-system")\n\nconfig = (\n    PolywrapClientConfigBuilder()\n    .set_package(fs_plugin_uri, file_system_plugin())\n    .add_interface_implementations(fs_interface_uri, [fs_plugin_uri])\n    .set_redirect(fs_interface_uri, fs_plugin_uri)\n    .build()\n)\n\nclient.invoke(\n    uri=Uri.from_str("wrap://ens/wraps.eth:file-system@1.0.0"),\n    method="readFile",\n    args={\n        "path": "./file.txt"\n    }\n);\n```\n\nFor more usage examples see `src/__tests__`.\n',
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
