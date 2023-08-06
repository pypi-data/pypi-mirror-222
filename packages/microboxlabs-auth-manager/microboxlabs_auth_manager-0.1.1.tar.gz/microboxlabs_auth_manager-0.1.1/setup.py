# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['microboxlabs_auth_manager']

package_data = \
{'': ['*']}

install_requires = \
['pyjwt>=2.8.0,<3.0.0', 'requests>=2.31.0,<3.0.0']

setup_kwargs = {
    'name': 'microboxlabs-auth-manager',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Microboxlabs Auth Manager SDK for Python 3\n\nThis SDK provides a set of tools to interact and manage authentication with Microboxlabs services using Python 3.\n\n## Installation\n\n### Using pip:\n\nYou can install the SDK from PyPI using `pip`:\n\n```bash\npip install microboxlabs-auth-manager-sdk\n```\n\n### Using Poetry:\n\nIf you\'re using Poetry for your project, you can add it as a dependency:\n\n```bash\npoetry add microboxlabs-auth-manager-sdk\n```\n\n## Usage\n\nTo use the SDK in your Python projects:\n\n```python\nfrom microboxlabs_auth_manager import AuthToken\n\n# Initialization with your client details\nauth = AuthToken(client_id="YOUR_CLIENT_ID", \n                           client_secret="YOUR_CLIENT_SECRET", \n                           audience="https://api.microboxlabs.com/v1", \n                           grant_type="client_credentials")\n\n# Get a new access token\naccess_token = auth.get_token()\n```\n\n## Development\n\nFor development purposes, you\'ll want to clone the repository and set up using Poetry:\n\n```bash\n# Clone the repository\ngit clone https://github.com/microboxlabs/auth-manager.git\ncd auth-manager\n\n# Install the SDK dependencies for development\npoetry install\n```\n\n### Running Tests\n\nEnsure you have the development dependencies installed:\n\n```bash\n# Run tests using unittest (or your preferred testing tool)\npoetry run python -m unittest discover tests\n\n# OR if you\'re using pytest\npoetry run pytest\n```\n\n## Features\n\n- Seamless authentication with Microboxlabs services.\n- Token management: acquire, refresh, and validate tokens.\n\n## Documentation\n\nRefer to the [official documentation](https://github.com/microboxlabs/auth-manager#readme) for detailed usage and API references.\n\n## Contributing\n\nPull requests are welcome! For major changes, please open an issue first to discuss what you\'d like to change.\n\n## License\n\n[MIT](https://choosealicense.com/licenses/mit/)\n',
    'author': 'Michel David',
    'author_email': 'mdavid.cu@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
