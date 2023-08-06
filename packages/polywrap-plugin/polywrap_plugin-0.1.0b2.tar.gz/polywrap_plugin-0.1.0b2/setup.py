# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['polywrap_plugin']

package_data = \
{'': ['*']}

install_requires = \
['polywrap-core>=0.1.0b2,<0.2.0',
 'polywrap-manifest>=0.1.0b2,<0.2.0',
 'polywrap-msgpack>=0.1.0b2,<0.2.0']

setup_kwargs = {
    'name': 'polywrap-plugin',
    'version': '0.1.0b2',
    'description': 'Plugin package',
    'long_description': '# polywrap-plugin\n\nPython implementation of the plugin wrapper runtime.\n\n## Usage\n\n### Invoke Plugin Wrapper\n\n```python\nfrom typing import Any, Dict, List, Union, Optional\nfrom polywrap_manifest import AnyWrapManifest\nfrom polywrap_plugin import PluginModule\nfrom polywrap_core import InvokerClient, Uri, InvokerOptions, UriPackageOrWrapper, Env\n\nclass GreetingModule(PluginModule[None]):\n    def __init__(self, config: None):\n        super().__init__(config)\n\n    def greeting(self, args: Dict[str, Any], client: Invoker[UriPackageOrWrapper], env: Optional[Env] = None):\n        return f"Greetings from: {args[\'name\']}"\n\nmanifest = cast(AnyWrapManifest, {})\nwrapper = PluginWrapper(greeting_module, manifest)\nargs = {\n    "name": "Joe"\n}\nclient: InvokerClient = ...\n\nresult = await wrapper.invoke(\n    uri=Uri.from_str("ens/greeting.eth"),\n    method="greeting",\n    args=args,\n    client=client\n)\nassert result, "Greetings from: Joe"\n```\n',
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
