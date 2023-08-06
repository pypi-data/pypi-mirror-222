# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['polywrap_http_plugin', 'polywrap_http_plugin.wrap']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.3,<0.24.0',
 'polywrap-core>=0.1.0b2,<0.2.0',
 'polywrap-manifest>=0.1.0b2,<0.2.0',
 'polywrap-msgpack>=0.1.0b2,<0.2.0',
 'polywrap-plugin>=0.1.0b2,<0.2.0']

setup_kwargs = {
    'name': 'polywrap-http-plugin',
    'version': '0.1.0b2',
    'description': '',
    'long_description': '# polywrap-http-plugin\n\nHttp plugin currently supports two different methods `GET` and `POST`. Similar to calling axios, when defining request you need to specify a response type. Headers and query parameters may also be defined.\n\n## Response Types\n\n`TEXT` - The server will respond with text, the HTTP plugin will return the text as-is.\n\n`BINARY` - The server will respond with binary data (_bytes_), the HTTP plugin will encode as a **base64** string and return it.\n\n## GET request\n\nBelow is sample invocation of the `GET` request with custom request headers and query parameters (`urlParams`).\n\n```python\nresult = client.invoke(\n    uri="wrap://ens/http.polywrap.eth",\n    method="get",\n    args={\n        "url": "http://www.example.com/api",\n        "request": {\n            "responseType": "TEXT",\n            "urlParams": [{"key": "query", "value": "foo"}],\n            "headers": [{"key": "X-Request-Header", "value": "req-foo"}],\n        },\n    },\n)\n```\n\n## POST request\n\nBelow is sample invocation of the `POST` request with custom request headers and query parameters (`urlParams`). It is also possible to set request body as shown below.\n\n```python\nresponse = client.invoke(\n    uri="wrap://ens/http.polywrap.eth",\n    method="post",\n    args={\n        "url": "http://www.example.com/api",\n        "request": {\n            "responseType": "TEXT",\n            "urlParams": [{"key": "query", "value": "foo"}],\n            "headers": [{"key": "X-Request-Header", "value": "req-foo"}],\n            "body": "{data: \'test-request\'}",\n        }\n    }\n)\n```\n',
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
