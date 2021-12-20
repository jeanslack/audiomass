# -*- coding: utf-8 -*-
"""
Name:         datastrings.py (module)
Porpose:      module for cosmetic output command line
Writer:       Gianluca Pernigoto <jeanlucperni@gmail.com>
Copyright:    (c) 2015/2019 Gianluca Pernigoto <jeanlucperni@gmail.com>
license:      GPL3
Rev:          nov 22 2017, Dec 15 2017, Aug 8 2019, Dec 08 2021
Code checker: flake8, pylint
"""

def msgdebug(info=None, warn=None, err=None, head='', tail=''):
    """
    print debug messages
    """
    if info:
        print(f"{head}\033[34;1mINFO:\033[0m {info}{tail}")
    if warn:
        print(f"{head}\033[33;1mWARNING:\033[0m {warn}{tail}")
    if err:
        print(f"{head}\033[31;1mERROR:\033[0m {err}{tail}")


def msgcolor(head='', tail='', orange=None, green=None, green2=None):
    """
    print informative messages
    """
    if orange:
        print(f"{head}\033[33;7m{orange}\033[0m{tail}")

    if green:
        print(f"{head}\033[32;7m{green}\033[0m{tail}")

    if green2:
        print(f"{head}\033[36;7m{green2}\033[0m{tail}")


def msgend(done=None, abort=None):
    """
    """
    if done:
        print("\n\033[1m..Finished!\033[0m\n")
    if abort:
        print("\n\033[1m..Abort!\033[0m\n")


def msgcustom(message):
    """
    """
    print(message)


def msg_str():
    """
    All general info of the audiomass

    """
    warnings = 'audiomass: \033[33;1mWARNING:\033[0m'
    errors = 'audiomass: \033[31;1mERROR:\033[0m'
    file_access = f"{errors} Unable to access, invalid file-name  >\033[0m"
    dir_access = f"{errors} Unable to access, Invalid dir-name  >\033[0m"

    return (warnings, errors, file_access, dir_access)
