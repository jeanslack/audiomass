# -*- coding: utf-8 -*-
"""
Name:      audio_formats.py (module)
Porpose:   module to pair audio formats
Writer:    Gianluca Pernigoto <jeanlucperni@gmail.com>
Copyright: (c) Gianluca Pernigoto <jeanlucperni@gmail.com>
license:   GPL3
Rev        Dec 09 2021
Code checker: flake8,
              pylint --ignore R0201
"""
from audiomass.comparisions import supported_formats, comparing


class AudioFormats():
    """
    interface for comparing audio formats in conversion
    processes where different libraries and codecs are used.

    """
    def __init__(self, input_format):
        """
        Can be accept one argument of type string or None values.
        If not None, Argument is the audio input extension string
        without dot char .

        """
        self.input_format = input_format
        self.output_format = None
        self.retcode = None  # return a data tuple

    def input_selector(self, input_selection):
        """
        Accept number string argument and return the corresponding
        format or None. This method is related to the graphic input menu
        and from process_dir only. it is useful to limit the choices within
        the available options of the graphic input menu.

        """
        if input_selection in supported_formats():
            # mi da il formato lower case:
            self.input_format = supported_formats()[input_selection][2]
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
        try:
            selection = int(output_selection)
        except ValueError:
            return self.output_format  # None

        if selection in supported_formats():
            # get lower case str(audio format):
            self.output_format = supported_formats().get(selection)[1]
        else:
            return self.output_format  # None
        return self.output_format

    def pairing_formats(self,):
        """
        returns data for that pair input_format and output_format

        """
        pair = f'{self.input_format} > {self.output_format}'

        if self.retcode == 'key_error':
            self.retcode = comparing
        else:
            self.retcode = comparing(pair)
        return self.retcode

    def quality_level(self, dict_bitrate, level):
        """
        If audio codec supports audio bitrate level, this method
        define true or false and return a level of bitrate.

        """
        if level in dict_bitrate:
            return dict_bitrate[level]

        return False
