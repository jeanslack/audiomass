# -*- coding: utf-8 -*-
"""
Name: cli.py
Porpose:  Main args parser for audiomass script
Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
Copyright: (c) 2015/2021 Gianluca Pernigoto <jeanlucperni@gmail.com>
license: GPL3
Rev: dec 9 2017, Aug 8 2019, Dec 09 2021, Dec 16 2021
Code checker: flake8, pylint
"""
import sys
import os
import argparse
from audiomass import (
    __version__,
    __release__,
    __rls_name__,
    __prg_name__,
)
from audiomass.utils import whichcraft
from audiomass.dir_conversion import DirConvert
from audiomass.batch_conversion import BatchConvert


def on_folder(inputdir, outputdir):
    """
    Check for dirs
    """
    if os.path.isdir(inputdir):
        path_in = os.path.abspath(os.path.join(inputdir))
    else:
        sys.exit(f"\033[31;1mERROR:\033[0m "
                 f"Invalid input folder '{inputdir}'")

    if outputdir == '.':
        path_out = None
    else:
        if os.path.isdir(outputdir):
            path_out = os.path.abspath(os.path.join(outputdir))
        else:
            sys.exit(f"\033[31;1mERROR:\033[0m "
                     f"Invalid output folder '{outputdir}'")

    return path_in, path_out


def on_files(inputfiles, outputdir):
    """
    Check for input files and output dir

    """
    for fname in inputfiles:
        if not os.path.isfile(os.path.abspath(os.path.join(fname))):
            sys.exit(f"\033[31;1mERROR:\033[0m "
                     f"Invalid filename '{fname}'")

    if outputdir == '.':
        path_out = None
    else:
        if os.path.isdir(outputdir):
            path_out = os.path.abspath(os.path.join(outputdir))
        else:
            sys.exit(f"\033[31;1mERROR:\033[0m "
                     f"Invalid output folder '{outputdir}'")

    return inputfiles, path_out


def main():
    """
    args parsing using argparse module
    """
    parser = argparse.ArgumentParser(
                prog=__prg_name__,
                description=(f"\n\033[1m{__prg_name__}\033[0m - Wrapper "
                             f"for multiple audio conversion libraries.\n"),
                )

    parser.add_argument('--version',
                        help="Show the current version and exit",
                        action='version',
                        version=(f"{__rls_name__} - version {__version__} - "
                                 f"released {__release__}"),
                        )
    parser.add_argument('-c', '--check-requires',
                        help="List of installed or missing dependencies",
                        action="store_true",
                        )
    parser.add_argument('-d', '--directory',
                        metavar='INPUT_FOLDER',
                        type=str,
                        help=("Path to input folder. Converts a bunch "
                              "of audio files contained in a folder"),
                        action="store",
                        )
    parser.add_argument('-f', '--files',
                        type=str,
                        help=("Convert one or more audio files separated "
                              "by spaces, even with different formats"),
                        nargs='+',
                        metavar='..FILE ..FILE',
                        action="store",
                        )
    parser.add_argument("-o", "--output",
                        action="store",
                        type=str,
                        dest="output_folder",
                        help=("Path to output folder, default same "
                              "destination as input file"),
                        required=False,
                        default='.'
                        )
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.error("Use at least one optional argument")

    if args.files and args.directory:
        parser.error("No action requested, add '--directory' "
                     "or '-files', not both")

    if args.check_requires:
        print(f"\n\033[1m{__rls_name__}\033[0m - "
              f"check of available audio libraries:")
        whichcraft()

    if args.directory:
        inp, out = on_folder(args.directory, args.output_folder)
        conv = DirConvert(inp, out)
        conv.prompt_to_output_format()
        conv.command_builder()
        conv.end_check()

    elif args.files:
        inp, out = on_files(args.files, args.output_folder)
        conv = BatchConvert(inp, out)
        conv.prompt_to_output_format()
        conv.command_builder()
        conv.end_check()

    return 0


if __name__ == '__main__':
    STATUS = main()
    sys.exit(STATUS)
