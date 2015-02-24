#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: cli_menu.py (module)
# Porpose:  module for commands assembly in the audio conversion formats
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015/2016 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (Ver.0.6) Febbruary 2015
# Rev
#########################################################


import subprocess
import sys
from datastrings import *



class Appetite(object):
	"""
	interactive menu for command line interface (cli)
	in the input/output audio selection files format objects.
	Accept only audio input extension string or None
	"""
	
	def __init__(self, input_format):
		"""
		accept input_format arg as audio extension string if 
		there is a single process (one audio track conversion). 
		Is None if batch file process (-b) arg. 
		"""
		
		self.input_format = input_format
		
		self.retcode = None # return a data tuple
		
		
	def input_selector(self, input_selection):
		"""
		evaluate the input key choose; return the attribute input_format
		and pass int number at the output_selection method
		"""
		case = {'1':'wav', '2':'aiff', '3':'flac', '4':'ape', '5':'mp3',
				'6':'ogg',}
		
		if input_selection in case.keys(): # keys sono numeri str
			
			self.input_format = case[input_selection] # mi da il formato
		
		else:
			self.input_format = None
			return self.input_format
		
		return self.input_format
		
		
		
	def output_selector(self, output_selection):
		"""
		Show a graphic audio formats list without the input format 
		for combine the user choice. This method can be called outside
		from this class with:
		exemple = Appetite(input_format) # must have a not empty ext input
		exemple.output_selector(int)
		
		when a output format is established, the pair of the formats is 
		sent to the method diction_strings
		"""
		case = {'a':'wav', 'A':'wav', 'b':'aiff','B':'aiff', 'c':'flac', 
				'C':'flac','d':'ape', 'D':'ape', 'e':'mp3', 'E':'mp3', 
				'f':'ogg', 'F':'ogg',
				}
		
		if output_selection in case.keys():
			
			output_format = case[output_selection]
			self.diction_strings(self.input_format, output_format)
			
		else:
			
			output_format = None
			return output_format
		
		return output_format
	
			
			
	def diction_strings(self, input_format, output_format):
		"""
		each pair of input and output audio formats here is 
		compared with a database (dictionary) from which returns 
		data for that pair
		"""
		comparision = '%s > %s' % (input_format, output_format)

		self.retcode = dictionaries(comparision)
		
		
		
	def quality_level(self, dict_bitrate, level):
		"""
		If audio codec support audio quality or bitrate, this method 
		return a level of bitrate.
		"""
		
		if level in dict_bitrate:
			
			valid = True
			
			return dict_bitrate[level]
			
		else:
			
			valid = False

			return valid
		
		
			
