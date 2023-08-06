# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['desktopspy']

package_data = \
{'': ['*']}

install_requires = \
['psutil>=5.9.5,<6.0.0']

setup_kwargs = {
    'name': 'desktopspy',
    'version': '0.0.1',
    'description': 'Utility functions for desktop activity tracking',
    'long_description': "# desktopspy\n\nThis library contains utility functions for recording desktop activity on windows and linux\n\nI created this for my productivity tool [Activity Monitor](https://github.com/elpachongco/activity-monitor)\n\n## Features \n- Cross platform [windows, linux(ubuntu, X window system)]\n\n## Functions \n\n### Get foreground window name, process, pid\n\n```python3\nfrom desktopspy.trackers import getForegroundWindow\n>>> getForegroundWindow()\n('New Tab`, 2500)\n\n>>> import psutil\n>>> psutil.Process(2500).name()\n'chrome.exe'\n```\n\n### isUserActive\n\n```python3\nfrom desktopspy.trackers import isUserActive\n>>> isUserActive()\nTrue\n```\n\n## Installation\n\nThis library is now available on the python package index.\n\nVisit the [pypi page](https://pypi.org/project/desktopspy).\n\n```bash\npip install desktopspy\n```\n\nor with python-poetry\n\n```bash\npoetry add desktopspy\n```\n\nPlease note that this software is in very early stage of development. \n",
    'author': 'elpachongco',
    'author_email': 'earlsiachongco@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/elpachongco/desktopspy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
