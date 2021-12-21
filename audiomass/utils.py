# -*- coding: utf-8 -*-
"""
Name:         utils.py (module)
Porpose:      Handles the audio data files for batch conversions.
Writer:       Gianluca Pernigoto <jeanlucperni@gmail.com>
Copyright:    (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
license:      GPL3
Rev:          Dec 20 2021
Code checker: flake8, pylint
"""
import subprocess
import sys
import os
from audiomass.datastrings import msgdebug, msgcustom
from audiomass.comparisions import supported_formats, comparing
from audiomass.comparisions import text_menu


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


def build_cmd(id_codec, bitrate, path_name, norm):
    """
    Since each command associated with a type of codec appears
    to be different, the key of the 'command_dict' must match
    with the first value of the 'object_assignment' dictionary.

    This function Return a string with the command correctly formed.

    The parameters accepted are:

    - id_codec: key of the command_dict
    - bitrate: str('value')
    - path_name: str('/dirname/filename.input_format')
    - norm: str('/dirname/filename.output_format')

    """
    output_format = os.path.splitext(os.path.basename(norm))[1]
    dirname = os.path.dirname(norm)
    command_dict = {
        'flac': f'flac -V {bitrate} "{path_name}" -o "{norm}"',
        'lame': f'lame --nohist {bitrate} "{path_name}" "{norm}"',
        'lame --decode': f'lame --decode "{path_name}" "{norm}"',
        'oggenc': f'oggenc {bitrate} "{path_name}" -o "{norm}"',
        'mac': f'mac "{path_name}" "{norm}" {bitrate}',
        'ffmpeg': f'ffmpeg -i "{path_name}" {bitrate} "{norm}"',
        'oggdec': f'oggdec "{path_name}" -o "{norm}"',
        'shntool': (f'shntool conv -o {output_format.split(".")[1]} '
                    f'-O always "{path_name}" -d "{dirname}"')
                    }

    return command_dict[id_codec]


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
