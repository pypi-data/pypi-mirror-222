# desktopspy

This library contains utility functions for recording desktop activity on windows and linux

I created this for my productivity tool [Activity Monitor](https://github.com/elpachongco/activity-monitor)

## Features 
- Cross platform [windows, linux(ubuntu, X window system)]

## Functions 

### Get foreground window name, process, pid

```python3
from desktopspy.trackers import getForegroundWindow
>>> getForegroundWindow()
('New Tab`, 2500)

>>> import psutil
>>> psutil.Process(2500).name()
'chrome.exe'
```

### isUserActive

```python3
from desktopspy.trackers import isUserActive
>>> isUserActive()
True
```

## Installation

This library is now available on the python package index.

Visit the [pypi page](https://pypi.org/project/desktopspy).

```bash
pip install desktopspy
```

or with python-poetry

```bash
poetry add desktopspy
```

Please note that this software is in very early stage of development. 
