# -*- coding: utf-8 -*-
"""
Name: cli.py
Porpose:  Main args parser for audiomass script
Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
Copyright: (c) 2015/2021 Gianluca Pernigoto <jeanlucperni@gmail.com>
license: GPL3
Rev: dec 9 2017, Aug 8 2019, Dec 09 2021
Code checker: flake8, pylint
"""
import sys
import os
from audiomass import (
    # __author__,
    # __mail__,
    # __copyright__,
    __version__,
    __release__,
    __rls_name__,
    # __prg_name__,
    # __url__,
    # __short_descript__,
    # __long_descript__,
    __usage__,
    __try__,
    __license__,
    # __short_license__,
    )
from audiomass.datastrings import msg_str
from audiomass.whichcraft import check_dependencies
from audiomass.process_file import file_parser
from audiomass.process_dir import dir_parser
from audiomass.process_batch import batch_parser


def main():
    """
    Boot straps and arg parsing

    """
    msg = msg_str()

    if '-f' in sys.argv or '--file' in sys.argv:
        get_file()

    elif '-d' in sys.argv or '--dir' in sys.argv:
        get_dir()

    elif '-b' in sys.argv or '--batch' in sys.argv:
        get_batch()

    elif '-c' in sys.argv or '--check' in sys.argv:
        print(f"\n\033[1m{__rls_name__}\033[0m - "
              f"check of available audio libraries:")
        check_dependencies()

    elif '-v' in sys.argv or '--version' in sys.argv:
        print(f"{__rls_name__} - version {__version__} - "
              f"released {__release__}")

    elif '-h' in sys.argv or '--help' in sys.argv:
        print(f"\n\033[1m{__rls_name__}\033[0m - Wrapper "
              f"for multiple audio conversion libraries.\n")
        print(__usage__)

    elif '-C' in sys.argv or '--copying' in sys.argv:
        print(__license__)

    elif len(sys.argv) == 1:
        print(__try__)

    else:
        raise SystemExit(f"{msg[1]} Invalid options: "
                         f"'{sys.argv[1:][0]}' \n{__try__}")
    return 0


def get_file():
    """
    Get the filename and output dirname if output dirname in sys.argv

    """
    msg = msg_str()
    opts = [x for x in ['-o', '--output'] if x in sys.argv]
    try:
        if os.path.isfile(sys.argv[2]):  # must be file only here
            path_in = os.path.abspath(os.path.join(sys.argv[2]))  # filename
        else:
            sys.exit(f"{msg[2]} {sys.argv[2]}")
    except IndexError:
        sys.exit(f"{msg[1]} Missing argument after '{sys.argv[1]}' "
                 f"option\n{__try__}")

    if len(sys.argv) == 4 or len(sys.argv) >= 4:
        # if sys.argv[3] != '-o':
        if sys.argv[3] not in opts:
            raise SystemExit(f"{msg[1]} Invalid option: "
                             f"'{sys.argv[3]}'\n{__try__}")

        if len(sys.argv) >= 5:
            if os.path.isdir(sys.argv[4]):
                path_out = os.path.abspath(os.path.join(sys.argv[4]))  # dirn
            else:
                raise SystemExit(f"{msg[3]} {sys.argv[4]}")
        else:
            raise SystemExit(f"{msg[1]} Missing output dirname "
                             f"after '{opts[0]}' option\n{__try__}")
    else:
        path_out = None
    # input_format is the extension format of path_in
    input_format = os.path.splitext(path_in)[1].replace(".", "")
    file_parser(input_format, path_in, path_out)


def get_dir():
    """
    Get input dirname and output dirname if output dirname in sys.argv

    """
    msg = msg_str()
    opts = [x for x in ['-o', '--output'] if x in sys.argv]
    try:
        if os.path.isdir(sys.argv[2]):
            path_in = os.path.abspath(os.path.join(sys.argv[2]))  # dirname
        else:
            sys.exit(f"{msg[3]} {sys.argv[2]}")
    except IndexError:
        sys.exit(f"{msg[1]} Missing argument\n{__try__}")

    if len(sys.argv) == 4 or len(sys.argv) >= 4:
        if sys.argv[3] not in opts:
            raise SystemExit(f"{msg[1]} Invalid option: '{sys.argv[3]}' "
                             f"\n{__try__}")
        if len(sys.argv) >= 5:
            if os.path.isdir(sys.argv[4]):
                path_out = os.path.abspath(os.path.join(sys.argv[4]))  # dirn
            else:
                raise SystemExit(f"{msg[3]} {sys.argv[4]}")
        else:
            raise SystemExit(f"{msg[1]} Missing output dirname "
                             f"after '{opts[0]}' option\n{__try__}")
    else:
        path_out = None
    dir_parser(path_in, path_out)


def get_batch():
    """
    Groups a queued input file stream and puts it in the queue list.
    Call the specified function and send queue list and output dirname
    if output dirname in sys.argv.

    """
    msg = msg_str()
    queue = []
    opts = [x for x in ['-o', '--output'] if x in sys.argv]
    if opts:
        opt = sys.argv.index(opts[0])
        try:
            if sys.argv[opt + 1]:  # se trovo percorso dopo opzione -o --output
                path_o = sys.argv[opt + 1]

        except IndexError:
            sys.exit(f"{msg[1]} Missing argument "
                     f"after '{opts[0]}' option\n{__try__}")
        else:
            if os.path.isdir(path_o):  # se opzione e percorso output corretti
                arg = sys.argv[2:]  # incorpora solo gli input pathnames
                arg.remove(opts[0])  # infatti rimuovo '-o' , '--output'
                arg.remove(path_o)  # e rimuovo l'eventuale output pathname
                path_o = os.path.abspath(os.path.join(path_o))  # pathn set
            else:
                raise SystemExit(f"{msg[3]} {path_o}")
    else:
        path_o = None
        arg = sys.argv[2:]  # list from 2° arg.

    for fname in arg:
        # must be file
        if os.path.isfile(os.path.abspath(os.path.join(fname))):
            queue.append(fname)
        else:
            raise SystemExit(f"{msg[2]} '{fname}'")
    if not queue:
        raise SystemExit(f"{msg[1]} Missing argument "
                         f"after '{sys.argv[1]}' option\n{__try__}")
    batch_parser(queue, path_o)


if __name__ == '__main__':
    STATUS = main()
    sys.exit(STATUS)
