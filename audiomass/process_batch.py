# -*- coding: utf-8 -*-
"""
Name:         getcommand.py (module)
Porpose:      parsing the data files list for batch process.
Writer:       Gianluca Pernigoto <jeanlucperni@gmail.com>
Copyright:    (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
license:      GPL3
Rev:          Nov 27 2017, Dec.15 2017, Aug.10 2019, Dec 08 2021
Code checker: flake8, pylint
"""
import subprocess
import sys
import os
from collections import Counter
from audiomass.datastrings import msg_str
from audiomass.audio_formats import AudioFormats
from audiomass.comparisions import supported_formats
from audiomass.comparisions import graphic_menu
from audiomass.comparisions import build_cmd


def batch_parser(f_list, path_o):
    """
    Clean-up list contaminated by duplicate files.

    """
    msg = msg_str()
    for key, val in Counter(f_list).items():  # controllo doppioni accidentali.
        if val > 1:
            print(f"{msg[0]} Removing following duplicates: > '{key}' >")
    f_list = list(set(f_list))  # removal of any duplicates in the list
    sorting_dictionary(f_list, path_o)


def sorting_dictionary(f_list, path_o):
    """
    Dictionary creation key = format: value = [filename, filename,
    etc] in order to group the streams with the same format into
    separate lists.

    """
    msg = msg_str()
    formats = {}  # Dizionario {formato1:[file1,file2,etc],..]}
    new_list = []  # La lista ripulita dai file non supportati
    all_formats = []  # tutti i formati supportati

    for val in supported_formats().values():
        all_formats.append(val[1])  # WAV,AIF,FLAC,APE etc
        all_formats.append(val[2])  # wav,aif,flac,ape etc

    # Creazione keys (chiavi) nel diz. formats:
    for finp in f_list:  # Append separated file format
        name, ext = os.path.splitext(finp)
        new = ext.replace(".", "")  # Tolgo il punto all'estensione
        if new in all_formats:  # Se estens. input è supportata
            new_list.append(finp)  # Lista ripulita file importati
            if new.lower() not in formats:  # Add not present key at dict
                # Aggiungo chiavi non presenti nel diz + il valore
                # lista vuota: {formato:[]}
                formats[new.lower()] = []
        else:
            print(f'\n{msg[0]} Not supported file format: '
                  f'"{name}{ext}" >> skipping >>')
    if not new_list:  # se i file importati sono tutti incompatibili
        sys.exit(f'\n{msg[1]} ...No audio files to process, exit!')
    # Creazione dei records (valori) nel diz. formats
    for i in new_list:
        name, ext = os.path.splitext(i)
        new = ext.replace(".", "")  # tolgo il punto all'estensione
        formats[new.lower()].append(f"{name}{ext}")
    menu_selections(formats, path_o)


def menu_selections(formats, path_o):
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
        print(f"\n    Available formats for encoding/decoding "
              f"'\033[32;1m{input_format}\033[0m' audio files")
        # Dizion. = {chiavi'srtinga 1':(integear,'formato')}
        # itero sulla tupla valori
        for val in supported_formats().values():
            if formats == {}:  # se è completamente vuoto, esco
                sys.exit(f'\n{msg[1]}...End selection process, exit!\n')
            if input_format in val[1:3]:  # mi prendo gli interi corrispondenti
                input_selection.append(val[0])  # val[0] mi da l'intero
                menu = [menu[i] for i in range(len(menu))
                        if i not in set(val[3])
                        ]
                for outformat in menu:  # realizzazione menu di output
                    print(f"    {outformat}")
                output_selection = input("    Type a number corresponding "
                                         "to the format and press Enter "
                                         "key... ")
                # ------------------- CREAZIONE OUTPUT MENU ------------------#
                main = AudioFormats(input_format)  # Have a ext input >
                output_format = main.output_selector(output_selection)
                tuple_data = main.pairing_formats()  # return tuple data codec
                if output_selection in ('a', 'A'):
                    print('audiomass: \033[1mAbort!\033[0m')
                    sys.exit()
                elif output_format is None:
                    # Se nessuna selezione e premi enter rimuovo chiave
                    # e valore dal dizionario, cioè escludo quei files
                    # dalla conversione.
                    print(f"\n{msg[0]} Unknow option '{output_selection}' "
                          f">> skipping")
                    formats.pop(input_format, None)
                    continue  # meglio partire da capo

                if tuple_data == 'key_error':
                    print(f"\n{msg[0]} No match available for "
                          f"'{output_selection}' option >> skipping >>")
                    formats.pop(input_format, None)
                    continue  # troppi errori, meglio contimuare da capo

                bitrate_test(tuple_data, output_format,
                             formats.get(input_format), path_o
                             )


def bitrate_test(tuple_data, output_format, path_in, path_o):
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
        audio = AudioFormats(None)
        bitrate = audio.quality_level(dict_bitrate, level)
        valid = bitrate
        if valid is False:
            print(f"\n{msg[0]} Unknow quality level "
                  f"'{level}', ...use default\n")
            bitrate = ''
    command_builder(tuple_data, bitrate, output_format, path_in, path_o)


def command_builder(tuple_data, bitrate, output_format, path_in, path_o):
    """
    command_builder build the command with the options, the paths names,
    etc. The 'id_codec' variable, contains the key (codec) for an
    corresponding value with command_dict.

    """
    interrupted = None
    msg = msg_str()
    id_codec = tuple_data[0]  # as lame --decodec or oggenc, etc
    count = 0
    not_processed = []
    for path_name in path_in:
        stream_i = os.path.basename(path_name)  # input, es: nome-canzone.wav'
        file_name = os.path.splitext(stream_i)[0]  # only stream with no ext
        count += 1
        if path_o is None:  # se scrive l'output nell'input source
            path_o = os.path.dirname(path_name)  # prendo lo stesso input path
        # rendo portabili i pathnames:
        norm = os.path.join(path_o, f'{file_name}.{output_format}')
        if os.path.exists(norm):
            print(f"\n{msg[0]} Already exists > '{norm}' >> skipping >>")
            # path_in.remove(path_name)
            not_processed.append(path_name)
            continue

        command = build_cmd(id_codec, bitrate, path_name, norm)
        print(f"\n\033[36;7m|{str(count)}| {output_format} "
              f"Output:\033[0m >> '{norm}'\n"
              )
        try:
            #print(command) # uncomment for debug
            subprocess.run(command, check=True, shell=True)
        except subprocess.CalledProcessError as err:
            sys.exit(f"audiomass:\033[31;1m ERROR!\033[0m {err}")
        except KeyboardInterrupt:
            interrupted = True
            break

    if interrupted:
        sys.exit("\n\033[37;7mKeyboardInterrupt !\033[0m\n")

    if not_processed:
        for _file in not_processed:
            if _file in path_in:
                path_in.remove(_file)

        print("\n\033[33;7;3mFiles NOT Processed:\033[0m")
        for list1 in not_processed:
            print(list1)

    if path_in:
        print("\n\033[32;7mQueue Files Processed:\033[0m")
        for list2 in path_in:
            print(list2)
    print("\n\033[37;7mDone...\033[0m\n")
