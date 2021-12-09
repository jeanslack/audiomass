# -*- coding: utf-8 -*-
"""
Name:         whichcraft.py (module)
Porpose:      checks for binaries
Writer:       Gianluca Pernigoto <jeanlucperni@gmail.com>
Copyright:    (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
license:      GPL3
Rev           July.26.2020, Dec 08 2021
Code checker: flake8, pylint
"""
import os
from shutil import which


def check_dependencies(arg=None):
    """
    Without *arg* checks for binaries in *listing* and print result.
    Otherwise accepts one argument and returns result of *which*: `None`
    if not exist or its executable path-name.

    """
    if not arg:
        listing = ['ffmpeg', 'flac', 'lame', 'oggdec', 'oggenc',
                   'shntool', 'mac']
        # listing = ['sox', 'wavpack']  # this are for futures implementations
        for required in listing:
            # if which(required):
            if which(required, mode=os.F_OK | os.X_OK, path=None):
                print(f"Check for: '{required}' ..Ok")
            else:
                print(f"Check for: '{required}' ..Not Installed")
        return None

    return which(str(arg), mode=os.F_OK | os.X_OK, path=None)
