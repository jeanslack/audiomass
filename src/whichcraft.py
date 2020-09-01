# -*- coding: utf-8 -*-
#
#########################################################
# Name:      whichcraft.py (module)
# Porpose:   checks for binaries
# Writer:    Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
# license:   GPL3
# Version:   (Ver.0.6) Febbruary 2015
# Rev        July.26.2020
#########################################################
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
                print("Check for: '%s' ..Ok" % required)
            else:
                print("Check for: '%s' ..Not Installed" % required)
    else:
        return which(str(arg), mode=os.F_OK | os.X_OK, path=None)
