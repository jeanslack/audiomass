#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: getcommand.py (module)
# Porpose: get command options and passes to the process
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015/2016 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (Ver.0.6) Febbruary 2015
# Rev
#########################################################

import subprocess
import sys
import os
import process_cli
from audio_formats import Audio_Formats
from datastrings import input_menu, output_menu
from comparisions import a_formats


def batch_(path_in):
    """
    Get all options for specific audio codecs for the batch process
    """
    subprocess.call(['clear'])
    input_menu()
    input_selection = raw_input("Enter here the corresponding number "
                                "and hit enter... "
                                )
    main = Audio_Formats(None) # not have a ext input = None
    a = main.input_selector(input_selection) # let choice an input format
    input_format = a # return a input format string

    if input_selection == 'q' or input_selection == 'Q':
            sys.exit()
    elif input_format is None:
            sys.exit("\n\033[1mEntry error in select input format!\033[0m\n")

    graphic_a_format = output_menu()
    new = graphic_a_format[:]
    new.remove(graphic_a_format[int(input_selection)])

    subprocess.call(['clear'])
    print ('\n\n    The audio input files format is "%s" \n\n'
            '    Please, now type the output files format for '
            'encoding\n' % input_format)

    for outformat in new:
        print "    %s"%(outformat)

    output_selection = raw_input(
                '\n Type a letter for your encoding and just hit enter: ')
    b = main.output_selector(output_selection)
    output_format = b
    
    if output_selection == 'q' or output_selection == 'Q':
            sys.exit()
    elif output_format is None:
        sys.exit("\n\033[1mEntry error in select output format!\033[0m\n")
        
    if main.retcode == 'KeyError':
        sys.exit("\nSorry, this conversion is not possible\n")
        
    bitrate_test(main.retcode[0], main.retcode[1], main.retcode[2], 
                main.retcode[3], main.retcode[4], path_in, 'on', input_format)


def single_(input_format, path_in):
    """
    Get all options for specific audio codecs for a single process
    """
    supported_formats = a_formats()
    input_selection = None
    
    for support in supported_formats[0].values():
        if input_format in support[1]:
            input_selection = support[0]
    
    if input_selection is None:
        # the file-name must be supported and match with dict keys
        sys.exit('\nSorry, not format supported "%s"\nPlease, choice one of: '
        '%s\n' % (input_format, supported_formats[1]))

    graphic_a_format = output_menu()
    new = graphic_a_format[:]
    new.remove(graphic_a_format[input_selection])
    subprocess.call(['clear'])
    print ('\n\n    The audio input files format is "%s" \n\n'
            '    Please, now type the output files format for '
            'encoding\n' % input_format)
    for outformat in new:
        print "    %s"%(outformat)
        
    output_selection = raw_input(
                '\n Type a letter for your encoding and just hit enter: ')
    main = Audio_Formats(input_format) # have a ext input
    b = main.output_selector(output_selection)
    output_format = b
    
    if output_selection == 'q' or output_selection == 'Q':
            sys.exit()
    elif output_format is None:
        sys.exit("\n\033[1mEntry error in select output format!\033[0m\n")

    bitrate_test(main.retcode[0], main.retcode[1], main.retcode[2], 
                 main.retcode[3], main.retcode[4], path_in, 'off', input_format)


def bitrate_test(command, dict_bitrate, graphic_bitrate, dialog, codec, path_in,
                 batch, input_format):
    """
    Check if codec has bitrate.
 
    just to remind me notified:

    dammi il valore di questa chiave: 
        command = main.retcode[0] 
    dammi il dizionario per il confronto del fattore di compressione:
        dict_bitrate = main.retcode[1]
    dammi il grafico del fattore compressione:
        graphic_bitrate = main.retcode[2]
    dialogo immissione fattore di compressione:
        dialog = main.retcode[3] 
    l'estensione finale dei files convertiti:
        codec = main.retcode[4]
    """
    if dict_bitrate is None:
        process_cli.Process_Conversion(path_in, command, None, batch, codec, 
                                        input_format)
    else:
        subprocess.call(['clear'])
        print graphic_bitrate
        level = raw_input(dialog)
        
        if level == 'c' or level == 'C':
                sys.exit()
        a = Audio_Formats(None)
        bitrate = a.quality_level(dict_bitrate, level)
        valid = bitrate
        
        if valid is False:
            sys.exit("\n\033[1m Error\033[0m, inexistent quality level\n")

        process_cli.Process_Conversion(path_in, command, bitrate, batch, 
                                        codec, input_format)
