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
############################################################## MENUs
def input_menu():
    """
    Menu for input audio selection format used from process_dir
    only
    """
    print """    Select the files input format below:
    -----------------------------------------------
    \033[1m 1 \033[0m .. WAV   (WAVEform audio format, PCM uncompresed)
    \033[1m 2 \033[0m .. AIF   (Apple Interchange File Format)
    \033[1m 3 \033[0m .. FLAC  (Free Lossless Audio Codecs)
    \033[1m 4 \033[0m .. APE   (Monkey's audio)
    \033[1m 5 \033[0m .. MP3   (MPEG-1 Audio Layer 3)
    \033[1m 6 \033[0m .. OGG   (ogg-vorbis lossy format)
    -----------------------------------------------
    \033[41;37;1m Q \033[0m \033[1m..EXIT\033[0m
    ----------------------------------------------- """


def output_menu():
    """
    Menu for output audio selection format used from all process(f,d,b)
    """
    graphic_out_formats = [
                    "----------------------",
                    "  \033[34;1mA\033[0m ......... Wav", 
                    "  \033[34;1mB\033[0m ......... Aiff", 
                    "  \033[34;1mC\033[0m ......... Flac", 
                    "  \033[34;1mD\033[0m ......... Ape", 
                    "  \033[34;1mE\033[0m ......... Mp3", 
                    "  \033[34;1mF\033[0m ......... Ogg",  
                    "----------------------", 
                    " \033[41;37;1m Q \033[0m \033[1m..EXIT\033[0m", 
                    "----------------------"
                            ]
    return graphic_out_formats


def a_formats():
  """
  Content of all audio supported formats . When you want add new formats
  you might start from here and then add formats modules to the function
  comparision
  """
  
  support = ['wav','aiff','flac','ape','mp3','ogg']
  
  supported_formats = {'1': (1,'wav'), '2': (2,'aiff'), 
                  '3': (3,'flac'), '4': (4,'ape'), 
                  '5': (5,'mp3'),'6': (6,'ogg')}
  
  case = {'a':'wav', 'A':'wav', 'b':'aiff','B':'aiff', 'c':'flac', 
              'C':'flac','d':'ape', 'D':'ape', 'e':'mp3', 'E':'mp3', 
              'f':'ogg', 'F':'ogg',
              }
  
  return supported_formats, support, case


def comparision(pair):
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
              "  8 = maximum compression > less space > lower quality\n"
              )

  ape_options = ("\n\033[1m"
              "References on quality for Ape format:\033[0m\n"
              "  1    -c1000 = Fast (Best quality)\n"
              "  2    -c2000 = Normal\n"
              "  3    -c3000 = High\n"
              "  4    -c4000 = Extra\n"
              "  5    -c5000 = Insane\033[0m\n"
              )

  mp3_options = ("\n\033[1m"
              "References on quality and bit-rate for MP3:\033[0m\n"
              "  0     medium    >  VBR 92 kbit\n"
              "  1     standard  >  VBR 112 kbit/s\n"
              "  2     extreme   >  VBR 150 kbit/s\n"
              "  3     insane    >  CBR 320 kbit/s\n\n"
              )

  ffmpeg_mp3_options = ("\n\033[1m"
              "References on quality and bit-rate for MP3:\033[0m\n"
              "  0     >  VBR 128 kbit\n"
              "  1     >  VBR 160 kbit/s\n"
              "  2     >  VBR 192 kbit/s\n"
              "  3     >  VBR 260 kbit/s\n"
              "  4     >  CBR 320 kbit/s\n"
              )

  ogg_options = ("\n\033[1m"
              "References on the quality and bit-rate for OGG:\033[0m\n"
              "  1    >   80 kbit        |     6   >   192 kbit/s\n"
              "  2    >   92 kbit/s      |     7   >   200 kbit/s\n"
              "  3    >   100 kbit/s     |     8   >   260 kbit/s\n"
              "  4    >   128 kbit/s     |     9   >   320 kbit/s\n"
              "  5    >   134 kbit/s     |     10  >   520 kbit/s\n"
              )

  ffmpeg_ogg_options = ("\n\033[1m"
              "References on the quality and bit-rate for OGG:\033[0m\n"
              "  0    >  VBR 128 kbit\n"
              "  1    >  VBR 160 kbit/s\n"
              "  2    >  VBR 192 kbit/s\n"
              "  3    >  VBR 260 kbit/s\n"
              "  4    >  CBR 320 kbit/s\n"
              )
              
  ###################### end list strings
  
  flac_diz = {"0":"-0", "1":"-1", "2":"-2", "3":"-3",
              "4":"-4", "5":"-5", "6":"-6", "7":"-7",
              "8":"-8"
              }

  ape_diz = {"1":"-c1000", "2":"-c2000", "3":"-c3000", 
              "4":"-c4000", "5":"-c5000"
              }

  mp3_diz = {"0":"--preset medium", "1":"--preset standard", 
              "2":"--preset extreme", "3":"--preset insane"}

  ffmpeg_mp3_diz = {"0":"-acodec libmp3lame -b:a 128k -ar 44100",  
                      "1":"-acodec libmp3lame -b:a 160k -ar 44100",
                      "2":"-acodec libmp3lame -b:a 192k -ar 44100", 
                      "3":"-acodec libmp3lame -b:a 260k -ar 44100",
                      "4":"-acodec libmp3lame -b:a 320k -ar 44100",
                          }

  ogg_diz = {"1":"-q 1", "2":"-q 2", "3":"-q 3", "4":"-q 4", "5":"-q 5",
          "6":"-q 6", "7":"-q 7", "8":"-q 8", "9":"-q 9", "10":"-q 10"
                  }

  ffmpeg_ogg_diz = {"0":"-vn -acodec libvorbis -ar 44100 -ab 128k",  
                      "1":"-vn -acodec libvorbis -ar 44100 -ab 160k", 
                      "2":"-vn -acodec libvorbis -ar 44100 -ab 192k", 
                      "3":"-vn -acodec libvorbis -ar 44100 -ab 260k",  
                      "4":"-vn -acodec libvorbis -ar 44100 -ab 320k",
                          }
      
  object_assignment = {
      'wav > aiff' : ('shntool', None, None, None, 'aiff'), 
      'aiff > wav' : ('shntool', None, None, None, 'wav'), 
      #'aiff > ape' : ('shntool', None, None, None, 'ape'),
      'flac > wav' : ('shntool', None, None, None, 'wav'),
      'flac > aiff' : ('shntool', None, None, None, 'aiff'),
      'flac > ape' : ('shntool', None, None, None, 'ape'), 
      'ape > wav' : ('shntool', None, None, None, 'wav'),
      'ape > aiff' : ('shntool', None, None, None, 'aiff'),
      'ape > flac' : ('shntool', None, None, None, 'flac'),

      'wav > flac' : ('flac', flac_diz, flac_options, 'Enter the '
                      'compression level in digits 0 to 8, and press '
                      'enter key > ', 'flac'), 
      'aiff > flac' : ('flac', flac_diz, flac_options, 'Enter the '
                      'compression level in digits 0 to 8, and press '
                      'enter key > ', 'flac'),

      'wav > mp3' : ('lame', mp3_diz, mp3_options, 'Enter the compression '
                      'level in digits 0 to 3, and press enter key > ', 'mp3'),
      'aiff > mp3' : ('lame', mp3_diz, mp3_options, 'Enter the compression '
                      'level in digits 0 to 3, and press enter key > ', 'mp3'),
      'mp3 > wav' : ('lame --decode', None, None, None, 'wav'),
      #'mp3 > aiff' : ('lame', None, None, None, 'aiff'), ## WARNING Valutare
      
      'wav > ogg' : ('oggenc', ogg_diz, ogg_options, 'Enter the compression '
                      'level in digits 1 to 10, and press enter key > ', 'ogg'),
      'aiff > ogg' : ('oggenc', ogg_diz, ogg_options, 'Enter the compression '
                      'level in digits 1 to 10, and press enter key > ', 'ogg'),
      'flac > ogg' : ('oggenc', ogg_diz, ogg_options, 'Enter the compression '
                      'level in digits 1 to 10, and press enter key > ', 'ogg'),

      'ogg > wav' : ('oggdec', None, None, None, 'wav'),

      'wav > ape' : ('mac', ape_diz, ape_options, 'Enter the compression '
                      'level in digits 1 to 5, and press enter key > ', 'ape'),

      'flac > mp3' : ('ffmpeg', ffmpeg_mp3_diz, ffmpeg_mp3_options, 
                      'Enter the compression level in digits 0 to 4, '
                      'and press enter key > ', 'mp3'),
      'ape > mp3' : ('ffmpeg', ffmpeg_mp3_diz, ffmpeg_mp3_options, 
                      'Enter the compression level in digits 0 to 4, '
                      'and press enter key > ', 'mp3'),
      'ape > ogg' : ('ffmpeg', ffmpeg_ogg_diz, ffmpeg_ogg_options,
                      'Enter the compression level in digits 0 to 4, '
                      'and press enter key > ', 'ogg'),
                          }
  try:
      return object_assignment[pair]

  except KeyError:
      return 'KeyError' 
