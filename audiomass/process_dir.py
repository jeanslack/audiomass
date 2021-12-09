# -*- coding: utf-8 -*-
"""
Name:         getcommand.py (module)
Porpose:      parsing data directory content.
Writer:       Gianluca Pernigoto <jeanlucperni@gmail.com>
Copyright:    (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
license:      GPL3
Rev:          Nov. 2017, Dec 08 2021
Code checker: flake8,
              pylint --ignore R0913
"""
import subprocess
import glob
import sys
import os
from audiomass.datastrings import msg_str
from audiomass.audio_formats import AudioFormats
from audiomass.comparisions import supported_formats
from audiomass.comparisions import graphic_menu
from audiomass.comparisions import build_cmd


def dir_parser(path_i, path_o):
    """
    1 - Show input menu to files input format choice
    2 - Create output menu
    During output menu creation, Get a tuple with specified command
    elements

    """
    msg = msg_str()
    print('\n    Select the audio input file format in your directory:')
    for inputformat in graphic_menu():  # realizzazione menu di output
        print(f"    {inputformat}")

    input_selection = input("    Type a number corresponding to the input "
                            "format and press Enter key... ")  # stringa num.

    main = AudioFormats(None)  # not have a ext input = None

    input_format = main.input_selector(input_selection)  # ret input format str
    if input_selection in ('a', 'A'):
        print('audiomass: \033[1mAbort!\033[0m')
        sys.exit()
    elif input_format is None:
        sys.exit(f"\n{msg[1]} Unknow option '{input_selection}' "
                 f"in select input format, Abort!"
                 )
    rawmenu = graphic_menu()
    sel = [x for x in supported_formats().values()
           if input_format in x[1:3]
           ]
    menu = [rawmenu[i] for i in range(len(rawmenu))
            if i not in set(sel[0][3])
            ]
    print("\n")
    for outformat in menu:
        print(f"    {outformat}")
    output_selection = input("    Type a number corresponding to "
                             "the output format and press Enter key... ")
    output_format = main.output_selector(output_selection)
    tuple_data = main.pairing_formats()  # return a tuple data of the codec

    if output_selection in ('a', 'A'):
        print('audiomass: \033[1mAbort!\033[0m')
        sys.exit()
    elif output_format is None:
        sys.exit(f"\n{msg[1]} Unknow option '{output_selection}' "
                 f"in select output format, Abort!")
    if tuple_data == 'key_error':
        sys.exit(f"\n{msg[1]} No match available for "
                 f"'{output_selection}' option, Abort!")

    bitrate_test(tuple_data,
                 output_format,
                 path_i,
                 path_o,
                 input_format
                 )


def bitrate_test(tuple_data, output_format, path_i, path_o, input_format):
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
        print(graphic_bitrate)
        level = input(f'{contestual_text}')

        audio = AudioFormats(None)
        bitrate = audio.quality_level(dict_bitrate, level)
        valid = bitrate

        if valid is False:
            print(f"\n{msg[0]} Unknow option '{level}', ...use default\n")
            bitrate = ''

    command_builder(tuple_data,
                    bitrate,
                    output_format,
                    path_i,
                    path_o,
                    input_format
                    )


def command_builder(tuple_data, bitrate,
                    output_format, path_i,
                    path_o, input_format):
    """
    command_builder is based on construction of the paths and formats
    strings (output_format, path_in, path_o) and the 'command' variable,
    that contains the key (codec) for an corresponding values used for
    process.

    WARNING : path_i e path_o devono rappresentare solo il nome dei percorsi
    file_name = 'only stream with no ext, es: nome_canzone'
    path_name = 'complete path input: /dir/dir/filename.ext'
    stream_i = 'Nome dello stream di input, es: nome-canzone.wav'
    stream_o = 'Nome dello stream di output, es: nome-canzone.flac'
    path_i = '/home/Musica solo input dir-name'
    path_o = '/dir/dir solo output dir-name'

    """
    interrupted = None
    msg = msg_str()
    id_codec = tuple_data[0]  # as lame --decodec or oggenc, etc
    exe = 'False'
    count = 0
    for names in [input_format, input_format.upper()]:
        # itero su nomi formato upper-case e lower-case
        for path_name in glob.glob(os.path.join(path_i, f"*.{names}")):
            stream_i = os.path.basename(path_name)
            file_name = os.path.splitext(stream_i)[0]
            exe = None
            count += 1
            if path_o is None:  # se scrive l'output nell'input source
                # prendo lo stesso input path
                path_o = os.path.dirname(path_name)

            norm = os.path.join(path_o, f'{file_name}.{output_format}'
                                )  # rendo portabili i pathnames
            if os.path.exists(norm):
                print(f"\n{msg[0]} Already exists > '{norm}' >> skipping >>")
                continue

            command = build_cmd(id_codec, bitrate, path_name, norm)
            print(f"\n\033[36;7m|{str(count)}| {output_format} "
                  f"Output:\033[0m >> '{norm}'\n")
            try:
                #print(command) # uncomment for debug
                subprocess.run(command, check=True, shell=True)

            except subprocess.CalledProcessError as err:
                sys.exit(f"audiomass:\033[31;1m ERROR!\033[0m {err}")
            except KeyboardInterrupt:
                interrupted = True
                break

    if exe == 'False':
        sys.exit(f"\n{msg[1]} Missing files: No '{input_format}' "
                 f"files in '{path_i}' \n")
    if interrupted:
        sys.exit("\n\033[37;7mKeyboardInterrupt !\033[0m\n")

    print("\n\033[37;7m...Done\033[0m\n")
