 
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: getcommand.py (module)
# Porpose: parsing data files and evaluate possible conditions.
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (Ver.0.7) Nov. 2017
# Rev.
#########################################################


import sys
import os
import process_cli
from audio_formats import Audio_Formats
from datastrings import input_menu, output_menu
from comparisions import a_formats


def file_(input_format, path_in):#================ WARNING: FILE
    """
    Redirect work flow on specific methods for single 
    audio file conversions
    """
    supported_formats = a_formats()
    input_selection = None
    
    for supp in supported_formats[0].values():
        if input_format in supp[1]:
            input_selection = supp[0]
    
    if input_selection is None:
        # the file-name must be supported and match with dict keys
        sys.exit('\nSorry, not format supported "%s"\nPlease, choice one of: '
        '%s\n' % (input_format, supported_formats[1]))

    graphic_a_format = output_menu()
    new = graphic_a_format[:]
    new.remove(graphic_a_format[input_selection])
    #subprocess.call(['clear'])
    print ('\n\n    Please, type the output audio format for '
              'encoding/decoding \033[32;1m%s\033[0m' % input_format)
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
    

###### WARNING area illesa ######
def bitrate_test(command, dict_bitrate, graphic_bitrate, dialog, codec, path_in,
                 batch, input_format):
    """
    Check if codec has bitrate 
    
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
