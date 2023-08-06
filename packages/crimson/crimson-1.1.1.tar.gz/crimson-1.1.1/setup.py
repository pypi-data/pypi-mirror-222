# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['crimson']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'click>=8.0,<9.0',
 'single-source>=0.2.0,<0.3.0',
 'urllib3>=1.26.16,<2.0.0']

entry_points = \
{'console_scripts': ['crimson = crimson.cli:main']}

setup_kwargs = {
    'name': 'crimson',
    'version': '1.1.1',
    'description': 'Bioinformatics tool outputs converter to JSON or YAML',
    'long_description': '# Crimson\n\n[![pypi](https://img.shields.io/pypi/v/crimson)](https://pypi.org/project/crimson)\n[![ci](https://github.com/bow/crimson/actions/workflows/ci.yml/badge.svg)](https://github.com/bow/crimson/actions?query=branch%3Amaster)\n[![coverage](https://api.codeclimate.com/v1/badges/7904a5424f60f09ebbd7/test_coverage)](https://codeclimate.com/github/bow/crimson/test_coverage)\n\n\nCrimson converts non-standard bioinformatics tool outputs to JSON or YAML.\n\nCurrently it can convert outputs of the following tools:\n\n  * [FastQC](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/>) (``fastqc``)\n  * [FusionCatcher](https://github.com/ndaniel/fusioncatcher) (``fusioncatcher``)\n  * [samtools](http://www.htslib.org/doc/samtools.html) flagstat (``flagstat``)\n  * [Picard](https://broadinstitute.github.io/picard/) metrics tools (``picard``)\n  * [STAR](https://github.com/alexdobin/STAR) log file (``star``)\n  * [STAR-Fusion](https://github.com/STAR-Fusion/STAR-Fusion) hits table (``star-fusion``)\n  * [Variant Effect Predictor](http://www.ensembl.org/info/docs/tools/vep/index.html)\n    plain text output (``vep``)\n\nFor each conversion, there are two execution options: as command line tool or as a Python\nlibrary function. The first alternative uses `crimson` as a command-line tool. The second one\nrequires importing the `crimson` library in your program.\n\n\n## Installation\n\nCrimson is available on the [Python Package Index](https://pypi.org/project/crimson/)\nand you can install it via ``pip``:\n\n```shell\n$ pip install crimson\n```\n\nIt is also available on\n[BioConda](https://bioconda.github.io/recipes/crimson/README.html), both through the\n`conda` package manager or as a\n[Docker container](https://quay.io/repository/biocontainers/crimson?tab=tags).\n\nFor Docker execution, you may also use\n[the GitHub Docker registry](https://github.com/bow/crimson/pkgs/container/crimson). This\nregistry hosts the latest version, but does not host versions 1.1.0 or earlier.\n\n```shell\ndocker pull ghcr.io/bow/crimson\n```\n\n\n## Usage\n\n### As a command line tool\n\nThe general command is `crimson {tool_name}`. By default, the output is written to\n`stdout`. For example, to use the `picard` parser, you would execute:\n\n```shell\n$ crimson picard /path/to/a/picard.metrics\n```\n\nYou can also write the output to a file by specifying a file name. The following\ncommand writes the output to a file named `converted.json`:\n\n```shell\n$ crimson picard /path/to/a/picard.metrics converted.json\n```\n\nSome parsers may accept additional input formats. The FastQC parser, for example, also\naccepts a path to a FastQC output directory as its input:\n\n\n```shell\n$ crimson fastqc /path/to/a/fastqc/dir\n```\n\nIt also accepts a path to a zipped result:\n\n```shell\n$ crimson fastqc /path/to/a/fastqc_result.zip\n```\n\nWhen in doubt, use the ``--help`` flag:\n\n```shell\n$ crimson --help            # for the general help\n$ crimson fastqc --help     # for the parser-specific help, in this case FastQC\n```\n\n### As a Python library function\n\nThe specific function to import is generally located at `crimson.{tool_name}.parser`. So to\nuse the `picard` parser in your program, you can do:\n\n```python\nfrom crimson import picard\n\n# You can specify the input file name as a string or path-like object...\nparsed = picard.parse("/path/to/a/picard.metrics")\n\n# ... or a file handle\nwith open("/path/to/a/picard.metrics") as src:\n    parsed = picard.parse(src)\n```\n\n## Why?\n\n  * Not enough tools use standard output formats.\n  * Writing and re-writing the same parsers across different scripts is not a productive\n    way to spend the day.\n\n\n## Local Development\n\nSetting up a local development requires that you set up all of the supported Python\nversions. We use [pyenv](https://github.com/pyenv/pyenv) for this.\n\n```shell\n# Clone the repository and cd into it.\n$ git clone https://github.com/bow/crimson\n$ cd crimson\n\n# Create your local development environment. This command also installs\n# all supported Python versions using `pyenv`.\n$ make env\n\n# Run the test and linter suite to verify the setup.\n$ make lint test\n\n# When in doubt, just run `make` without any arguments.\n$ make\n```\n\n\n## Contributing\n\nIf you are interested, Crimson accepts the following types contribution:\n\n  * Documentation updates / tweaks (if anything seems unclear, feel free to open an issue)\n  * Bug reports\n  * Support for tools\' outputs which can be converted to JSON or YAML\n\nFor any of these, feel free to open an issue in the [issue\ntracker](https://github.com/bow/crimson/issues>) or submit a pull request.\n\n\n## License\n\nCrimson is BSD-licensed. Refer to the ``LICENSE`` file for the full license.\n',
    'author': 'Wibowo Arindrarto',
    'author_email': 'contact@arindrarto.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bow/crimson',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
