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
from audiomass.comparisions import supported_formats, comparing
from audiomass.comparisions import text_menu


def whichcraft(arg=None):
    """
    Without *arg* checks for binaries in *listing*
    and print result. Otherwise accepts one argument
    and returns result of *which*: `None` if not exist
    or its executable path-name.

    """
    if not arg:
        listing = ['ffmpeg', 'flac', 'lame', 'oggdec', 'oggenc',
                   'shntool', 'mac']
        # listing = ['sox', 'wavpack']  # this are for futures implementations
        for required in listing:
            # if which(required):
            if which(required, mode=os.F_OK | os.X_OK, path=None):
                msgcustom(f"Check for: '{required}' ..Ok")
            else:
                msgcustom(f"Check for: '{required}' ..Not Installed")
        return None

    return which(str(arg), mode=os.F_OK | os.X_OK, path=None)


def show_format_menu(indexes):
    """
    print a text menu with audio format references
    currently supported.
    """
    menu = text_menu()
    setmenu = [menu[i] for i in range(len(menu)) if i not in set(indexes)]
    for outformat in setmenu:  # realizzazione menu di output
        msgcustom(f"{outformat}")


def get_codec_data(input_format, output_select):
    """
    Return an available audio format and its codec data
    """
    try:
        selection = int(output_select)
    except ValueError:
        return None

    if selection in supported_formats():
        # get lower case str(audio format):
        output_format = supported_formats().get(selection)[1]
        codec_data = comparing(f'{input_format} > {output_format}')
    else:
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
    output_format = os.path.splitext(os.path.basename(out_file))[1]
    dirname = os.path.dirname(out_file)

    command_dict = {
        'flac': f'flac -V {bitrate} "{in_file}" -o "{out_file}"',
        'lame': f'lame --nohist {bitrate} "{in_file}" "{out_file}"',
        'lame --decode': f'lame --decode "{in_file}" "{out_file}"',
        'oggenc': f'oggenc {bitrate} "{in_file}" -o "{out_file}"',
        'mac': f'mac "{in_file}" "{out_file}" {bitrate}',
        'ffmpeg': f'ffmpeg -i "{in_file}" {bitrate} "{out_file}"',
        'oggdec': f'oggdec "{in_file}" -o "{out_file}"',
        'shntool': (f'shntool conv -o {output_format.split(".")[1]} '
                    f'-O always "{in_file}" -d "{dirname}"')
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
