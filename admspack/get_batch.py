#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: getcommand.py (module)
# Porpose: parsing data in batch and evaluate possible conditions.
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (Ver.0.7) Nov 27 2017
# Rev
#########################################################


import sys
import os
import process_cli
from audio_formats import Audio_Formats
from datastrings import input_menu, output_menu
from comparisions import a_formats




def batch_(list_):#================ WARNING: BATCH
    """
    Redirect work flow on specific methods for batch conversions
    """
    formats = {}#Dizionario {formato1:[file1,file2,etc],..]}
    new_list = []#La lista ripulita dai file non supportati
    supported_formats = a_formats()#Chiamo la funzione su comparisions
    input_selection = []#Contiene solo interi(int) corrispondenti al formato

    # NOTE: BLOCCO DI ORDINAZIONE SEPARATA IN LISTE PER CIASCUN FILE EXTENSION
    #Creazione chiavi da aggiungere nel diz. formats:
    for i in list_: #Append separated file format
      name, ext = os.path.splitext(i)
      new = ext.replace(".","")#Tolgo il punto all'estensione
      if new in supported_formats[1]:#Se estensione input è supportata
        new_list.append(i)#Lista ripulita file importati
        if not formats.has_key(new):#Add not present key
          formats[new] = [] #Aggiungo chiavi non presenti nel diz +
                            #valore lista vuota: {formato:[]}
      else:
        print '\033[1mRemoving not supported file format>\033[0m "%s%s"'% (
                                                                  name,ext)

    if new_list == []: # se i file importati sono tutti incompatibili
      print '\n...No audio files to process, exit!\n'
      return
    
    # Aggiungo i records(valori) nel diz. formats
    for i in new_list:
      name, ext = os.path.splitext(i)
      new = ext.replace(".","")# tolgo il punto all'estensione
      formats[new].append("%s%s" %(name,ext))
      
    """input selection contiene solo integear, che sono il primo elemento
       del valore tupla della chiave del dizionario 'supported_formats' 
       corrispondente al formato (vedi supported_formats in 
       comparisions.a_formats()
    for a in formats.keys():
      for v in supported_formats[0].values():
        if a in v:
          input_selection.append(v[0])
        print v[1]
    """

    graphic_a_format = output_menu()#E' il menu per i formati in uscita

    for a in formats.keys():#Itero sui formati importati
      new = graphic_a_format[:]#NOTE RESET: ricarico nuovamente il grafico
                               #dei formati 
      print ('\n\n    Please, type the output audio format for '
              'encoding/decoding \033[32;1m%s\033[0m' % a)
      for v in supported_formats[0].values():#Dizion. = 
        #{chiavi'srtinga 1':(integear,'formato')} itero sulla tupla valori
        if a in v:# mi prendo gli interi corrispondenti
          """input selection contiene solo integear, che sono il primo elemento
             del valore tupla della chiave del dizionario 'supported_formats' 
             corrispondente al formato (vedi supported_formats in 
             comparisions.a_formats()
          """
          input_selection.append(v[0])# v[0] mi da l'intero
          new.remove(graphic_a_format[v[0]])#NOTE SET: con l'intero ottenuto 
          #rimuovo dalla lista i formati non trattati.
          for outformat in new:# realizzazione menu di output
            print "    %s"%(outformat)
          output_selection = raw_input(
                  '    Choice a format by a letter and just hit enter: ')
          del new[:]#NOTE CANCEL: cancello il grafico dei formati 
          
          main = Audio_Formats(a)# Have a (Pope :-) shit!) ext input >
          b = main.output_selector(output_selection)
          output_format = b
          if output_selection == 'q' or output_selection == 'Q':
            sys.exit()
          elif output_format is None:
            print ("\nWarning: Entry error in select output format! %s" % (
                                                         output_selection))
            formats.pop(a, None)#Se nessuna selezione e premi enter rimuovo 
            #chiave e valore dal dizionario, cioè escludo quei files dalla
            #conversione.
          if formats == {}:# se è completamente vuoto, esco
            sys.exit('...No selection for the conversion process, exit!\n')
          
          bitrate_test(main.retcode[0], main.retcode[1], main.retcode[2], 
                main.retcode[3], main.retcode[4], formats.get(a), 'off', a)
####### -----------------------------------------------------------------------
          #print '1---- %s' %(main.retcode[0])# comando, nome codificatore/decodificatore
          #print '2----%s' % main.retcode[1]# dizionario quality usato dal prog
          #print '3----%s' % main.retcode[2]# reference quality usato dallo user
          #print '4----%s' % main.retcode[3]#stringa contestuale di object_assignment diz. 
          #print '5----%s' % main.retcode[4]# nome del formato in uscita
          #print '6----%s' % formats.get(a)# percorso o filename (dai la lista)
          #print '7----%s' % 'off' # batch mode disabilitato
          #print '8----%s' % a # formato dei file da convertire
####### -----------------------------------------------------------------------
    #bitrate_test(main.retcode[0], main.retcode[1], main.retcode[2], 
                #main.retcode[3], main.retcode[4], path_in, 'off', input_format)
                
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
        print command
        print dict_bitrate
        print graphic_bitrate
        print dialog
        print codec
        print path_in
        print batch
        print input_format
        process_cli.Process_Conversion(path_in, command, None, batch, codec, 
                                        input_format)
    else:
        #subprocess.call(['clear'])
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
