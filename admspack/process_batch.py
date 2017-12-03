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
from comparisions import a_formats, output_menu

warnings = 'audiomass: \033[33;7;3mWarning!\033[0m'
errors = 'audiomass: \033[31;7;3mError!\033[0m'

def batch_parser(f_list, path_O):
    """
    1- removal of any duplicates in the list
    2- dictionary creation key = format: value = [filename, filename, etc] 
      in order to group the streams with the same format into separate lists 
    3- Creation input menu
    4- Creation output menu
    """
    ##########################RIMOZIONE DUPLICATI ########################
    # Clean-up list contaminated by duplicate files.
    for k,v in Counter(f_list).items():# controllo doppioni accidentali.
        if v>1:
            print "%s Removing following duplicates: > '%s' >" % (warnings, k)
    f_list = list(set(f_list)) # elimino eventuali doppioni
    """
    ##########################CREAZIONE DIZ ##############################
    The following block of code is for sorting input formats into 
    separate lists
    ORDINAZIONE SEPARATA IN LISTE PER CIASCUN FILE FORMAT.
    """
    formats = {}#Dizionario {formato1:[file1,file2,etc],..]}
    new_list = []#La lista ripulita dai file non supportati
    supported_formats = a_formats()#Chiamo la funzione su comparisions
    #Creazione keys (chiavi) nel diz. formats:
    for i in f_list: #Append separated file format
      name, ext = os.path.splitext(i)
      new = ext.replace(".","")#Tolgo il punto all'estensione
      if new in supported_formats[1]:#Se estensione input è supportata
        new_list.append(i)#Lista ripulita file importati
        if not formats.has_key(new):#Add not present key at dict
          formats[new] = [] #Aggiungo chiavi non presenti nel diz +
                            #valore lista vuota: {formato:[]}
      else:
        print '\n%s Not supported file format: "%s%s" >> skipping >>'% (
                                                    warnings,name,ext)
    if new_list == []: # se i file importati sono tutti incompatibili
      sys.exit('\n%s ...No audio streams to process, exit!' % errors)
    # Creazione dei records (valori) nel diz. formats
    for i in new_list:
      name, ext = os.path.splitext(i)
      new = ext.replace(".","")# tolgo il punto all'estensione
      formats[new].append("%s%s" %(name,ext))
      
    #####################CREAZIONE INPUT MENU ############################
    input_selection = []#Contiene solo interi(int)
    graphic_out_formats = output_menu()#Lista menu per i formati in uscita
    """
    indx: range che indica gli indici per i formati non supportati in 
    lista graphic_out_formats data da output_menu() solo per i formati definiti 
    in variabile f_limit, perche mp3, ogg, ape, is available decoding in 
    wav/aiff only:
    """
    f_limit = ['mp3','ogg','ape']
    indx = 2,3,4,5,6
    for input_format in formats.keys():#Itero sui formati importati
      """
      NOTE 1 RELOAD: ricarico nuovamente il grafico dei formati 
                    integralmente con l'originale 
      """
      new = graphic_out_formats[:] # RELOAD
      print ("\n    Available formats for encoding/decoding "
          "'\033[32;1m%s\033[0m' audio stream" % input_format)
      """
      Dizion. = {chiavi'srtinga 1':(integear,'formato')} 
      itero sulla tupla valori 
      """
      for v in supported_formats[0].values():
        if input_format in v:# mi prendo gli interi corrispondenti
          """
          input_selection contiene solo integear, che sono il primo elemento
          del valore tupla della chiave del dizionario 'supported_formats' 
          corrispondente al formato (vedi supported_formats in 
          comparisions.a_formats()
          """
          input_selection.append(v[0])# v[0] mi da l'intero
          if input_format in f_limit:
              new = [ new[i] for i in xrange(len(new)) if i not in set(indx) ]
          else:
              """
              NOTE 2 SET: qui con l'intero ottenuto rimuovo dalla lista
                          i formati che non sono trattati o incompatibili.
              """
              new.remove(graphic_out_formats[v[0]])# SET
          for outformat in new:# realizzazione menu di output
            print "    %s"%(outformat)
          output_selection = raw_input('    Choice a format by a letter '
                                        'and just hit enter: ')
          """
          NOTE 3 DELETE: cancello il grafico dei formati settati prima
                         altrimenti rimangono in memoria con gli elementi
                         cancellati
          """
          del new[:] # DELETE
          
          #####################CREAZIONE OUTPUT MENU #######################
          main = Audio_Formats(input_format)# Have a ext input >
          b = main.output_selector(output_selection)
          output_format = b
          print output_selection
          if output_selection == 'q' or output_selection == 'Q':
            sys.exit()
          elif output_format is None:
            print ("\n%s Entry error in selection output format, "
                     " %s >> skipping" % (warnings, output_selection))
            formats.pop(input_format, None)#Se nessuna selezione e premi enter rimuovo 
            #chiave e valore dal dizionario, cioè escludo quei files dalla
            #conversione.
            continue # meglio partire da capo 
          if main.retcode == 'KeyError':
            print ("\n%s Incompatible conversion >> skipping >>" % warnings)
            formats.pop(input_format, None)
            continue # troppi errori, meglio contimuare da capo

          if formats == {}:# se è completamente vuoto, esco
            sys.exit('\n%s...End selection process, exit!\n'% warnings)

          bitrate_test(main.retcode[0], main.retcode[1], 
                       main.retcode[2], main.retcode[3], 
                       main.retcode[4], formats.get(input_format), 
                       path_O, input_format)

#print '1---- %s' %(main.retcode[0])# comando, nome codificatore/decodificatore
#print '2----%s' % main.retcode[1]# dizionario quality usato dal prog
#print '3----%s' % main.retcode[2]# reference quality usato dallo user
#print '4----%s' % main.retcode[3]#stringa contestuale bit-rate di object_assignment diz. 
#print '5----%s' % main.retcode[4]# nome del formato in uscita
#print '6----%s' % formats.get(a)# percorso o filename (dai la lista)
#print '7----%s' % path_O # percorso salvataggio output stream
#print '8----%s' % a # formato dei file da convertire

def bitrate_test(command, dict_bitrate, graphic_bitrate, dialog, 
                 out_format, path_in, path_O, input_format):
    """
    Check if codec out_format has bitrate.
    Here in reality, it is only used: dict_bitrate, graphic_bitrate, 
    and dialog parameters.
 
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
        level = raw_input(dialog)

        a = Audio_Formats(None)
        bitrate = a.quality_level(dict_bitrate, level)
        valid = bitrate
        if valid is False:
            print ("\n%s inexistent quality level '%s', ...use default\n" % (
                warnings, level)
                    )
            bitrate = ''
            
    command_builder(command, bitrate, out_format, path_in, path_O, 
                    input_format)
    
#print command # comando impostato per conversione
#print dict_bitrate #  dizionario bit-rate
#print graphic_bitrate # grafico per scelta livello bit-rate
#print dialog # stringa usata per il contesto su level = raw_input(dialog)
#print out_format # formato di uscita
#print path_in # lista file da convertire
#print path_O # percorso salvataggio output stream
#print input_format # formato dei file da convertire

def command_builder(command, bitrate, out_format, path_in, path_O, 
                    input_formatt):
    """
    command_builder is based on construction of the paths and formats
    strings (out_format, path_in, path_O) and the 'command' variable, that 
    contains the key (codec) for an corresponding values used for process.
    """
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
'lame --decode':'ame --decode "%s" "%s/%s.%s"' % (path_name, path_O,
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
            #print command_dict[command]# uncomment for debug
            subprocess.check_call(command_dict[command], shell=True)
        except subprocess.CalledProcessError as err:
            sys.exit("audioamass:\033[31;1mERROR!\033[0m %s" % (err))
            
    print "\n\033[32;7mQueue Streams Processed:\033[0m >> %s\n" % (path_in)
    print "\n\033[37;7mDone...\033[0m\n"


