#!/usr/bin/python
# -*- coding: UTF-8 -*-



import subprocess
import sys
import os
import command_obj
from audio_formats import Audio_Formats
#from datastrings import usage, copying
from datastrings import *



def multiple_process(path_in):
	
	subprocess.call(['clear'])
		
	main_menu()
		
	input_selection = raw_input("Enter here the corresponding number "
								"and hit enter... "
								)
	
	main = Audio_Formats(None) # not have a ext input = None
	a = main.input_selector(input_selection) # let choice an input format
	input_format = a # return a input format string
	
	if input_selection == 'q' or input_selection == 'Q':
			sys.exit()
	
	elif input_format == None:
			sys.exit("\n\033[1mEntry error in select input format!\033[0m\n")
			
			
			
	graphic_a_format = output_menu()
	new = graphic_a_format[:] # make a new list
	new.remove(graphic_a_format[int(input_selection)]) # remove input format
	 
	
	subprocess.call(['clear'])

	print ('\n\n    The audio input files format is "%s" \n\n'
			'    Please, now type the output files format for '
			'encoding\n' % input_format)
	
	for outformat in new:
		print "    %s"%(outformat)
		
	output_selection = raw_input(
				'\n Type a letter for your encoding and just hit enter: ')
	
	b = main.output_selector(output_selection)
	output_format = b
	
	if output_selection == 'q' or output_selection == 'Q':
			
			sys.exit()
			
	elif output_format == None:
		sys.exit("\n\033[1mEntry error in select output format!\033[0m\n")
		
		
	vaiBit(main.retcode[0], main.retcode[1], main.retcode[2], main.retcode[3], 
			main.retcode[4], path_in, 'on', input_format)
		
	
		
		
def single_process(input_format, path_in):
	
	supported_formats = a_formats()
	input_selection = None
	
	for support in supported_formats[0].values():
		if input_format in support[1]:
			input_selection = support[0]
	
	if input_selection == None:
		# the file-name must be supported and match with dict keys
		sys.exit('\nSorry, not format supported "%s"\nPlease, choice one of: '
		   '%s\n' % (input_format, supported_formats[1]))

	graphic_a_format = output_menu()
	new = graphic_a_format[:] # make a new list
	new.remove(graphic_a_format[input_selection]) # remove input format
	 
	
	subprocess.call(['clear'])

	print ('\n\n    The audio input files format is "%s" \n\n'
			'    Please, now type the output files format for '
			'encoding\n' % input_format)
	
	for outformat in new:
		print "    %s"%(outformat)
		
	output_selection = raw_input(
				'\n Type a letter for your encoding and just hit enter: ')
	
	main = Audio_Formats(input_format) # have a ext input
	b = main.output_selector(output_selection)
	output_format = b
	
	if output_selection == 'q' or output_selection == 'Q':
			
			sys.exit()
			
	elif output_format == None:
		sys.exit("\n\033[1mEntry error in select output format!\033[0m\n")
		
	
	vaiBit(main.retcode[0], main.retcode[1], main.retcode[2], main.retcode[3], 
			main.retcode[4], path_in, 'off', input_format)
	
	
	
	
def vaiBit(command, dict_bitrate, graphic_bitrate, dialog, codec, path_in,
		   batch, input_format):
	# TEST
	#- dammi il valore di questa chiave: 
		#command = main.retcode[0] 
		
	#- dammi il dizionario per il confronto del fattore di compressione:
		#dict_bitrate = main.retcode[1]
		
	#-dammi il grafico del fattore compressione:
		#graphic_bitrate = main.retcode[2]
		
	#dialogo immissione fattore di compressione:
		#dialog = main.retcode[3] 
		
	#-l'estensione finale dei files convertiti:
		#codec = main.retcode[4]
	
	#print command
	#print dict_bitrate
	#print graphic_bitrate
	#print dialog
	#print codec

	if dict_bitrate == None:
		
		command_obj.Process_Conversion(path_in, command, None, batch, codec, 
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
		
		if valid == False:
			
			sys.exit("\n\033[1m Error\033[0m, inexistent quality level\n")

		#print path_in
		#print command
		#print bitrate
		#print batch
		#print codec
		#print input_format

		command_obj.Process_Conversion(path_in, command, bitrate, batch, 
										codec, input_format)
