# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['polywrap_wasm',
 'polywrap_wasm.imports',
 'polywrap_wasm.imports.types',
 'polywrap_wasm.linker',
 'polywrap_wasm.linker.types',
 'polywrap_wasm.types']

package_data = \
{'': ['*']}

install_requires = \
['polywrap-core>=0.1.0b2,<0.2.0',
 'polywrap-manifest>=0.1.0b2,<0.2.0',
 'polywrap-msgpack>=0.1.0b2,<0.2.0',
 'wasmtime>=9.0.0,<10.0.0']

setup_kwargs = {
    'name': 'polywrap-wasm',
    'version': '0.1.0b2',
    'description': '',
    'long_description': '# polywrap-wasm\n\nPython implementation of the Wasm wrapper runtime.\n\n## Usage\n\n### Invoke Wasm Wrapper\n\n```python\nfrom typing import cast\nfrom polywrap_manifest import AnyWrapManifest\nfrom polywrap_core import FileReader, InvokerClient\nfrom polywrap_wasm import WasmWrapper\n\nfile_reader: FileReader = ... # any valid file_reader, pass NotImplemented for mocking\nwasm_module: bytes = bytes("<wrapper wasm module bytes read from file or http>")\nwrap_manifest: AnyWrapManifest = ...\nwrapper = WasmWrapper(file_reader, wasm_module, wrap_manifest)\nclient: InvokerClient = ... # any valid invoker client, mostly PolywrapClient\n\nmessage = "hey"\nargs = {"arg": message}\nresult = wrapper.invoke(\n  uri=Uri.from_str("fs/./build"),\n  method="simpleMethod",\n  args=args,\n  client=client\n)\nassert result.encoded is True\nassert msgpack_decode(cast(bytes, result.result)) == message\n```\n',
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
