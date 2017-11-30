 
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: process_file.py (module)
# Porpose: parsing data files controls.
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (Ver.0.7) Nov. 2017
# Rev.
#########################################################

import subprocess
import glob
import sys
import os
from audio_formats import Audio_Formats
from datastrings import input_menu, output_menu
from comparisions import a_formats

#lista dei formati con limiti di scelta nella conversioni
f_limit = ['mp3','ogg','ape']

def file_parser(input_format, path_name, path_O):
    """
    Redirect work flow on specific methods for single 
    audio file conversions. 
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

    if input_format in f_limit:
        indx = 2,3,4,5,6
        new = [ new[i] for i in xrange(len(new)) if i not in set(indx) ]
    else:
        new.remove(graphic_a_format[input_selection])
    #subprocess.call(['clear'])
    print ('\n    Available formats for '
              'encoding/decoding \033[32;1m%s\033[0m audio ' 
              'files' % input_format
            )
    for outformat in new:
        print "    %s"%(outformat)
        
    output_selection = raw_input(
                '    Type a letter for your encoding and just hit enter: ')
    main = Audio_Formats(input_format) # have a ext input
    b = main.output_selector(output_selection)
    output_format = b
    
    if output_selection == 'q' or output_selection == 'Q':
            sys.exit()
    elif output_format is None:
        sys.exit("\n\033[1mEntry error in select output format!\033[0m\n")
    
    bitrate_test(main.retcode[0], main.retcode[1], main.retcode[2], 
                 main.retcode[3], main.retcode[4], path_name, path_O, 
                 input_format)
    

def bitrate_test(command, dict_bitrate, graphic_bitrate, dialog, 
                 out_format, path_name, path_O, input_format):
    """
    Check if out_format has bitrate 
    
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
        out_format = main.retcode[4]
    """
    if dict_bitrate is None:
        bitrate = ''
    else:
        #subprocess.call(['clear'])
        print graphic_bitrate
        level = raw_input(dialog)

        a = Audio_Formats(None)
        bitrate = a.quality_level(dict_bitrate, level)
        valid = bitrate

        if valid is False:
            print ("\naudiomass:\033[1m Warning!\033[0m, inexistent "
                   "quality level '%s', ...use default\n" % level
                  )
            bitrate = ''

    stream_I = os.path.basename(path_name)#input, es: nome-canzone.wav'
    file_name = os.path.splitext(stream_I)[0]#only stream with no ext
    if path_O is None: # se non ce sys.argv[3]
        path_O = os.path.dirname(path_name)

    if os.path.exists('%s/%s.%s' % (path_O, file_name, out_format)):
        sys.exit("\naudiomass:\033[1m Warning!\033[0m Already exists > "
                       "'%s/%s.%s'" % (path_O, file_name, out_format))

    command_dict = {
'flac':"flac -V %s '%s' -o '%s/%s.%s'" % (bitrate, path_name, path_O,
                                          file_name, out_format),
'lame':'lame --nohist %s "%s" "%s/%s.%s"' % (bitrate, path_name, path_O,
                                             file_name, out_format),
'lame --decode':"lame --nohist --decode '%s' '%s/%s.%s'" % (path_name, path_O,
                                    file_name, out_format),
'oggenc':'oggenc %s "%s" -o "%s/%s.%s"' % (bitrate, path_name, path_O,
                                           file_name, out_format),
'mac':'mac "%s" "%s/%s.%s" %s' % (path_name, path_O, file_name, out_format,
                                  bitrate),
'ffmpeg':'ffmpeg -i "%s" %s "%s/%s.%s" ' % (path_name, bitrate, path_O,
                                            file_name, out_format),
'oggdec':"oggdec '%s' -o '%s/%s.%s'" % (path_name, path_O, file_name,
                                        out_format),
'shntool':"shntool conv -o %s '%s' -d '%s/%s'" % (out_format,  path_name,
                                                  path_O, file_name),
                            }
    try:
        print "\n\033[1mConvert '%s' to '%s'\033[0m\n" % (input_format, 
                                                          out_format)
        #print command_dict[command]# uncomment for debug
        subprocess.check_call(command_dict[command], shell=True)
    except subprocess.CalledProcessError as err:
        sys.exit("audiomass:\033[31;1m ERROR!\033[0m %s" % (err))
    else:
        print "\n\033[36;7mDone...\033[0m\n"

