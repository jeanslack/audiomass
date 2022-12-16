# -*- coding: utf-8 -*-
"""
Name:         utils.py (module)
Porpose:      All the useful functions used by the program.
Writer:       Gianluca Pernigoto <jeanlucperni@gmail.com>
Copyright:    (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
license:      GPL3
Rev:          Dec 21 2021
Code checker: flake8, pylint
"""
import subprocess
import sys
import os
from shutil import which
from audiomass.datastrings import msgdebug, msgcustom
from audiomass.comparisions import (comparing,
                                    text_menu,
                                    output_formats
                                    )


def whichcraft(arg=None):
    """
    With default ``arg=None`` checks for binaries in default
    *listing* and prints a formatted result. If ``arg`` is used
    to pass a specified binary as string argument, this function
    returns result of *which*, e.g: Returns `None` if not exist
    or its executable path-name.
    """
    if not arg:
        listing = ('ffmpeg', 'flac', 'lame', 'oggdec', 'oggenc',)
        # listing = ['sox', 'wavpack']  # this are for futures implementations
        for required in listing:
            # if which(required):
            if which(required, mode=os.F_OK | os.X_OK, path=None):
                msgcustom(f"Check for: '{required}' ..Ok")
            else:
                msgcustom(f"Check for: '{required}' ..Not Installed")
        return None

    return which(str(arg), mode=os.F_OK | os.X_OK, path=None)


def show_format_menu(indexes=None):
    """
    print a text menu with a list of audio format references
    currently supported. ``indexes`` argument is used  to
    indexing (show) specified formats. For more info, see
    ``text_menu()`` and ``input_formats()`` examples
    in comparisions module.
    """
    indexes = [] if indexes is None else indexes
    menu = text_menu()
    setmenu = [menu[i] for i in range(len(menu)) if i not in set(indexes)]

    for outformat in setmenu:
        msgcustom(f"{outformat}")


def get_codec_data(input_format, output_select):
    """
    Given a ``str(input_format)`` and an ``int(output_select)``
    returns the available audio format and its codec data. For
    more info, see ``input_formats()`` function in comparisions
    module.
    """
    try:
        selection = int(output_select)
    except ValueError:
        return None

    try:
        codec_data = comparing(f'{input_format.lower()} > '
                               f'{output_formats()[selection-1]}')
    except IndexError:
        return None

    return codec_data


def build_cmd(codec, bitrate, in_file, out_file):
    """
    Since each command associated with a type of codec appears
    to be different, the key of the 'command_dict' must be equal
    with the first value of the 'comparision.object_assignment'
    dictionary.

    This function Return a string with the command correctly formed.

    The accepted parameters are:

    - codec: key of the command_dict
    - bitrate: str('value')
    - in_file: str('/dirname/inputfilename.ext')
    - out_file: str('/dirname/outfilename.ext')

    """
    command_dict = {
        'flac': f'flac -V {bitrate} "{in_file}" -o "{out_file}"',
        'lame': f'lame --nohist {bitrate} "{in_file}" "{out_file}"',
        'lame --decode': f'lame --decode "{in_file}" "{out_file}"',
        'oggenc': f'oggenc {bitrate} "{in_file}" -o "{out_file}"',
        'oggdec': f'oggdec "{in_file}" -o "{out_file}"',
        'ffmpeg': (f'ffmpeg -i "{in_file}" -stats -hide_banner '
                   f'-map_metadata 0 {bitrate} "{out_file}"'),
                    }

    return command_dict[codec]


def run_subprocess(command):
    """
    Run command using subprocess.run
    """
    interrupted = None
    # print(command) # uncomment for debug, and comment try clause
    try:
        subprocess.run(command, check=True, shell=True)

    except subprocess.CalledProcessError as error:
        sys.exit(msgdebug(err=error))

    except KeyboardInterrupt:
        interrupted = True

    if interrupted:
        sys.exit(msgdebug(head='\n\n', warn="KeyboardInterrupt !"))
