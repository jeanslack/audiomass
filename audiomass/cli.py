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
from audiomass.whichcraft import check_dependencies
from audiomass.dir_conversion import dir_process
from audiomass.batch_conversion import BatchConvert


def get_dir(inputdir, outputdir):
    """
    Check for dirs
    """
    if os.path.isdir(inputdir):
        path_in = os.path.abspath(os.path.join(inputdir))
    else:
        sys.exit(f"\033[31;1mERROR:\033[0m "
                 f"Invalid input directory '{inputdir}'")

    if outputdir == '.':
        path_out = None
    else:
        if os.path.isdir(outputdir):
            path_out = os.path.abspath(os.path.join(outputdir))
        else:
            sys.exit(f"\033[31;1mERROR:\033[0m "
                     f"Invalid output directory '{outputdir}'")

    return path_in, path_out


def get_batch(inputfiles, outputdir):
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
                     f"Invalid output directory '{outputdir}'")

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

    parser.add_argument('-v', '--version',
                        help="Show the current version and exit",
                        action='version',
                        version=(f"{__rls_name__} - version {__version__} - "
                                 f"released {__release__}"),
                        )
    parser.add_argument('-c', '--check-requires',
                        help="List of installed or missing dependencies",
                        action="store_true",
                        )
    parser.add_argument('-d', '--onedir',
                        metavar='DIR',
                        type=str,
                        help=("Converts a bunch of audio files "
                              "contained in a directory"),
                        action="store",
                        )
    parser.add_argument('-b', '--batch',
                        type=str,
                        help=("Convert a single file or a queue of "
                              "files even with different formats"),
                        nargs='+',
                        metavar='..FILE ..FILE',
                        action="store",
                        )
    parser.add_argument("-o", "--output-dir",
                        action="store",
                        type=str,
                        dest="outputdir",
                        help=("Output directory, default same "
                              "destination as input file"),
                        required=False,
                        default='.'
                        )
    args = parser.parse_args()

    if args.batch and args.onedir:
        parser.error("Use the '-d' option or the '-b' option, "
                     "not both. Invalid arguments.")

    if args.check_requires:
        print(f"\n\033[1m{__rls_name__}\033[0m - "
              f"check of available audio libraries:")
        check_dependencies()

    if args.onedir:
        inp, out = get_dir(args.onedir, args.outputdir)
        dir_process(inp, out)

    elif args.batch:
        inp, out = get_batch(args.batch, args.outputdir)
        conv = BatchConvert(inp, out)
        conv.prompt_to_get_format_and_bitrate()
        conv.command_builder()
        conv.end_check()


    return 0


if __name__ == '__main__':
    STATUS = main()
    sys.exit(STATUS)
