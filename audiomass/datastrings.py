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


def msg_str():
    """
    All general info of the audiomass

    """
    warnings = 'audiomass: \033[33;7;3mWarning!\033[0m'
    errors = 'audiomass: \033[31;7;3mError!\033[0m'
    file_access = f"{errors} Unable to access, invalid file-name  >\033[0m"
    dir_access = f"{errors} Unable to access, Invalid dir-name  >\033[0m"

    return (warnings, errors, file_access, dir_access)
