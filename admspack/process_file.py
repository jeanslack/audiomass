 
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
from comparisions import a_formats, output_menu

warnings = 'audiomass: \033[33;7;3mWarning!\033[0m'
errors = 'audiomass: \033[31;7;3mError!\033[0m'

#lista dei formati con limiti di scelta nella conversioni
f_limit = ['mp3','ogg','ape','MP3','OGG','APE']

def file_parser(input_format, path_name, path_O):
    """
    1 - Get the input filename format
    2 - Creation output menu
    During output menu creation, Get a tuple with specified command
    elements
    """
    supported_formats = a_formats()
    input_selection = None
    
    for supp in supported_formats[0].values():
        if input_format in supp[1]:
            input_selection = supp[0]
    
    if input_selection is None:
        # the file-name must be supported and match with dict keys
        sys.exit('\n%s Not format supported "%s"\nPlease, choice one of: '
        '%s\n' % (errors, input_format, supported_formats[1]))

    graphic_out_formats = output_menu()
    new = graphic_out_formats[:]

    if input_format in f_limit:
        indx = 2,3,4,5,6
        new = [ new[i] for i in xrange(len(new)) if i not in set(indx) ]
    else:
        new.remove(graphic_out_formats[input_selection])
    #subprocess.call(['clear'])
    print ("\n    Available formats for "
              "encoding/decoding '\033[32;1m%s\033[0m' audio " 
              "stream" % input_format.lower()
            )
    for outformat in new:
        print "    %s"%(outformat)
        
    output_selection = raw_input('    Type a letter for your encoding '
                                    'and just hit enter: '
                                    )
    main = Audio_Formats(input_format.lower())# Have a ext input >
    output_format = main.output_selector(output_selection)# get out format
    tuple_data = main.diction_strings()# return a tuple data of the codec
    
    if output_selection == 'q' or output_selection == 'Q':
            sys.exit()
    elif output_format is None:
        sys.exit("\n%s Entry error in select output format!\n" % errors)
    if tuple_data == 'KeyError':
        sys.exit("\n%s Incompatible conversion" % errors)

    bitrate_test(tuple_data, output_format, path_name, path_O)

def bitrate_test(tuple_data, output_format, path_name, path_O):
    """
    Check if codec support bitrate for level compression.
    
    """
    dict_bitrate = tuple_data[1] # a dictionary of corresponding bitrate values
    graphic_bitrate = tuple_data[2]# a list with strings for graphic of choice
    contestual_text = tuple_data[3]# 'please, select a bitrate value'
    #output_format = tuple_data[4] # non serve, gia definito
    if dict_bitrate is None:
        bitrate = ''
    else:
        #subprocess.call(['clear'])
        print graphic_bitrate
        level = raw_input(contestual_text)

        a = Audio_Formats(None)
        bitrate = a.quality_level(dict_bitrate, level)
        valid = bitrate

        if valid is False:
            print ("\n%s Inexistent quality level '%s', "
                   "...use default\n" % (warnings, level)
                   )
            bitrate = ''

    command_builder(tuple_data, bitrate, output_format, path_name, path_O)
            
def command_builder(tuple_data, bitrate, output_format, path_name, path_O):
    """
    command_builder build the command, with the options, the paths names, etc.
    The 'id_codec' variable, contains the key (codec) for an corresponding 
    value with command_dict.
    """
    id_codec = tuple_data[0] # as lame --decodec or oggenc, etc
    stream_I = os.path.basename(path_name)#input, es: nome-canzone.wav'
    file_name = os.path.splitext(stream_I)[0]#only stream with no ext
    if path_O is None: # se non ce sys.argv[3]
        path_O = os.path.dirname(path_name)

    if os.path.exists('%s/%s.%s' % (path_O, file_name, output_format)):
        sys.exit("\n%s Already exists > '%s/%s.%s'" % (
                                errors, path_O, file_name, output_format))

    command_dict = {
'flac':'flac -V %s "%s" -o "%s/%s.%s"' % (bitrate, path_name, path_O,
                                        file_name, output_format),
'lame':'lame --nohist %s "%s" "%s/%s.%s"' % (bitrate, path_name, path_O,
                                file_name, output_format),
'lame --decode':'lame --decode "%s" "%s/%s.%s"' % (path_name, path_O,
                                file_name, output_format),
'oggenc':'oggenc %s "%s" -o "%s/%s.%s"' % (bitrate, path_name, path_O,
                                        file_name, output_format),
'mac':'mac "%s" "%s/%s.%s" %s' % (path_name, path_O, file_name, output_format,
                                bitrate),
'ffmpeg':'ffmpeg -i "%s" %s "%s/%s.%s"' % (path_name, bitrate, path_O,
                                        file_name, output_format),
'oggdec':'oggdec "%s" -o "%s/%s.%s"' % (path_name, path_O, file_name,
                                    output_format),
'shntool':'shntool conv -o %s "%s" -d "%s"' % (output_format, path_name, path_O),
                        }
    try:
        print ("\n\033[36;7m %s Output Stream:\033[0m >> '%s/%s.%s'\n" 
                % (output_format, path_O, file_name, output_format))
        #print command_dict[id_codec]# uncomment for debug
        subprocess.check_call(command_dict[id_codec], shell=True)
    except subprocess.CalledProcessError as err:
        sys.exit("audiomass:\033[31;1m ERROR!\033[0m %s" % (err))
    else:
        print "\n\033[37;7mDone...\033[0m\n"

