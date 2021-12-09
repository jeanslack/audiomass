# -*- coding: utf-8 -*-
"""
Name:         process_file.py (module)
Porpose:      parsing data files controls.
Writer:       Gianluca Pernigoto <jeanlucperni@gmail.com>
Copyright:    (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
license:      GPL3
Rev:          Nov. 2017, Dec 08 2021
Code checker: flake8
              pylint --ignore R0913
"""
import subprocess
import sys
import os
from audiomass.datastrings import msg_str
from audiomass.audio_formats import AudioFormats
from audiomass.comparisions import supported_formats
from audiomass.comparisions import graphic_menu
from audiomass.comparisions import build_cmd


def file_parser(input_format, path_name, path_o):
    """
    Get the input filename format and check if input format is supported;
    If input format is supported, Dispay an output menu with the options
    conversion based on input format.
    Also, get a tuple with specified command elements for process
    conversion.

    """
    msg = msg_str()
    input_selection = None
    rawmenu = graphic_menu()

    for supp in supported_formats().values():
        if input_format in supp[1:3]:
            input_selection = supp[0]
            menu = [rawmenu[i] for i in range(len(rawmenu))
                    if i not in set(supp[3])]
    if input_selection is None:
        # the file-name must be supported and match with dict keys
        sys.exit(f'\n{msg[1]} File not supported: '
                 f'"{os.path.basename(path_name)}"\n')
    print(f"\n    Available formats for encoding/decoding "
          f"'\033[32;1m{input_format.lower()}\033[0m' audio file")
    for outformat in menu:
        print(f"    {outformat}")
    output_selection = input("    Type a number corresponding to "
                             "the format and press Enter key... ")
    main = AudioFormats(input_format.lower())  # Have a ext input >
    output_format = main.output_selector(output_selection)  # get out format
    tuple_data = main.pairing_formats()  # return a tuple data of the codec
    if output_selection in ('a', 'A'):
        print('audiomass: \033[1mAbort!\033[0m')
        sys.exit()
    elif output_format is None:
        sys.exit(f"\n{msg[1]} Unknow option '{output_selection}', Abort!")
    if tuple_data == 'key_error':
        sys.exit(f"\n{msg[1]} No match available for "
                 f"'{output_selection}' option, Abort!")

    bitrate_test(tuple_data, output_format, path_name, path_o)


def bitrate_test(tuple_data, output_format, path_name, path_o):
    """
    Check if codec support bitrate for level compression.

    """
    msg = msg_str()
    dict_bitrate = tuple_data[1]  # dict of corresponding bitrate values
    graphic_bitrate = tuple_data[2]  # list with strings for graphic of choice
    contestual_text = tuple_data[3]  # 'please, select a bitrate value'
    # output_format = tuple_data[4]  # non serve, gia definito
    if dict_bitrate is None:
        bitrate = ''
    else:
        # subprocess.call(['clear'])
        print(graphic_bitrate)
        level = input(contestual_text)

        audio = AudioFormats(None)
        bitrate = audio.quality_level(dict_bitrate, level)
        valid = bitrate

        if valid is False:
            print(f"\n{msg[0]} Unknow option '{level}', ...use default\n")
            bitrate = ''

    command_builder(tuple_data,
                    bitrate,
                    output_format,
                    path_name,
                    path_o)


def command_builder(tuple_data,
                    bitrate,
                    output_format,
                    path_name,
                    path_o):
    """
    command_builder build the command, with the options,
    the paths names, etc. The 'id_codec' variable, contains the key
    (codec) for an corresponding value with command_dict.

    """
    interrupted = None
    msg = msg_str()
    id_codec = tuple_data[0]  # as lame --decodec or oggenc, etc
    stream_i = os.path.basename(path_name)  # input, es: nome-canzone.wav'
    file_name = os.path.splitext(stream_i)[0]  # only stream with no ext
    if path_o is None:  # se scrive l'output nell'input source
        path_o = os.path.dirname(path_name)  # prendo lo stesso input path
    norm = os.path.join(path_o, f'{file_name}.{output_format}'
                        )  # rendo portabili i pathnames
    if os.path.exists(norm):
        sys.exit(f"\n{msg[0]} Already exists > '{norm}'")

    command = build_cmd(id_codec, bitrate, path_name, norm)
    print(f"\n\033[36;7m {output_format} Output:\033[0m >> '{norm}'\n")

    try:
        #print(command) # uncomment for debug
        subprocess.run(command, check=True, shell=True)

    except subprocess.CalledProcessError as err:
        sys.exit(f"audiomass:\033[31;1m ERROR!\033[0m {err}")
    except KeyboardInterrupt:
        interrupted = True
    else:
        print("\n\033[37;7mDone...\033[0m\n")

    if interrupted:
        sys.exit("\n\033[37;7mKeyboardInterrupt !\033[0m\n")
