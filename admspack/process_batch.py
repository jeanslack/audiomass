#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: getcommand.py (module)
# Porpose: parsing the data files list for batch process.
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (Ver.0.7) Nov 27 2017
# Rev
#########################################################

import subprocess
import sys
import os
from collections import Counter
from audio_formats import Audio_Formats
from datastrings import input_menu, output_menu
from comparisions import a_formats

warnings = 'audiomass:\033[1m Warning!\033[0m'
errors = 'audiomass:\033[31;1m Error!\033[0m'

def batch_parser(f_list, path_O):
    """
    Redirect work flow on specific methods for batch conversions
    """
    formats = {}#Dizionario {formato1:[file1,file2,etc],..]}
    new_list = []#La lista ripulita dai file non supportati
    supported_formats = a_formats()#Chiamo la funzione su comparisions
    input_selection = []#Contiene solo interi(int) corrispondenti al formato
    #  mp3, ogg, ape, is available decoding in wav, aiff only
    f_limit = ['mp3','ogg','ape']
    #range che esclude indici in lista in datastrings.py graphic_a_format
    # per i formati in f_limit
    indx = 2,3,4,5,6 

    for k,v in Counter(f_list).items():# controllo se ci sono doppioni accidentali.
        if v>1:
            print "%s Removing following duplicates: > '%s' >" % (warnings, k)
    f_list = list(set(f_list)) # elimino eventuali doppioni

    # NOTE: BLOCCO DI ORDINAZIONE SEPARATA IN LISTE PER CIASCUN FILE EXTENSION
    #Creazione chiavi da aggiungere nel diz. formats:
    for i in f_list: #Append separated file format
      name, ext = os.path.splitext(i)
      new = ext.replace(".","")#Tolgo il punto all'estensione
      if new in supported_formats[1]:#Se estensione input è supportata
        new_list.append(i)#Lista ripulita file importati
        if not formats.has_key(new):#Add not present key
          formats[new] = [] #Aggiungo chiavi non presenti nel diz +
                            #valore lista vuota: {formato:[]}
      else:
        print '%s Removing not supported file format > "%s%s"'% (warnings,
                                                                name,ext)

    if new_list == []: # se i file importati sono tutti incompatibili
      sys.exit('audiomass: ...No audio files to process, exit!')
    # Aggiungo i records(valori) nel diz. formats
    for i in new_list:
      name, ext = os.path.splitext(i)
      new = ext.replace(".","")# tolgo il punto all'estensione
      formats[new].append("%s%s" %(name,ext))

    graphic_a_format = output_menu()#E' il menu per i formati in uscita

    for a in formats.keys():#Itero sui formati importati
      new = graphic_a_format[:]#NOTE RESET: ricarico nuovamente il grafico
                               #dei formati integralmente 
      print ("\n    Available formats for encoding/decoding "
          "'\033[32;1m%s\033[0m' audio stream" % a)
      for v in supported_formats[0].values():#Dizion. = 
        #{chiavi'srtinga 1':(integear,'formato')} itero sulla tupla valori
        if a in v:# mi prendo gli interi corrispondenti
          """input selection contiene solo integear, che sono il primo elemento
             del valore tupla della chiave del dizionario 'supported_formats' 
             corrispondente al formato (vedi supported_formats in 
             comparisions.a_formats()
          """
          input_selection.append(v[0])# v[0] mi da l'intero
          if a in f_limit:
              new = [ new[i] for i in xrange(len(new)) if i not in set(indx) ]
          else:
              """
              SET: con l'intero ottenuto rimuovo dalla lista i formati 
              non trattati.
              """
              new.remove(graphic_a_format[v[0]])#NOTE SET
          for outformat in new:# realizzazione menu di output
            print "    %s"%(outformat)
          output_selection = raw_input('    Choice a format by a letter '
                                        'and just hit enter: ')
          del new[:]#NOTE CANCEL: cancello il grafico dei formati 
          
          main = Audio_Formats(a)# Have a (Pope :-) shit!) ext input >
          b = main.output_selector(output_selection)
          output_format = b
          if output_selection == 'q' or output_selection == 'Q':
            sys.exit()
          elif output_format is None:
            print ("\n%s Entry error in selection output format, "
                     " %s >> skipping" % (warnings, output_selection))
            formats.pop(a, None)#Se nessuna selezione e premi enter rimuovo 
            #chiave e valore dal dizionario, cioè escludo quei files dalla
            #conversione.
            continue # meglio partire da capo 
          if main.retcode == 'KeyError':
            print ("\n%s Incompatible conversion >> skipping >>" % warnings)
            formats.pop(a, None)
            continue # troppi errori, meglio contimuare da capo

          if formats == {}:# se è completamente vuoto, esco
            sys.exit('\n%s...End selection process, exit!\n'% warnings)

          bitrate_test(main.retcode[0], main.retcode[1], main.retcode[2], 
                main.retcode[3], main.retcode[4], formats.get(a), path_O, a)
          
          
####### -----------------------------------------------------------------------
          #print '1---- %s' %(main.retcode[0])# comando, nome codificatore/decodificatore
          #print '2----%s' % main.retcode[1]# dizionario quality usato dal prog
          #print '3----%s' % main.retcode[2]# reference quality usato dallo user
          #print '4----%s' % main.retcode[3]#stringa contestuale bit-rate di object_assignment diz. 
          #print '5----%s' % main.retcode[4]# nome del formato in uscita
          #print '6----%s' % formats.get(a)# percorso o filename (dai la lista)
          #print '7----%s' % path_O # percorso salvataggio output stream
          #print '8----%s' % a # formato dei file da convertire
####### -----------------------------------------------------------------------
                
def bitrate_test(command, dict_bitrate, graphic_bitrate, dialog, 
                 out_format, path_in, path_O, input_format):
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
    #print command # comando impostato per conversione
    #print dict_bitrate #  dizionario bit-rate
    #print graphic_bitrate # grafico per scelta livello bit-rate
    #print dialog # stringa usata per il contesto su level = raw_input(dialog)
    #print out_format # formato di uscita
    #print path_in # lista file da convertire
    #print path_O # percorso salvataggio output stream
    #print input_format # formato dei file da convertire
        
    #file_list = ("'  '".join(path_in))
    if dict_bitrate is None:
        bitrate = ''
    else:
        print graphic_bitrate
        level = raw_input(dialog)

        a = Audio_Formats(None)
        bitrate = a.quality_level(dict_bitrate, level)
        valid = bitrate
        if valid is False:
            print ("\n%s inexistent quality level '%s', ...use default\n" % (
                warnings, level)
                    )
            bitrate = ''
            
    exe = 'False'
    count = 0
    for path_name in path_in:
        stream_I = os.path.basename(path_name)#input, es: nome-canzone.wav'
        file_name = os.path.splitext(stream_I)[0]#only stream with no ext
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
        print ("\n\033[36;7m |%s| %s Output Stream:\033[0m >> '%s/%s.%s'\n" 
                    % (str(count),out_format, path_O, file_name, out_format))
        try:
            print command_dict[command]# uncomment for debug
            #subprocess.check_call(command_dict[command], shell=True)
        except subprocess.CalledProcessError as err:
            sys.exit("audioamass:\033[31;1mERROR!\033[0m %s" % (err))
            
    print "\n\033[32;7mQueue Streams Processed:\033[0m >> %s\n" % (path_in)
    print "\n\033[37;7mDone...\033[0m\n"


