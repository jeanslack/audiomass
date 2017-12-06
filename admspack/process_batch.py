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
from comparisions import a_formats, output_menu, build_cmd

warnings = 'audiomass: \033[33;7;3mWarning!\033[0m'
errors = 'audiomass: \033[31;7;3mError!\033[0m'

def batch_parser(f_list, path_O):
    """
    1- removal of any duplicates in the list
    2- dictionary creation key = format: value = [filename, filename, etc] 
      in order to group the streams with the same format into separate lists 
    3- Creation input menu
    4- Creation output menu
    During output menu creation, Get a tuple with specified command
    elements
    """
    ##########################  RIMOZIONE DUPLICATI
    # Clean-up list contaminated by duplicate files.
    for k,v in Counter(f_list).items():# controllo doppioni accidentali.
        if v>1:
            print "%s Removing following duplicates: > '%s' >" % (warnings, k)
    f_list = list(set(f_list)) # elimino eventuali doppioni
    """
    ##########################  CREAZIONE DIZ 
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


        if not formats.has_key(new.lower()):#Add not present key at dict
          formats[new.lower()] = [] #Aggiungo chiavi non presenti nel diz +
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
      formats[new.lower()].append("%s%s" %(name,ext))
      
    ##########################  CREAZIONE INPUT MENU 
    input_selection = []#Contiene solo interi(int)
    graphic_out_formats = output_menu()#Lista menu per i formati in uscita
    """
    indx: range che indica gli indici per i formati non supportati in 
    lista graphic_out_formats data da output_menu() solo per i formati definiti 
    in variabile f_limit, perche mp3, ogg, ape, is available decoding in 
    wav/aiff only:
    """
    f_limit = ['mp3','ogg','ape','MP3','OGG','APE']
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
          """NOTE 3 DELETE: cancello il grafico dei formati settati prima
            altrimenti rimangono in memoria con gli elementi gia rimossi"""
          del new[:] # DELETE
          
          ######################  CREAZIONE OUTPUT MENU 
          main = Audio_Formats(input_format)# Have a ext input >
          output_format = main.output_selector(output_selection)# get out format
          tuple_data = main.diction_strings()# return a tuple data of the codec
          if output_selection == 'q' or output_selection == 'Q':
            sys.exit()
          elif output_format is None:
            print ("\n%s Entry error in selection output format, "
                     " %s >> skipping" % (warnings, output_selection))
            formats.pop(input_format, None)#Se nessuna selezione e premi enter
            #rimuovo  chiave e valore dal dizionario, cioè escludo quei files
            #dalla conversione.
            continue # meglio partire da capo 
          if tuple_data == 'KeyError':
            print ("\n%s Incompatible conversion >> skipping >>" % warnings)
            formats.pop(input_format, None)
            continue # troppi errori, meglio contimuare da capo

          if formats == {}:# se è completamente vuoto, esco
            sys.exit('\n%s...End selection process, exit!\n'% warnings)

          bitrate_test(tuple_data, output_format, formats.get(input_format), 
                       path_O)

def bitrate_test(tuple_data, output_format, path_in, path_O):
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
        level = raw_input(contestual_text)
        a = Audio_Formats(None)
        bitrate = a.quality_level(dict_bitrate, level)
        valid = bitrate
        if valid is False:
            print ("\n%s inexistent quality level '%s', ...use default\n" % (
                warnings, level)
                    )
            bitrate = ''
    command_builder(tuple_data, bitrate, output_format, path_in, path_O)

def command_builder(tuple_data, bitrate, output_format, path_in, path_O):
    """
    command_builder build the command, with the options, the paths names, etc.
    The 'id_codec' variable, contains the key (codec) for an corresponding 
    value with command_dict.
    """
    id_codec = tuple_data[0] # as lame --decodec or oggenc, etc
    count = 0
    for path_name in path_in:
        stream_I = os.path.basename(path_name)#input, es: nome-canzone.wav'
        file_name = os.path.splitext(stream_I)[0]#only stream with no ext
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
            % (str(count),output_format, path_O, file_name, output_format))
        try:
            #print command # uncomment for debug
            subprocess.check_call(command, shell=True)
        except subprocess.CalledProcessError as err:
            sys.exit("audioamass:\033[31;1mERROR!\033[0m %s" % (err))
            
    print "\n\033[32;7mQueue Streams Processed:\033[0m >> %s\n" % (path_in)
    print "\n\033[37;7mDone...\033[0m\n"
