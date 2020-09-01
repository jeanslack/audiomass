# -*- coding: utf-8 -*-
#
#########################################################
# Name: getcommand.py (module)
# Porpose: parsing the data files list for batch process.
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Rev: Nov 27 2017, Dec.15 2017, Aug.10 2019
#########################################################
import subprocess
import sys
import os
from collections import Counter
from src.datastrings import msg_str
from src.audio_formats import Audio_Formats
from src.comparisions import supported_formats
from src.comparisions import graphic_menu
from src.comparisions import build_cmd


def batch_parser(f_list, path_O):
    """
    Clean-up list contaminated by duplicate files.

    """
    msg = msg_str()
    for k, v in Counter(f_list).items():  # controllo doppioni accidentali.
        if v > 1:
            print("%s Removing following duplicates: > '%s' >" % (msg[0], k))
    f_list = list(set(f_list))  # removal of any duplicates in the list
    sorting_dictionary(f_list, path_O)


def sorting_dictionary(f_list, path_O):
    """
    Dictionary creation key = format: value = [filename, filename,
    etc] in order to group the streams with the same format into
    separate lists.

    """
    msg = msg_str()
    formats = {}  # Dizionario {formato1:[file1,file2,etc],..]}
    new_list = []  # La lista ripulita dai file non supportati
    all_formats = []  # tutti i formati supportati
    for selection, upper_f, lower_f, limits in supported_formats().values():
        all_formats.append(upper_f)  # WAV,AIF,FLAC,APE etc
        all_formats.append(lower_f)  # wav,aif,flac,ape etc

    # Creazione keys (chiavi) nel diz. formats:
    for i in f_list:  # Append separated file format
        name, ext = os.path.splitext(i)
        new = ext.replace(".", "")  # Tolgo il punto all'estensione
        if new in all_formats:  # Se estens. input è supportata
            new_list.append(i)  # Lista ripulita file importati
            if new.lower() not in formats:  # Add not present key at dict
                # Aggiungo chiavi non presenti nel diz + il valore
                # lista vuota: {formato:[]}
                formats[new.lower()] = []
        else:
            print('\n%s Not supported file format: "%s%s" >> skipping >>' % (
                                                                msg[0],
                                                                name,
                                                                ext
                                                                ))
    if new_list == []:  # se i file importati sono tutti incompatibili
        sys.exit('\n%s ...No audio files to process, exit!' % msg[1])
    # Creazione dei records (valori) nel diz. formats
    for i in new_list:
        name, ext = os.path.splitext(i)
        new = ext.replace(".", "")  # tolgo il punto all'estensione
        formats[new.lower()].append("%s%s" % (name, ext))
    menu_selections(formats, path_O)


def menu_selections(formats, path_O):
    """
    - Make input menu
    - Make output menu
    During output menu creation, Get a tuple with specified command
    elements

    """
    msg = msg_str()
    input_selection = []  # deve contenere solo interi(int)
    for input_format in list(formats.keys()):  # Itero sui formati importati
        # NOTE 1 RELOAD: ricarico nuovamente il grafico dei formati
        # integralmente con l'originale
        menu = graphic_menu()
        print("\n    Available formats for encoding/decoding "
              "'\033[32;1m%s\033[0m' audio files" % input_format)
        # Dizion. = {chiavi'srtinga 1':(integear,'formato')}
        # itero sulla tupla valori
        for v in supported_formats().values():
            if formats == {}:  # se è completamente vuoto, esco
                sys.exit('\n%s...End selection process, exit!\n' % msg[1])
            if input_format in v[1:3]:  # mi prendo gli interi corrispondenti
                input_selection.append(v[0])  # v[0] mi da l'intero
                menu = [menu[i] for i in range(len(menu))
                        if i not in set(v[3])
                        ]
                for outformat in menu:  # realizzazione menu di output
                    print("    %s" % outformat)
                output_selection = input("    Type a number corresponding"
                                         " format and press enter key... ")
                # ------------------- CREAZIONE OUTPUT MENU ------------------#
                main = Audio_Formats(input_format)  # Have a ext input >
                output_format = main.output_selector(output_selection)
                tuple_data = main.pairing_formats()  # return tuple data codec
                if output_selection == 'a' or output_selection == 'A':
                    print('audiomass: \033[1mAbort!\033[0m')
                    sys.exit()
                elif output_format is None:
                    # Se nessuna selezione e premi enter rimuovo chiave
                    # e valore dal dizionario, cioè escludo quei files
                    # dalla conversione.
                    print("\n%s Unknow option '%s' >> skipping" % (
                                                            msg[0],
                                                            output_selection
                                                            ))
                    formats.pop(input_format, None)
                    continue  # meglio partire da capo

                if tuple_data == 'key_error':
                    print("\n%s No match available for '%s' option >> "
                          "skipping >>" % (msg[0], output_selection))
                    formats.pop(input_format, None)
                    continue  # troppi errori, meglio contimuare da capo

                bitrate_test(tuple_data, output_format,
                             formats.get(input_format), path_O
                             )


def bitrate_test(tuple_data, output_format, path_in, path_O):
    """
    Check if codec support bitrate for level compression.

    """
    msg = msg_str()
    dict_bitrate = tuple_data[1]  # dict with corresponding bitrate values
    graphic_bitrate = tuple_data[2]  # list with strings for graphic choice
    contestual_text = tuple_data[3]  # 'please, select a bitrate value msg'
    # output_format = tuple_data[4]  # non serve, gia definito

    if dict_bitrate is None:
        bitrate = ''
    else:
        print(graphic_bitrate)
        level = input(contestual_text)
        a = Audio_Formats(None)
        bitrate = a.quality_level(dict_bitrate, level)
        valid = bitrate
        if valid is False:
            print("\n%s Unknow quality level '%s', ...use default\n" % (
                                                            msg[0], level))
            bitrate = ''
    command_builder(tuple_data, bitrate, output_format, path_in, path_O)


def command_builder(tuple_data, bitrate, output_format, path_in, path_O):
    """
    command_builder build the command with the options, the paths names,
    etc. The 'id_codec' variable, contains the key (codec) for an
    corresponding value with command_dict.

    """
    msg = msg_str()
    id_codec = tuple_data[0]  # as lame --decodec or oggenc, etc
    count = 0
    not_processed = []
    for path_name in path_in:
        stream_I = os.path.basename(path_name)  # input, es: nome-canzone.wav'
        file_name = os.path.splitext(stream_I)[0]  # only stream with no ext
        count += 1
        if path_O is None:  # se scrive l'output nell'input source
            path_O = os.path.dirname(path_name)  # prendo lo stesso input path
        norm = os.path.join('%s' % path_O,
                            '%s.%s' % (file_name,
                                       output_format)
                            )  # rendo portabili i pathnames
        if os.path.exists(norm):
            print("\n%s Already exists > '%s' >> skipping >>" % (msg[0], norm))
            # path_in.remove(path_name)
            not_processed.append(path_name)
            continue

        command = build_cmd(id_codec, bitrate, path_name, norm)
        print("\n\033[36;7m|%s| %s Output:\033[0m >> "
              "'%s'\n" % (str(count), output_format, norm)
              )
        try:
            # print (command) # uncomment for debug
            subprocess.check_call(command, shell=True)
        except subprocess.CalledProcessError as err:
            sys.exit("audioamass:\033[31;1mERROR!\033[0m %s" % (err))

    if not_processed:
        for fiLe in not_processed:
            if fiLe in path_in:
                path_in.remove(fiLe)
        # print ("\n\033[31;7mStreams NOT Processed:\033[0m >> %s\n" % (
                                                            # not_processed
                                                            # ))
        print("\n\033[33;7;3mFiles NOT Processed:\033[0m")
        for list1 in not_processed:
            print(list1)
    # print ("\n\033[32;7mQueue Streams Processed:\033[0m >> %s\n" % (path_in))
    if path_in:
        print("\n\033[32;7mQueue Files Processed:\033[0m")
        for list2 in path_in:
            print(list2)
    print("\n\033[37;7mDone...\033[0m\n")
