# -*- coding: utf-8 -*-
"""
Name:         dir_conversion.py (module)
Porpose:      Handles the audio files conversions into specified folder.
Writer:       Gianluca Pernigoto <jeanlucperni@gmail.com>
Copyright:    (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
license:      GPL3
Rev:          Nov. 2017, Dec 08 2021
Code checker: flake8, pylint
"""
import glob
import sys
import os
from audiomass.comparisions import input_formats
from audiomass.datastrings import (msgdebug,
                                   msgcolor,
                                   msgcustom,
                                   msgend)
from audiomass.utils import (show_format_menu,
                             get_codec_data,
                             build_cmd,
                             run_subprocess)


class DirConvert():
    """
    Convert all audio files with a certain format placed
    in a given folder.

    USE:
        dirconv = BatchConvert(directory, out=None)
        dirconv.prompt_to_format()
        dirconv.command_builder()
        dirconv.end_check()

    NOTE: the ``out`` default argument can accept the
          path of an output folder.
          the ``end_check`` method is optional but useful
          for printing debug messages and the final result.
    """
    def __init__(self, path_i, path_o):
        """
        Print a text menu with a list of available formats
        and wait for user input. The input value given by the
        user represents the format of the files to be converted
        in a given folder .
        """
        # (too-many-instance-attributes) (FIXME)
        self.inputdir = path_i
        self.outputdir = path_o
        self.input_format = None
        self.output_format = None
        self.index = None
        self.codec = None
        self.bitrate = ''
        self.not_processed = []
        self.processed = []
        self.warnings = []
        self.info = []
        self.errors = []

        msgcustom("\n\033[1mWhat is the files format to convert?\033[0m")
        menu = ("------------",
                " \033[41;37;1m A \033[0m \033[1m..ABORT\033[0m",
                "------------")
        for outformat in menu:
            msgcustom(f"{outformat}")

        while True:
            input_selection = input("Type a file format to convert, "
                                    "and press the Enter key > ")
            if input_selection in ('a', 'A'):
                msgend(abort=True)
                sys.exit()
            for frmt in input_formats():
                if input_selection.lower() in frmt[0]:
                    self.input_format = input_selection
                    self.index = frmt[1]
            if self.input_format is None:
                msgdebug(err=(f"Unsupported format: '{input_selection}'"))
                continue
            break
    # ---------------------------------------------------------------#

    def prompt_to_output_format(self):
        """
        Prompt to get codec data and set the output audio format
        """
        msgcustom(f"\n\033[1mConvert the '\033[32;1m"
                  f"{self.input_format}\033[0m' format to:\033[0m")
        show_format_menu(self.index)  # show text menu before prompt

        while True:
            output_select = input("Type a format number among those "
                                  "available, and press the Enter key > ")
            if output_select in ('a', 'A'):
                msgend(abort=True)
                sys.exit()
            data_codec = get_codec_data(self.input_format, output_select)

            if data_codec is None:
                msgdebug(err=f"Invalid option '{output_select}'")
                continue
            break

        self.codec = data_codec[0]
        self.output_format = data_codec[4]

        self.prompt_to_bitrate(data_codec)
    # ---------------------------------------------------------------#

    def prompt_to_bitrate(self, data_codec):
        """
        Prompt to set the audio bitrate
        """
        if data_codec[1] is not None:  # None bitrate
            msgcustom(data_codec[2])  # show menu

            while True:
                level = input(data_codec[3])  # show text menu before prompt
                if level in data_codec[1]:
                    self.bitrate = data_codec[1][level]
                else:
                    msgdebug(err=f"Invalid option '{level}'")
                    continue
                break
    # ---------------------------------------------------------------#

    def command_builder(self):
        """
        Build the command and pass it to `run_subprocess` function
        """
        count = 0
        pname = None
        for suffix in [self.input_format, self.input_format.upper()]:
            # itero su nomi formato upper-case e lower-case
            for pname in glob.glob(os.path.join(self.inputdir, f"*.{suffix}")):
                basename = os.path.basename(pname)
                name = os.path.splitext(basename)[0]
                count += 1
                if self.outputdir is None:
                    # same dest as input file
                    self.outputdir = os.path.dirname(pname)

                fname = os.path.join(self.outputdir,
                                     f'{name}.{self.output_format}')
                if os.path.exists(fname):
                    self.warnings.append(f"Already exists > '{fname}' ..skip")
                    self.not_processed.append(pname)
                    continue  # next

                command = build_cmd(self.codec, self.bitrate, pname, fname)
                msgcolor(head='\n', green2=(f"|{str(count)}| "
                                            f"{self.output_format} "
                                            f"Output:"), tail=f" >> '{fname}'")

                self.processed.append(fname)
                run_subprocess(command)

        if not pname:
            self.errors.append(f"No files in '{self.input_format}' "
                               f"format found!")
    # ---------------------------------------------------------------#

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
