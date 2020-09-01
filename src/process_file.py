# -*- coding: utf-8 -*-
#
#########################################################
# Name: process_file.py (module)
# Porpose: parsing data files controls.
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (Ver.0.7) Nov. 2017
# Rev.
#########################################################
import subprocess
import sys
import os
from src.datastrings import msg_str
from src.audio_formats import Audio_Formats
from src.comparisions import supported_formats
from src.comparisions import graphic_menu
from src.comparisions import build_cmd


def file_parser(input_format, path_name, path_O):
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
        sys.exit('\n%s File not supported: "%s"\n' % (msg[1],
                                                      os.path.basename(
                                                          path_name)))
    print("\n    Available formats for "
          "encoding/decoding '\033[32;1m%s\033[0m' audio "
          "file" % input_format.lower()
          )
    for outformat in menu:
        print("    %s" % (outformat))
    output_selection = input("    Type a number corresponding"
                             " format and press enter key... ")
    main = Audio_Formats(input_format.lower())  # Have a ext input >
    output_format = main.output_selector(output_selection)  # get out format
    tuple_data = main.pairing_formats()  # return a tuple data of the codec
    if output_selection == 'a' or output_selection == 'A':
        print('audiomass: \033[1mAbort!\033[0m')
        sys.exit()
    elif output_format is None:
        sys.exit("\n%s Unknow option '%s', Abort!" % (msg[1],
                                                      output_selection))
    if tuple_data == 'key_error':
        sys.exit("\n%s No match available for '%s' option, Abort!" % (
                                                            msg[1],
                                                            output_selection
                                                            ))

    bitrate_test(tuple_data, output_format, path_name, path_O)


def bitrate_test(tuple_data, output_format, path_name, path_O):
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

        a = Audio_Formats(None)
        bitrate = a.quality_level(dict_bitrate, level)
        valid = bitrate

        if valid is False:
            print("\n%s Unknow option '%s', "
                  "...use default\n" % (msg[0], level)
                  )
            bitrate = ''

    command_builder(tuple_data, bitrate, output_format, path_name, path_O)


def command_builder(tuple_data, bitrate, output_format, path_name, path_O):
    """
    command_builder build the command, with the options,
    the paths names, etc. The 'id_codec' variable, contains the key
    (codec) for an corresponding value with command_dict.

    """
    msg = msg_str()
    id_codec = tuple_data[0]  # as lame --decodec or oggenc, etc
    stream_I = os.path.basename(path_name)  # input, es: nome-canzone.wav'
    file_name = os.path.splitext(stream_I)[0]  # only stream with no ext
    if path_O is None:  # se scrive l'output nell'input source
        path_O = os.path.dirname(path_name)  # prendo lo stesso input path
    norm = os.path.join('%s' % path_O,
                        '%s.%s' % (file_name,
                                   output_format,)
                        )  # rendo portabili i pathnames
    if os.path.exists(norm):
        sys.exit("\n%s Already exists > '%s'" % (msg[0], norm))

    command = build_cmd(id_codec, bitrate, path_name, norm)
    print("\n\033[36;7m %s Output:\033[0m >> '%s'\n" % (output_format,
                                                               norm))
    try:
        # print (command)# uncomment for debug
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as err:
        sys.exit("audiomass:\033[31;1m ERROR!\033[0m %s" % (err))
    else:
        print("\n\033[37;7mDone...\033[0m\n")
