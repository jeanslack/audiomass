# -*- coding: UTF-8 -*-
#
#########################################################
# Name: getcommand.py (module)
# Porpose: parsing data directory content.
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (Ver.0.7) Nov. 2017
#########################################################
import subprocess
import glob
import sys
import os
from audio_formats import Audio_Formats
from comparisions import graphic_menu, build_cmd

warnings = 'audiomass: \033[33;7;3mWarning!\033[0m'
errors = 'audiomass: \033[31;7;3mError!\033[0m'

#lista dei formati con limiti di scelta nella conversioni
f_limit = ['mp3','ogg','ape','MP3','OGG','APE']

def dir_parser(path_I, path_O):
    """
    1 - Show input menu for files input format choice
    2 - Creation output menu
    During output menu creation, Get a tuple with specified command
    elements
    """
    print('    Select the audio input file format in your directory:')
    for inputformat in graphic_menu():# realizzazione menu di output
                    print "    %s"%(inputformat)

    input_selection = raw_input("    Enter here the corresponding number "
                                "and hit enter... "
                                )
    main = Audio_Formats(None) # not have a ext input = None
    input_format = main.input_selector(input_selection) # return a input format string
    if input_selection == 'a' or input_selection == 'A':
            print('audiomass: \033[1mAbort!\033[0m')
            sys.exit()
    elif input_format is None:
            sys.exit("\n%s Entry error in select input format, exit!" % errors)
    graphic_out_formats = graphic_menu()
    new = graphic_out_formats[:]
    if input_format in f_limit:
        indx = 2,3,4,5,6
        new = [ new[i] for i in range(len(new)) if i not in set(indx) ]
    else:
        new.remove(graphic_out_formats[int(input_selection)])
    print ("\n    Available formats for encoding/decoding "
            "'\033[32;1m%s\033[0m' audio stream" % input_format)
    for outformat in new:
        print "    %s"%(outformat)
    output_selection = raw_input("    Enter here the corresponding number "
                                "and hit enter... "
                                    )
    output_format = main.output_selector(output_selection)
    tuple_data = main.pairing_formats()# return a tuple data of the codec

    if output_selection == 'a' or output_selection == 'A':
            print('audiomass: \033[1mAbort!\033[0m')
            sys.exit()
    elif output_format is None:
        sys.exit("\n%s Entry error in select output format, exit!" % errors)
    if tuple_data == 'KeyError':
        sys.exit("\n%s Incompatible conversion" % errors)

    bitrate_test(tuple_data, output_format, path_I, path_O, input_format)

def bitrate_test(tuple_data, output_format, path_I, path_O, input_format):
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
        print graphic_bitrate
        level = raw_input('%s' % contestual_text)

        a = Audio_Formats(None)
        bitrate = a.quality_level(dict_bitrate, level)
        valid = bitrate

        if valid is False:
            print ("\n%s inexistent quality level '%s', "
                   "...use default\n" % (warnings, level)
                   )
            bitrate = ''
            
    command_builder(tuple_data, bitrate, output_format, path_I, 
                                        path_O, input_format)

def command_builder(tuple_data, bitrate, output_format, path_I, 
                                        path_O, input_format):
    """
    command_builder is based on construction of the paths and formats
    strings (output_format, path_in, path_O) and the 'command' variable, that 
    contains the key (codec) for an corresponding values used for process.
    
    WARNING : path_I e path_O devono rappresentare solo il nome dei percorsi
    file_name = 'only stream with no ext, es: nome_canzone'
    path_name = 'complete path input: /dir/dir/filename.ext'
    stream_I = 'Nome dello stream di input, es: nome-canzone.wav'
    stream_O = 'Nome dello stream di output, es: nome-canzone.flac'
    path_I = '/home/Musica solo input dir-name'
    path_O = '/dir/dir solo output dir-name'
    """
    id_codec = tuple_data[0] # as lame --decodec or oggenc, etc
    exe = 'False'
    count = 0
    for upper_lower_name in [input_format, input_format.upper()]:
        # itero su nomi formato upper-case e lower-case
        for path_name in glob.glob("%s/*.%s" % (path_I, upper_lower_name)):
            stream_I = os.path.basename(path_name)
            file_name = os.path.splitext(stream_I)[0]
            exe = None
            count += 1
            if path_O is None: # se non ce sys.argv[3]
                path_O = os.path.dirname(path_name)
            if os.path.exists('%s/%s.%s' % (path_O, file_name, output_format)):
                print ("\n%s Already exists > '%s/%s.%s' >> skipping >>" % (
                        warnings, path_O, file_name, output_format)
                        )
                continue
            
            command = build_cmd(id_codec, bitrate, path_name, 
                            path_O, file_name, output_format)
            print ("\n\033[36;7m|%s| %s Output Stream:\033[0m >> '%s/%s.%s'\n" 
                    % (str(count),output_format, path_O, file_name, 
                       output_format))
            try:
                #print command # uncomment for debug
                subprocess.check_call(command, shell=True)
                    
            except subprocess.CalledProcessError as err:
                sys.exit("audiomass:\033[31;1m ERROR!\033[0m %s" % (err))
        
    if exe == 'False':
            sys.exit("\n%s Files missing: No files '%s' "
                "in '%s' \n" % (errors, input_format, path_I)
                        )
    print "\n\033[37;7mDone...\033[0m\n"


