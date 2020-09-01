# -*- coding: utf-8 -*-
#
#########################################################
# Name: audiomass.py
# Porpose:  Boot straps and arg parser for audiomass script
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015/2017 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (Ver.0.7) December 2017
# Rev: dec 9 2017, Aug 8 2019
#########################################################
import sys
import os
from src import (
    __author__,
    __mail__,
    __copyright__,
    __version__,
    __release__,
    __rls_name__,
    __prg_name__,
    __url__,
    __short_descript__,
    __long_descript__,
    __usage__,
    __try__,
    __license__,
    __short_license__,
    )
from src.datastrings import msg_str
from src.whichcraft import check_dependencies
from src.process_file import file_parser
from src.process_dir import dir_parser
from src.process_batch import batch_parser


def main():
    """
    Boot straps and arg parsing

    """
    msg = msg_str()
    title = ("\033[1m%s\033[0m - Wrapper for multiple audio "
             "conversion libraries." % (__rls_name__))

    if '-f' in sys.argv or '--file' in sys.argv:
        print(title)
        get_file()
    elif '-d' in sys.argv or '--dir' in sys.argv:
        print(title)
        get_dir()
    elif '-b' in sys.argv or '--batch' in sys.argv:
        print(title)
        get_batch()
    elif '-C' in sys.argv or '--check' in sys.argv:
        print(title)
        check_dependencies()
    elif '-v' in sys.argv or '--version' in sys.argv:
        print("%s - version %s - released %s" % (__rls_name__,
                                                 __version__,
                                                 __release__
                                                 ))
    elif '-h' in sys.argv or '--help' in sys.argv:
        print(__usage__)
    elif '-c' in sys.argv or '--copying' in sys.argv:
        print(__license__)
    elif len(sys.argv) == 1:
        print(title)
        print(__try__)
    else:
        raise SystemExit("%s Invalid options: '%s' \n%s" % (msg[1],
                                                            sys.argv[1:][0],
                                                            __try__
                                                            ))
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
            sys.exit("%s %s" % (msg[2], sys.argv[2]))
    except IndexError:
        sys.exit("%s Missing argument after option '%s'\n%s" % (msg[1],
                                                                sys.argv[1],
                                                                __try__
                                                                ))
    if len(sys.argv) == 4 or len(sys.argv) >= 4:
        # if sys.argv[3] != '-o':
        if sys.argv[3] not in opts:
            raise SystemExit("%s Invalid option: '%s' \n%s" % (msg[1],
                                                               sys.argv[3],
                                                               __try__
                                                               ))
        if len(sys.argv) >= 5:
            if os.path.isdir(sys.argv[4]):
                path_out = os.path.abspath(os.path.join(sys.argv[4]))  # dirn
            else:
                raise SystemExit("%s %s" % (msg[3], sys.argv[4]))
        else:
            raise SystemExit("%s Missing output dir-name after option "
                             "'%s'\n%s" % (msg[1], opts[0], __try__))
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
            sys.exit("%s %s" % (msg[3], sys.argv[2]))
    except IndexError:
        sys.exit("%s Missing argument\n%s" % (msg[1], __try__))

    if len(sys.argv) == 4 or len(sys.argv) >= 4:
        if sys.argv[3] not in opts:
            raise SystemExit("%s Invalid option: '%s' \n%s" % (msg[1],
                                                               sys.argv[3],
                                                               __try__
                                                               ))
        if len(sys.argv) >= 5:
            if os.path.isdir(sys.argv[4]):
                path_out = os.path.abspath(os.path.join(sys.argv[4]))  # dirn
            else:
                raise SystemExit("%s %s" % (msg[3], sys.argv[4]))
        else:
            raise SystemExit("%s Missing output dir-name after option "
                             "'%s'\n%s" % (msg[1], opts[0], __try__))
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
                path_O = sys.argv[opt + 1]

        except IndexError:
            sys.exit("%s Missing argument after option '%s'\n%s" % (msg[1],
                                                                    opts[0],
                                                                    __try__
                                                                    ))
        else:
            if os.path.isdir(path_O):  # se opzione e percorso output corretti
                arg = sys.argv[2:]  # incorpora solo gli input pathnames
                arg.remove(opts[0])  # infatti rimuovo '-o' , '--output'
                arg.remove(path_O)  # e rimuovo l'eventuale output pathname
                path_O = os.path.abspath(os.path.join(path_O))  # pathname set
            else:
                raise SystemExit("%s %s" % (msg[3], path_O))
    else:
        path_O = None
        arg = sys.argv[2:]  # dal 2° arg. lista

    for f in arg:
        if os.path.isfile(os.path.abspath(os.path.join(f))):  # must be file
            queue.append(f)
        else:
            raise SystemExit("%s '%s'" % (msg[2], f))
    if not queue:
        raise SystemExit("%s Missing argument after option '%s'\n%s" % (
                                                                msg[1],
                                                                sys.argv[1],
                                                                __try__
                                                                ))
    batch_parser(queue, path_O)


if __name__ == '__main__':
    status = main()
    sys.exit(status)
