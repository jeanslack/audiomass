#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: audio_formats.py (module)
# Porpose: module to pair audio formats
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (Ver.0.6) Febbruary 2015
# Rev
#########################################################

from comparisions import a_formats, comparision

class Audio_Formats(object):
    """
    interface for comparison audio formats in the conversion 
    processes where different libraries and codecs are used.
    """
    def __init__(self, input_format):
        """
        Can be accept one argument of type string or None values.
        If not None, Argument is the audio input extension string 
        without dot punctuation.  
        """
        self.input_format = input_format
        self.output_format = None
        self.retcode = None # return a data tuple

    def input_selector(self, input_selection):
        """
        Accept number string argument and return the corresponding 
        format or None. This method is related to the graphic input menu
        and from process_dir only. it is useful to limit the choices within 
        the available options of the graphic input menu.
        """

        supported_formats = a_formats()
        if supported_formats[0].has_key(input_selection):
            # mi da il formato:
            input_format = supported_formats[0][input_selection][1]
            self.input_format = input_format.lower()
        else:
            self.input_format = None
            return self.input_format
        return self.input_format

    def output_selector(self, output_selection):
        """
        looking for a comparison/compatibilities between the input 
        format and the output format.
        Accept letters string in corresponding with output menu. see the
        output_menu in comparisions module.
        """
        case = a_formats()

        if output_selection in case[2].keys():
            self.output_format = case[2][output_selection]
        else:
            #output_format = None
            return self.output_format
        return self.output_format

    def diction_strings(self,):
        """
        returns data for that pair input_format and output_format
        """
        pair = '%s > %s' % (self.input_format, self.output_format)

        if self.retcode == 'KeyError':
            self.retcode = comparision
        else:
            self.retcode = comparision(pair)
        return self.retcode

    def quality_level(self, dict_bitrate, level):
        """
        If audio codec support audio bitrate level, this method 
        define true or false and return a level of bitrate.
        """
        if level in dict_bitrate:
            valid = True
            return dict_bitrate[level]
        else:
            valid = False
            return valid
