import os

APPNAME = "Project Manager"
APPICON = "assets/Icon.ico"

DEFAULT_SETTINGS = {
    'project-dir': os.path.join(os.path.expanduser("~/Documents"), "Projects")
}

DEFAULT_TRACK = {
    'projects': [],
    'num': 0
}