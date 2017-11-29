#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: comparisions.py (module)
# Porpose:  module for output strings commands and formats comparisions
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015/2016 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (Ver.0.6) Febbruary 2015
# Rev
#########################################################


def comparision_b(pair):
  """
  returns the required values for each pair of audio formats. 
  Accept one only string argument in this form: 'exemple > exemple'.
  You can add or remove new formats modules from here.
  """
  
  flac_options = ("\n\033[1m"
              "References on quality for Flac format:\033[0m\n"
              "  0 = low compression > more access space > better quality\n"
              "  1\n"
              "  2\n"
              "  3\n"
              "  4 = Great quality/compression ratio\n"
              "  5 = Is the default compression \n"
              "  6\n"
              "  7\n"
              "  8 = maximum compression > less space > lower quality\n")

  ape_options = ("\n\033[1m"
              "References on quality for Ape format:\033[0m\n"
              "  1    -c1000 = Fast (Best quality)\n"
              "  2    -c2000 = Normal\n"
              "  3    -c3000 = High\n"
              "  4    -c4000 = Extra\n"
              "  5    -c5000 = Insane\033[0m\n")

  mp3_options = ("\n\033[1m"
              "References on quality and bit-rate for MP3:\033[0m\n"
              "  0     medium    >  VBR 92 kbit\n"
              "  1     standard  >  VBR 112 kbit/s\n"
              "  2     extreme   >  VBR 150 kbit/s\n"
              "  3     insane    >  CBR 320 kbit/s\n")

  ogg_options = ("\n\033[1m"
              "References on the quality and bit-rate for OGG:\033[0m\n"
              "  1    >   80 kbit        |     6   >   192 kbit/s\n"
              "  2    >   92 kbit/s      |     7   >   200 kbit/s\n"
              "  3    >   100 kbit/s     |     8   >   260 kbit/s\n"
              "  4    >   128 kbit/s     |     9   >   320 kbit/s\n"
              "  5    >   134 kbit/s     |     10  >   520 kbit/s\n")

  ###################### end strings
  
  flac_diz = {"0":"-0", "1":"-1", "2":"-2", "3":"-3",
              "4":"-4", "5":"-5", "6":"-6", "7":"-7",
              "8":"-8"
              }

  ape_diz = {"1":"-c1000", "2":"-c2000", "3":"-c3000", 
              "4":"-c4000", "5":"-c5000"
              }

  mp3_diz = {"0":"--preset medium", "1":"--preset standard", 
              "2":"--preset extreme", "3":"--preset insane"
                  }

  ogg_diz = {"1":"-q 1", "2":"-q 2", "3":"-q 3", "4":"-q 4", "5":"-q 5",
          "6":"-q 6", "7":"-q 7", "8":"-q 8", "9":"-q 9", "10":"-q 10"
                  }

  object_assignment = {
      'wav > aiff' : ('shntool conv -o aiff', None, None, None, 'aiff'), 
      'aiff > wav' : ('shntool conv o- waw', None, None, None, 'wav'), 
      #'aiff > ape' : ('shntool', None, None, None, 'ape'),
      'flac > wav' : ('shntool conv -o wav', None, None, None, 'wav'),
      'flac > aiff' : ('shntool conv -o aiff', None, None, None, 'aiff'),
      'flac > ape' : ('shntool conv -o ape', None, None, None, 'ape'), 
      'ape > wav' : ('shntool conv -o wav', None, None, None, 'wav'),
      'ape > aiff' : ('shntool conv -o aiff', None, None, None, 'aiff'),
      'ape > flac' : ('shntool conv -o flac', None, None, None, 'flac'),

      'wav > flac' : ('flac -V', flac_diz, flac_options, 'Enter the '
                      'compression level in digits 0 to 8, and press '
                      'enter key > ', 'flac'), 

      'aiff > flac' : ('flac -V', flac_diz, flac_options, 'Enter the '
                      'compression level in digits 0 to 8, and press '
                      'enter key > ', 'flac'),

      'wav > mp3' : ('lame --nogap', mp3_diz, mp3_options, 'Enter the compression '
                      'level in digits 0 to 3, and press enter key > ', 'mp3'),

      'aiff > mp3' : ('lame --nogap', mp3_diz, mp3_options, 'Enter the compression '
                      'level in digits 0 to 3, and press enter key > ', 'mp3'),

      'mp3 > wav' : ('lame --nogap --decode', None, None, None, 'wav'),

      'wav > ogg' : ('oggenc', ogg_diz, ogg_options, 'Enter the compression '
                      'level in digits 1 to 10, and press enter key > ', 'ogg'),

      'aiff > ogg' : ('oggenc', ogg_diz, ogg_options, 'Enter the compression '
                      'level in digits 1 to 10, and press enter key > ', 'ogg'),

      'flac > ogg' : ('oggenc', ogg_diz, ogg_options, 'Enter the compression '
                      'level in digits 1 to 10, and press enter key > ', 'ogg'),

      'ogg > wav' : ('oggdec', None, None, None, 'wav'),

      'wav > ape' : ('mac', ape_diz, ape_options, 'Enter the compression '
                      'level in digits 1 to 5, and press enter key > ', 'ape'),
                    }
  try:
      return object_assignment[pair]

  except KeyError:
      return 'KeyError'
