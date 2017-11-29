 
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: getcommand.py (module)
# Porpose: parsing data directory and evaluate possible conditions.
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (Ver.0.7) Nov. 2017
#########################################################


import sys
import os
import process_cli
from audio_formats import Audio_Formats
from datastrings import input_menu, output_menu
from comparisions import a_formats

#lista dei formati con limiti di scelta nella conversioni
f_limit = ['mp3','ogg','ape']


def dir_(path_in):#================ WARNING: DIR
    """
    Redirect work flow on specific methods for audio files with same 
    format in a directory content for conversions
    """
    #subprocess.call(['clear'])
    input_menu()
    input_selection = raw_input("    Enter here the corresponding number "
                                "and hit enter... "
                                )
    main = Audio_Formats(None) # not have a ext input = None
    a = main.input_selector(input_selection, None) # let choice an input format
    input_format = a # return a input format string

    if input_selection == 'q' or input_selection == 'Q':
            sys.exit()
    elif input_format is None:
            sys.exit("\n\033[1mEntry error in select input format, exit!\033[0m")

    graphic_a_format = output_menu()
    new = graphic_a_format[:]
    
    if input_format in f_limit:

        indx = 3,4,5,6
        new = [ new[i] for i in xrange(len(new)) if i not in set(indx) ]
    else:
        new.remove(graphic_a_format[int(input_selection)])
    
    

    #subprocess.call(['clear'])
    print ('\n\   Available formats for '
              'encoding/decoding \033[32;1m%s\033[0m audio files' % input_format)

    for outformat in new:
        print "    %s"%(outformat)

    output_selection = raw_input(
                '    Type a letter for your encoding and just hit enter: ')
    b = main.output_selector(output_selection)
    output_format = b
    
    if output_selection == 'q' or output_selection == 'Q':
            sys.exit()
    elif output_format is None:
        sys.exit("\n\033[1mEntry error in select output format, exit!\033[0m")
        
    if main.retcode == 'KeyError':
        sys.exit("\nSorry, this conversion is not possible")

    bitrate_test(main.retcode[0], main.retcode[1], main.retcode[2], 
                main.retcode[3], main.retcode[4], path_in, 'dir', input_format)



###### WARNING area illesa ######
def bitrate_test(command, dict_bitrate, graphic_bitrate, dialog, codec, path_in,
                 type_proc, input_format):
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
        process_cli.Process_Conversion(path_in, command, None, type_proc, codec, 
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

        process_cli.Process_Conversion(path_in, command, bitrate, type_proc, 
                                        codec, input_format)
