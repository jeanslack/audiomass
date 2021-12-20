# -*- coding: utf-8 -*-
"""
Name:         batch_conversion.py (module)
Porpose:      Handles the audio data files for batch conversions.
Writer:       Gianluca Pernigoto <jeanlucperni@gmail.com>
Copyright:    (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
license:      GPL3
Rev:          Nov 27 2017, Dec.15 2017, Aug.10 2019, Dec 17 2021
Code checker: flake8, pylint
"""
import subprocess
import sys
import os
from collections import Counter
from audiomass.datastrings import msgdebug, msgcolor, msgcustom, msgend
from audiomass.audio_formats import AudioFormats
from audiomass.comparisions import supported_formats
from audiomass.comparisions import text_menu
from audiomass.comparisions import build_cmd


def show_format_menu(indexes):
    """
    print a text menu with audio format references
    """
    menu = text_menu()
    setmenu = [menu[i] for i in range(len(menu)) if i not in set(indexes)]
    for outformat in setmenu:  # realizzazione menu di output
        msgcustom(f"{outformat}")


def get_format_and_bitrate(input_format, output_select):
    """
    Return an available audio format and its codec data
    """
    main = AudioFormats(input_format)
    output_format = main.output_selector(output_select)
    codec_data = main.pairing_formats()

    if output_format is None or codec_data == 'key_error':
        return None, None

    return output_format, codec_data


def on_bitrate(data_codec):
    """
    Check bitrate for level compression if
    supported by codec.
    Returns the codec name and bitrate
    """
    codec_name = data_codec[0]  # as lame --decodec or oggenc, flac, etc
    dict_bitrate = data_codec[1]  # dict with corresponding bitrate values
    graphic_bitrate = data_codec[2]  # list with strings for graphic choice
    contestual_text = data_codec[3]  # 'please, select a bitrate value msg'
    # output_format = data_codec[4]  # non serve, gia definito

    if dict_bitrate is None:
        bitrate = ''
    else:
        msgcustom(graphic_bitrate)

        while True:
            level = input(contestual_text)
            audio = AudioFormats(None)
            bitrate = audio.quality_level(dict_bitrate, level)
            if bitrate is False:
                msgdebug(err=f"Invalid option '{level}'")
                continue
                # bitrate = ''
            break

    return codec_name, bitrate


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


class BatchConvert():
    """
    The goal of this class is to obtain a catalog of one
    or more audio files, even with different formats and
    paths, and associate them with the data required for
    conversion into other audio formats, all in a convenient
    data structure.

    USE:
        conv = BatchConvert([file.wav, file.flac, etc]  out=None)
        conv.prompt_to_get_format_and_bitrate()
        conv.command_builder()
        conv.end_check()

    NOTE: the ``out`` default argument can accept the
          path of an output folder.
          the ``end_check`` method is optional but useful
          for printing debug messages and the final result.
    """
    def __init__(self, f_list, outdir):
        """
        Evaluate the supported audio formats and assign them
        in a 'files' list of the self.filecatalog dictionary
        in order to group the files with the same format into
        separated lists, example:

            {'wav': {'files': [file1.wav, file2.wav],
            'flac': [file3.flac], 'mp3': [file4.mp3, file5.mp3]}

        """
        self.filecatalog = {}
        self.outdir = outdir
        self.not_processed = []
        self.processed = []
        self.warnings = []
        self.info = []
        f_list = self.remove_duplicates_from_list(f_list)
        supported_filelist = []  # clean list with no fake file formats
        all_formats = []  # all available supported formats

        for val in supported_formats().values():
            all_formats.append(val[0])  # WAV,AIF,FLAC,APE etc
            all_formats.append(val[1])  # wav,aif,flac,ape etc

        # populate self.filecatalog:
        for finp in f_list:
            name = os.path.splitext(finp)[0]
            ext = os.path.splitext(finp)[1].replace(".", "")
            if ext in all_formats:  # if supported
                supported_filelist.append(finp)  # cleaned list
                if ext.lower() not in self.filecatalog:
                    # add key=format : val=[[]]
                    self.filecatalog[ext.lower()] = {'files': []}
            else:
                self.warnings.append(f"Invalid file format: "
                                     f"'{name}.{ext}' ..skip")

        if not supported_filelist:  # if not files
            sys.exit(msgdebug(err='...No audio files to convert, exit!'))

        # Creazione dei records (valori) nel diz. self.filecatalog
        for i in supported_filelist:
            name = os.path.splitext(i)[0]
            ext = os.path.splitext(i)[1].replace(".", "")
            self.filecatalog[ext.lower()]['files'].append(f"{name}.{ext}")
    # ------------------------------------------------------------------#

    def remove_duplicates_from_list(self, f_list):
        """
        Clean-up list contaminated by possible duplicate files
        using set()

        """
        val = 0
        for key, val in Counter(f_list).items():
            if val > 1:
                self.info.append(f"duplicate: '{key}' ..removing")

        # removal of any duplicates in the list using set()
        return list(set(f_list)) if val > 1 else f_list
    # ------------------------------------------------------------------#

    def prompt_to_get_format_and_bitrate(self):
        """
        Get the prompt strings of the audio format and bitrate
        """
        for input_format in list(self.filecatalog.keys()):
            msgcustom(f"\n\033[1mConvert the '\033[32;1m"
                      f"{input_format}\033[0m'format to:\033[0m")

            for supp in supported_formats().values():
                if not self.filecatalog:
                    sys.exit(msgdebug(err="...exit!\n"))
                if input_format in supp[0:2]:
                    show_format_menu(supp[2])  # show text menu before prompt
                    while True:
                        output_select = input("Type a format number among "
                                              "those available, and press "
                                              "the Enter key > ")
                        if output_select in ('a', 'A'):
                            msgend(abort=True)
                            sys.exit()
                        ext, cod = get_format_and_bitrate(input_format,
                                                          output_select)
                        if ext is None and cod is None:
                            msgdebug(err=f"Invalid option '{output_select}'")
                            continue
                        break

                    codec, bitrate = on_bitrate(cod)
                    self.filecatalog[input_format]['codec'] = codec
                    self.filecatalog[input_format]['bitrate'] = bitrate
                    self.filecatalog[input_format]['format'] = ext

        return self.filecatalog
    # ------------------------------------------------------------------#

    def command_builder(self):
        """
        Build the command and pass it to `run_subprocess` function
        """
        count = 0
        for key, val in self.filecatalog.items():
            for fname in val['files']:
                inputfile = os.path.basename(fname)
                file_name = os.path.splitext(inputfile)[0]
                count += 1
                if self.outdir is None:
                    self.outdir = os.path.dirname(fname)
                # rendo portabili i pathnames:
                norm = os.path.join(self.outdir,
                                    f"{file_name}.{val['format']}")
                if os.path.exists(norm):
                    self.warnings.append(f"Already exists > '{norm}' ..skip")
                    self.not_processed.append(fname)
                    continue
                command = build_cmd(val['codec'],
                                    val['bitrate'],
                                    fname,
                                    norm
                                    )
                msgcolor(head='\n', green2=(f"|{str(count)}| "
                                            # f"{val['format']} "
                                            f"{key} "
                                            f"Output:"), tail=f" >> '{norm}'")
                self.processed.append(norm)
                run_subprocess(command)
    # ------------------------------------------------------------------#

    def end_check(self):
        """
        Print debug messages at the end of the tasks
        """
        if self.warnings:
            for msg in self.warnings:
                msgdebug(warn=msg)

        if self.info:
            for msg in self.info:
                msgdebug(info=msg)

        if self.not_processed:
            msgcolor(orange="\nInput files NOT converted:")
            for list1 in self.not_processed:
                msgcustom(list1)

        if self.processed:
            msgcolor(green="\nConverted successfully:")
            for list2 in self.processed:
                msgcustom(list2)
        msgend(done=True)
