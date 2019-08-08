#
#########################################################
# Name: main_prg.py
# Porpose:  Boot straps and arg parser for audiomass script
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015/2017 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (Ver.0.7) December 2017
# Rev: dec 9 2017, Aug 8 2019
#########################################################
import sys
import os
from admspack.whichcraft import check_dependencies
from admspack.datastrings import info
from admspack.process_file import file_parser
from admspack.process_dir import  dir_parser
from admspack.process_batch import batch_parser

AUTHOR, MAIL, COPYRIGHT, VERSION, RELEASE, RLS_NAME, PRG_NAME, URL, \
    SHORT_DESCRIPT, LONG_DESCRIPT, USAGE, LICENSE, SHORT_LICENSE, TRY = info()

warnings = 'audiomass: \033[33;7;3mwarning:\033[0m'
errors = 'audiomass: \033[31;7;3merror:\033[0m'
file_access = "%s Unable to access, invalid file-name  >\033[0m" % errors
dir_access = "%s Unable to access, Invalid dir-name  >\033[0m" % errors
title = ("""\033[1m%s\033[0m - audio conversion utility""" %(RLS_NAME))

def main():
    """
    Boot straps and arg parsing
    """
    if '-f' in sys.argv or '--file' in sys.argv:
        print (title)
        get_file()
    elif '-d' in sys.argv or '--dir' in sys.argv:
        print (title)
        get_dir()
    elif '-b' in sys.argv or '--batch' in sys.argv:
        print (title)
        get_batch()
    elif '-C' in sys.argv or '--check' in sys.argv:
        print (title)
        check_dependencies()
    elif '-v' in sys.argv or '--version' in sys.argv:
        print ("%s - version %s - released %s" % (RLS_NAME, VERSION, 
                                                  RELEASE))
    elif '-h' in sys.argv or '--help' in sys.argv:
        print (USAGE)
    elif '-c' in sys.argv or '--copying' in sys.argv:
        print (LICENSE)
    elif len(sys.argv) == 1:
        print (title)
        print (TRY)
    else:
        sys.exit("%s Invalid options: '%s' \n%s" % (errors,
                                            sys.argv[1:][0], TRY))
    return 0

def get_file():
    """
    Get the filename and output dirname if output dirname in sys.argv
    """
    opts = [x for x in ['-o','--output'] if x in sys.argv]
    try:
        if os.path.isfile(sys.argv[2]): # must be file only here
            path_in = os.path.abspath(sys.argv[2]) # is a file-name
        else:
            sys.exit("%s %s" % (file_access, sys.argv[2]))
    except IndexError:
        sys.exit("%s Missing argument after '%s' option.\n%s" % (errors,
                                                    sys.argv[1],TRY))
    if len(sys.argv) == 4 or len(sys.argv) >= 4:
        #if sys.argv[3] != '-o':
        if sys.argv[3] not in opts:
            sys.exit("%s Invalid option: '%s' \n%s"% (errors,
                                                      sys.argv[3], TRY))
        if len(sys.argv) >= 5:
            if os.path.isdir(sys.argv[4]):
                path_out = os.path.abspath(sys.argv[4]) # this is a dir-name
            else:
                sys.exit("%s %s"%(dir_access ,sys.argv[4]))
        else:
            sys.exit("%s Missing output dir-name after '%s' option.\n%s" % (
                                                        errors, opts[0],TRY))
    else:
        path_out = None
    # input_format is the extension format of path_in
    input_format = os.path.splitext(path_in)[1].replace(".","")
    file_parser(input_format, path_in, path_out)

def get_dir():
    """
    Get input dirname and output dirname if output dirname in sys.argv
    """
    opts = [x for x in ['-o','--output'] if x in sys.argv]
    try:
        if os.path.isdir(sys.argv[2]): 
            path_in = os.path.abspath(sys.argv[2]) # this is a dir-name
        else:
            sys.exit("%s %s"%(dir_access ,sys.argv[2]))
    except IndexError:
        sys.exit("%s Missing argument\n%s" % (errors,TRY))
    if len(sys.argv) == 4 or len(sys.argv) >= 4:
        if sys.argv[3] not in opts:
            sys.exit("%s Invalid option: '%s' \n%s"% (errors,
                                                      sys.argv[3], TRY))
        if len(sys.argv) >= 5:
            if os.path.isdir(sys.argv[4]):
                path_out = os.path.abspath(sys.argv[4]) # this is a dir-name
            else:
                sys.exit("%s %s"%(dir_access ,sys.argv[4]))
        else:
            sys.exit("%s Missing output dir-name after '%s' option.\n%s" % (
                                                        errors, opts[0],TRY))
    else:
        path_out = None
    dir_parser(path_in, path_out)

def get_batch():
    """
    Groups a queued input file stream and puts it in the queue list. 
    Call the specified function and send queue list and output dirname 
    if output dirname in sys.argv.
    """
    queue = []
    opts = [x for x in ['-o','--output'] if x in sys.argv]
    if opts:
        opt = sys.argv.index(opts[0])
        try:
            if sys.argv[opt +1]:# se trovo percorso dopo opzione -o --output
                path_O = sys.argv[opt +1]
                
        except IndexError:
            sys.exit( "%s Missing argument after '%s' option.\n%s" % (
                                                        errors, opts[0], TRY))
        else:
            if os.path.isdir(path_O):#se opzione e percorso output corretti
                arg = sys.argv[2:] # incorpora solo gli input pathnames
                arg.remove(opts[0])# infatti rimuovo '-o' , '--output'
                arg.remove(path_O) # e rimuovo l'eventuale output pathname
                path_O = os.path.abspath(path_O)#ora setto il pathname
            else:
                sys.exit("%s %s"%(dir_access ,path_O))
    else:
        path_O = None
        arg = sys.argv[2:] # dal 2° arg. lista

    for f in arg:
        if os.path.isfile(os.path.abspath(f)): # must be file only here
            queue.append(f) 
        else:
            sys.exit("%s '%s'" % (file_access, f))
    if not queue:
        sys.exit("%s Missing argument after '%s' option.\n%s" % (errors,
                                                    sys.argv[1],TRY))
    batch_parser(queue, path_O)


if __name__ == '__main__':
    status = main()
    sys.exit(status)
