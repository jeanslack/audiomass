# -*- coding: utf-8 -*-
"""
Name:         batch_conversion.py (module)
Porpose:      Handles the audio data files for batch conversions.
Writer:       Gianluca Pernigoto <jeanlucperni@gmail.com>
Copyright:    (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
license:      GPL3
Rev:          Nov 27 2017, Dec.15 2017, Aug.10 2019, Dec 20 2021
Code checker: flake8, pylint
"""
import sys
import os
from collections import Counter
from audiomass.datastrings import msgdebug, msgcolor, msgcustom, msgend
from audiomass.comparisions import supported_formats
from audiomass.utils import (show_format_menu,
                             get_codec_data,
                             build_cmd,
                             run_subprocess)


class BatchConvert():
    """
    The goal of this class is to obtain a catalog of one
    or more audio files, even with different formats and
    paths, and associate them with the data required for
    conversion into other different audio formats,
    all in a convenient data structure for processing.

    USE:
        conv = BatchConvert([file.wav, file.flac, ...], out=None)
        conv.prompt_to_format()
        conv.command_builder()
        conv.end_check()

    NOTE: the ``out`` default argument can accept the
          path of an output folder.
          the ``end_check`` method is optional but useful
          for printing debug messages and the final result.
    """
    def __init__(self, f_list, outdir):
        """
        Evaluates formats compatibility of the imported files.
        This method is responsible to defining `self.filecatalog`
        attribute in order to group the files and data as values
        of a format key, example:

        {'wav': {'files': [file1.wav, file2.wav] 'data_codec': data, ...},
         'flac': {'files': [file3.flac], 'data_codec': ...},
         'mp3': {'files': [file4.mp3, file5.mp3], 'data_codec': ...}
         }

        """
        self.filecatalog = {}
        self.outdir = outdir
        self.not_processed = []
        self.processed = []
        self.warnings = []
        self.info = []
        self.errors = []
        f_list = self.remove_duplicates_from_list(f_list)
        unsupported = []

        # populate self.filecatalog:
        for infile in f_list:
            ext = os.path.splitext(infile)[1].replace(".", "")

            for frmt in supported_formats().values():
                if ext in frmt:
                    if frmt[1] not in self.filecatalog:  # create the key...
                        self.filecatalog[frmt[1]] = {'files': [],
                                                     'index': None}
                    # ...and
                    unsupported.append(infile)
                    self.filecatalog[frmt[1]]['files'].append(infile)
                    self.filecatalog[frmt[1]]['index'] = frmt[2]

        # make unsupported debug
        unsupported = [val for val in f_list if val not in unsupported]
        for unsup in unsupported:
            if unsup:
                self.warnings.append(f"Unsupported: '{unsup}' ..skip")
        # if not files...
        if not self.filecatalog:
            self.errors.append('...No audio files to convert, exit!')
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

    def prompt_to_output_format(self):
        """
        Prompt to set codec and output audio format.
        """
        for input_format, val in list(self.filecatalog.items()):
            msgcustom(f"\n\033[1mConvert the '\033[32;1m"
                      f"{input_format}\033[0m'format to:\033[0m")

            show_format_menu(val['index'])  # show text menu before prompt
            while True:
                output_select = input("Type a format number among those "
                                      "available, and press the Enter key > ")
                if output_select in ('a', 'A'):
                    msgend(abort=True)
                    sys.exit()
                codec = get_codec_data(input_format, output_select)

                if codec is None:
                    msgdebug(err=f"Invalid option '{output_select}'")
                    continue
                break

            self.filecatalog[input_format]['codec'] = codec[0]
            self.filecatalog[input_format]['format'] = codec[4]

            self.prompt_to_bitrate(codec, input_format)
    # ------------------------------------------------------------------#

    def prompt_to_bitrate(self, codec, input_format):
        """
        Prompt to set the audio bitrate
        """
        if codec[1] is None:  # None bitrate
            bitrate = ''
        else:
            msgcustom(codec[2])  # show menu

            while True:
                level = input(codec[3])  # show text menu before prompt
                if level in codec[1]:
                    bitrate = codec[1][level]
                else:
                    msgdebug(err=f"Invalid option '{level}'")
                    continue
                break

        self.filecatalog[input_format]['bitrate'] = bitrate
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
        if self.info:
            for msg in self.info:
                msgdebug(info=msg)

        if self.warnings:
            for msg in self.warnings:
                msgdebug(warn=msg)

        if self.errors:
            for msg in self.errors:
                msgdebug(err=msg)

        if self.not_processed:
            msgcolor(orange="\nInput files NOT converted:")
            for list1 in self.not_processed:
                msgcustom(list1)

        if self.processed:
            msgcolor(green="\nConverted successfully:")
            for list2 in self.processed:
                msgcustom(list2)
        msgend(done=True)
