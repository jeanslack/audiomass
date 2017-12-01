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
    Interface for combine audio formats in the conversion processes that 
    use different libraries .
    """
    def __init__(self, input_format):
        """
        Can be accept one argument of type strings or None values.

        Pass argument with audio input extension strings without dot, if 
        you have already chosen a single file (one audio track conversion). 

        Pass None if you want also select the input format for directory 
        file process. 
        """
        self.input_format = input_format
        self.retcode = None # return a data tuple


    def input_selector(self, input_selection):
        """
        evaluate the audio input extension strings for combine format; 
        return the attribute input_format for directory file conversions
        """
        supported_formats = a_formats()
        if supported_formats[0].has_key(input_selection):
            # mi da il formato:
            self.input_format = supported_formats[0][input_selection][1] 

        else:
            self.input_format = None
            return self.input_format
        return self.input_format


    def output_selector(self, output_selection):
        """
        looking for a comparison between the input format and the 
        output format.
        Accept integer only .
        when both formats are paired they are sent to the method 
        diction_strings
        """
        case = a_formats()
        if output_selection in case[2].keys():
            output_format = case[2][output_selection]
            self.diction_strings(self.input_format, output_format)
        else:
            output_format = None
            return output_format
        return output_format


    def diction_strings(self, input_format, output_format):
        """
        returns data for that pair input_format and output_format
        type_proc è un contrassegno file/dir o batch
        """
        pair = '%s > %s' % (input_format, output_format)

        if self.retcode == 'KeyError':
            self.retcode = comparision
        else:
            self.retcode = comparision(pair)
            


    def quality_level(self, dict_bitrate, level):
        """
        If audio codec support audio quality or bitrate, this method 
        return a level of bitrate.
        """
        print 'dict_bitrate  %s' % dict_bitrate
        print 'level  %s' % level
        if level in dict_bitrate:
            print 'SONO SU IF LEVEL'
            valid = True
            return dict_bitrate[level]
        else:
            print 'SONO SU ELSE LEVEL'
            valid = False
            return valid
