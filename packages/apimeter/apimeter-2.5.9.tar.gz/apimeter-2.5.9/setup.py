# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['apimeter',
 'apimeter.builtin',
 'apimeter.ext',
 'apimeter.ext.har2case',
 'apimeter.ext.locusts',
 'apimeter.ext.uploader',
 'apimeter.loader',
 'apimeter.report',
 'apimeter.report.html']

package_data = \
{'': ['*'], 'apimeter.loader': ['schemas/*']}

install_requires = \
['colorama>=0.4.1,<0.5.0',
 'colorlog>=4.0.2,<5.0.0',
 'filetype>=1.0.5,<2.0.0',
 'har2case>=0.3.1,<0.4.0',
 'jinja2>=2.10.3,<3.0.0',
 'jsonpath>=0.82,<0.83',
 'jsonschema>=3.2.0,<4.0.0',
 'pyyaml>=5.1.2,<6.0.0',
 'requests-toolbelt>=0.9.1,<0.10.0',
 'requests>=2.22.0,<3.0.0',
 'sentry-sdk>=0.13.5,<0.14.0']

extras_require = \
{':python_version >= "2.7" and python_version < "2.8"': ['future>=0.18.1,<0.19.0',
                                                         'enum34>=1.1.6,<2.0.0']}

entry_points = \
{'console_scripts': ['apilocust = apimeter.ext.locusts.cli:main',
                     'apimeter = apimeter.cli:main',
                     'ate = apimeter.cli:main',
                     'hrun = apimeter.cli:main',
                     'httprunner = apimeter.cli:main',
                     'locusts = apimeter.ext.locusts.cli:main',
                     'meter = apimeter.cli:main']}

setup_kwargs = {
    'name': 'apimeter',
    'version': '2.5.9',
    'description': 'One-stop solution for HTTP(S) testing.',
    'long_description': "\n# ApiMeter\n\n*ApiMeter* is a simple & elegant, yet powerful HTTP(S) testing framework. Enjoy! ✨ 🚀 ✨\n\n## Design Philosophy\n\n- Embrace open source, stand on giants' shoulders, like [`Requests`][Requests], [`unittest`][unittest] and [`Locust`][Locust].\n- Convention over configuration.\n- Pursuit of high rewards, write once and achieve a variety of testing needs\n\n## Key Features\n\n- Inherit all powerful features of [`Requests`][Requests], just have fun to handle HTTP(S) in human way.\n- Define testcases in YAML or JSON format in concise and elegant manner.\n- Record and generate testcases with [`HAR`][HAR] support. see [`har2case`][har2case].\n- Supports `variables`/`extract`/`validate` mechanisms to create full test scenarios.\n- Supports perfect hook mechanism.\n- With `debugtalk.py` plugin, very easy to implement complex logic in testcase.\n- Testcases can be run in diverse ways, with single testcase, multiple testcases, or entire project folder.\n- Test report is concise and clear, with detailed log records.\n- With reuse of [`Locust`][Locust], you can run performance test without extra work.\n- CLI command supported, perfect combination with `CI/CD`.\n\n## Documentation\n\nApiMeter is rich documented.\n\n- [`中文用户使用手册`][user-docs-zh]\n- [`开发历程记录博客`][development-blogs]\n- [CHANGELOG](docs/CHANGELOG.md)\n\n## Usage\n```python\n# 报告支持忽略成功用例数据\napimeter xxx.yml --skip-success\n\n\n```\n\n\n[Requests]: http://docs.python-requests.org/en/master/\n[unittest]: https://docs.python.org/3/library/unittest.html\n[Locust]: http://locust.io/\n[har2case]: https://github.com/httprunner/har2case\n[user-docs-zh]: http://docs.httprunner.org/\n[development-blogs]: http://debugtalk.com/tags/httprunner/\n[HAR]: http://httparchive.org/\n[Swagger]: https://swagger.io/\n\n",
    'author': 'debugtalk',
    'author_email': 'debugtalk@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/httprunner/httprunner',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
}


setup(**setup_kwargs)
