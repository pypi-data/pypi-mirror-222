# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['polywrap_ethereum_provider', 'polywrap_ethereum_provider.wrap']

package_data = \
{'': ['*']}

install_requires = \
['eth_account==0.8.0',
 'polywrap-core>=0.1.0b2,<0.2.0',
 'polywrap-manifest>=0.1.0b2,<0.2.0',
 'polywrap-msgpack>=0.1.0b2,<0.2.0',
 'polywrap-plugin>=0.1.0b2,<0.2.0',
 'web3==6.1.0']

setup_kwargs = {
    'name': 'polywrap-ethereum-provider',
    'version': '0.1.0b2',
    'description': 'Ethereum provider in python',
    'long_description': '# polywrap-ethereum-plugin\nThe Ethereum Provider plugin implements the `ethereum-provider-interface` @ [ens/wraps.eth:ethereum-provider@2.0.0](https://app.ens.domains/name/wraps.eth/details) (see [../../interface/polywrap.graphql](../../interface/polywrap.graphql)). It handles Ethereum wallet transaction signatures and sends JSON RPC requests for the Ethereum wrapper.\n\n## Usage\n### 1. Configure Client\nWhen creating your Polywrap Python client, add the ethereum wallet plugin:\n```python\nfrom polywrap_client import PolywrapClient\nfrom polywrap_ethereum_provider import ethereum_provider_plugin\n\nethereum_provider_plugin_uri = Uri.from_str("plugin/ethereum-provider")\nconnections = Connections(\n    connections={\n        "mocknet": Connection(provider, None),\n        "sepolia": Connection.from_network(KnownNetwork.sepolia, None)\n    },\n    default_network="sepolia",\n    signer=account.key if with_signer else None,  # type: ignore\n)\n\nethreum_provider_interface_uri = Uri.from_str("ens/wraps.eth:ethereum-provider@2.0.0")\n\nclient_config = (\n    PolywrapClientConfigBuilder()\n    .set_package(ethereum_provider_plugin_uri, ethereum_provider_plugin(connections=connections))\n    .add_interface_implementations(ethreum_provider_interface_uri, [ethereum_provider_plugin_uri])\n    .set_redirect(ethreum_provider_interface_uri, ethereum_provider_plugin_uri)\n    .build()\n)\nclient = PolywrapClient(client_config)\n```\n\n### 2. Invoke The Ethereum Wrapper\nInvocations to the Ethereum wrapper may trigger sub-invocations to the Ethereum Provider plugin:\n```python\nclient.invoke(\n  uri=ethreum_provider_interface_uri,\n  method="getSignerAddress",\n);\n```\n',
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
