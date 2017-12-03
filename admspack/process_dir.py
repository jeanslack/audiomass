 
#!/usr/bin/python
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
from comparisions import a_formats, input_menu, output_menu

warnings = 'audiomass: \033[33;7;3mWarning!\033[0m'
errors = 'audiomass: \033[31;7;3mError!\033[0m'

#lista dei formati con limiti di scelta nella conversioni
f_limit = ['mp3','ogg','ape']

def dir_parser(path_I, path_O):
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
    a = main.input_selector(input_selection) # let choice an input format
    input_format = a # return a input format string

    if input_selection == 'q' or input_selection == 'Q':
            sys.exit()
    elif input_format is None:
            sys.exit("\n%s Entry error in select input format, exit!" % errors)

    graphic_out_formats = output_menu()
    new = graphic_out_formats[:]
    
    if input_format in f_limit:

        indx = 2,3,4,5,6
        new = [ new[i] for i in xrange(len(new)) if i not in set(indx) ]
    else:
        new.remove(graphic_out_formats[int(input_selection)])


    print ("\n    Available formats for encoding/decoding "
            "'\033[32;1m%s\033[0m' audio stream" % input_format)

    for outformat in new:
        print "    %s"%(outformat)

    output_selection = raw_input('    Type a letter for your encoding '
                                    'and just hit enter: '
                                    )
    b = main.output_selector(output_selection)
    output_format = b
    
    if output_selection == 'q' or output_selection == 'Q':
            sys.exit()
    elif output_format is None:
        sys.exit("\n%s Entry error in select output format, exit!" % errors)
        
    if main.retcode == 'KeyError':
        sys.exit("\n%s Incompatible conversion" % errors)

    bitrate_test(main.retcode[0], main.retcode[1], main.retcode[2],
                main.retcode[3], main.retcode[4], path_I, path_O, 
                input_format)


def bitrate_test(command, dict_bitrate, graphic_bitrate, dialog, 
                 out_format, path_I, path_O, input_format):
    """
    Check if out_format has bitrate.
 
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
        print graphic_bitrate
        level = raw_input('%s' % dialog)

        a = Audio_Formats(None)
        bitrate = a.quality_level(dict_bitrate, level)
        valid = bitrate

        if valid is False:
            print ("\n%s inexistent quality level '%s', "
                   "...use default\n" % (warnings, level)
                   )
            bitrate = ''
            
    command_builder(command, bitrate, out_format, path_I, path_O, 
                    input_format)
        
#print command # comando impostato per conversione
#print dict_bitrate #  dizionario bit-rate
#print graphic_bitrate # grafico per scelta livello bit-rate
#print dialog # stringa usata per il contesto su level = raw_input(dialog)
#print out_format # formato di uscita
#print path_name # lista file da convertire
#print path_O # percorso salvataggio output stream
#print input_format # formato dei file da convertire (variabile non usata)
            
def command_builder(command, bitrate, out_format, path_I, path_O, 
                    input_format):
    """
    command_builder is based on construction of the paths and formats
    strings (out_format, path_in, path_O) and the 'command' variable, that 
    contains the key (codec) for an corresponding values used for process.
    
    WARNING : path_I e path_O devono rappresentare solo il nome dei percorsi
    file_name = 'only stream with no ext, es: nome_canzone'
    path_name = 'complete path input: /dir/dir/filename.ext'
    stream_I = 'Nome dello stream di input, es: nome-canzone.wav'
    stream_O = 'Nome dello stream di output, es: nome-canzone.flac'
    path_I = '/home/Musica solo input dir-name'
    path_O = '/dir/dir solo output dir-name'
    """
    exe = 'False'
    count = 0
        # nome del singolo file completo
    for path_name in glob.glob("%s/*.%s" % (path_I, input_format)): 
        stream_I = os.path.basename(path_name)
        file_name = os.path.splitext(stream_I)[0]
        exe = None
        count += 1
        if path_O is None: # se non ce sys.argv[3]
            path_O = os.path.dirname(path_name)
        if os.path.exists('%s/%s.%s' % (path_O, file_name, out_format)):
            print ("\n%s Already exists > '%s/%s.%s' >> skipping >>" % (
                    warnings, path_O, file_name, out_format)
                    )
            continue

        command_dict = {
'flac':'flac -V %s "%s" -o "%s/%s.%s"' % (bitrate, path_name, path_O,
                                        file_name, out_format),
'lame':'lame --nohist %s "%s" "%s/%s.%s"' % (bitrate, path_name, path_O,
                                file_name, out_format),
'lame --decode':'lame --decode "%s" "%s/%s.%s"' % (path_name, path_O,
                                file_name, out_format),
'oggenc':'oggenc %s "%s" -o "%s/%s.%s"' % (bitrate, path_name, path_O,
                                        file_name, out_format),
'mac':'mac "%s" "%s/%s.%s" %s' % (path_name, path_O, file_name, out_format,
                                bitrate),
'ffmpeg':'ffmpeg -i "%s" %s "%s/%s.%s"' % (path_name, bitrate, path_O,
                                        file_name, out_format),
'oggdec':'oggdec "%s" -o "%s/%s.%s"' % (path_name, path_O, file_name,
                                    out_format),
'shntool':'shntool conv -o %s "%s" -d "%s"' % (out_format, path_name, path_O),
                        }
        print ("\n\033[36;7m|%s| %s Output Stream:\033[0m >> '%s/%s.%s'\n" 
                % (str(count),out_format, path_O, file_name, out_format))
        try:
            #print command_dict[command] # uncomment for debug
            subprocess.check_call(command_dict[command], shell=True)
                
        except subprocess.CalledProcessError as err:
            sys.exit("audiomass:\033[31;1m ERROR!\033[0m %s" % (err))

    print "\n\033[37;7mDone...\033[0m\n"


