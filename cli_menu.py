#!/usr/bin/python
# -*- coding: UTF-8 -*-


import subprocess
import sys
from datastrings import *



class Appetite(object):
	"""
	interactive menu for command line interface (cli)
	in the selection audio input/output files format objects.
	Accept only audio input extension string or None
	"""
	
	def __init__(self, input_format):
		"""
		input_format arg is a true extension input audio string if 
		there is a single process (one audio track conversion). 
		Is None if batch file process (-b) arg. 
		"""
		
		self.input_format = input_format 
		
		self.retcode = None # return a data tuple
		
		
	def input_selector(self):
		"""
		The first dish is served with fresh music, notes of pasta with 
		tomato or meat sauce, or with the excellent Cuban salsa or flamenco.
		"""
		case = {'1':'wav', '2':'aiff', '3':'flac', '4':'ape', '5':'mp3',
				'6':'ogg',}
		
		subprocess.call(['clear'])
		
		main_menu()
		
		input_selection = raw_input("Enter here the corresponding number "
									"and hit enter... "
									)
		
		if input_selection in case.keys():
			
			self.input_format = case[input_selection]
			self.output_selector(int(input_selection))
			
		elif input_selection == 'q' or input_selection == 'Q':
			sys.exit()
			
		else:
			sys.exit("\n\033[1mEntry error in select input format!\033[0m\n")
			
		return self.input_format
		
		
		
	def output_selector(self, remove_this):
		"""
		Do you still hungry? There is a cake with a rock Hendrix wax. 
		But this depends on your diet, of course.
		"""
		case = {'a':'wav', 'A':'wav', 'b':'aiff','B':'aiff', 'c':'flac', 
				'C':'flac','d':'ape', 'D':'ape', 'e':'mp3', 'E':'mp3', 
				'f':'ogg', 'F':'ogg',
				}
		
		graphic_a_format = output_menu()
		self.new = graphic_a_format[:] # make a new list
		self.new.remove(graphic_a_format[remove_this]) # remove input format 
		
		subprocess.call(['clear'])

		print ('\n\n    The audio input files format is "%s" \n\n'
				'    Please, now type the output files format for '
				'encoding\n' % self.input_format)
		
		for outformat in self.new:
			print "    %s"%(outformat)
			
		output_selection = raw_input(
					'\n Type a letter for your encoding and just hit enter: ')
		
		if output_selection in case.keys():
			
			output_format = case[output_selection]
			
			self.diction_strings(self.input_format, output_format)
			
		elif output_selection == 'q' or output_selection == 'Q':
			
			sys.exit()
			
		else:
			
			sys.exit("\n\033[1mEntry error in select output format!\033[0m\n")
			
			
	def diction_strings(self, input_format, output_format):
		
		comparision = '%s > %s' % (input_format, output_format)

		self.retcode = dictionaries(comparision)
		
		
		
	def quality_level(self, dict_bitrate, graphic_bitrate, dialog):
		
		subprocess.call(['clear'])
		
		print graphic_bitrate
		
		level = raw_input(dialog)
		
		if level in dict_bitrate:
			
			return dict_bitrate[level]
		
		elif level == 'c' or level == 'C':
			
			sys.exit()
			
		else:
		
			sys.exit("\n\033[1m Error\033[0m, inexistent quality level\n")
			
