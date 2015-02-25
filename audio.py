#!/usr/bin/python
# -*- coding: UTF-8 -*-
#

def batch():
	
	
	
	input_selection = raw_input('scegli un formato da 1 a 6')
	
	supported_formats = {'1': (1,'wav'), '2': (2,'aiff'), '3': (3,'flac'), '4': (4,'ape'), 
						'5': (5,'mp3'),'6': (6,'ogg')}


	lista = ['wav','aiff','flac','ape','mp3','ogg']
	
	if supported_formats.has_key(input_selection):
		
		#if input_selection in case.keys(): # keys sono numeri str
		output_selection = supported_formats[input_selection][0]	
		input_format = supported_formats[input_selection][1]
		
		print input_format
		print output_selection
		
		
		
def single():
	
	input_format = raw_input('scegli un formato da wav a ogg')
	input_selection = None
	
	supported_formats = {'1': (1,'wav'), '2': (2,'aiff'), '3': (3,'flac'), '4': (4,'ape'), 
						'5': (5,'mp3'),'6': (6,'ogg')}


	lista = ['wav','aiff','flac','ape','mp3','ogg']
	
	l = supported_formats.values()
	for n in l:
		if input_format in n[1]:
			input_selection = n[0]

	print input_format
	print input_selection
	
	#if input_format in l:
		#print 'si'
	
	
	
#	if supported_formats.has_key(input_selection):
		
#		#if input_selection in case.keys(): # keys sono numeri str
			
#		input_format = supported_formats[input_selection][1]
		
#		print input_selection
	

#batch()
single()
	
	




