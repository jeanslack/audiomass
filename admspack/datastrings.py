#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: datastrings.py (module)
# Porpose: module for cosmetic command line 
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015/2016 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (Ver.0.6) Febbruary 2015
# Rev 1 november 22 2017
#########################################################

def info():################################### INFO
  """
  All general info of the audiomass-cli
  """
  author = u"Gianluca Pernigotto aka Jeanslack"
  mail = u'<jeanlucperni@gmail.com>'
  copyright = u'© 2013-2017'
  version = u'v0.6.1'
  release = u'Nov. 21 2017'
  rls_name = u"Audiomass-CLI"
  prg_name = u"audiomass-cli"
  webpage = u"https://github.com/jeanslack/audiomass"
  short_decript = u'Audiomass-clc is a front-end wrapper audio converter'
  long_desript = u"""
Audiomass-clc is a front-end wrapper audio converter to simplify the 
use of Flac, Lame, vorbis-tools, Monkey's audio, Shntool and FFmpeg 
audio libraries. It brings together all this tools/libraries for audio 
conversions between the most popular audio formats. It has an easy command 
line interface with different default settings at your choice.
"""

  usage = """--------------------------------------------------------------
Audiomass-cli - %s by %s
--------------------------------------------------------------
Simple audio conversion interface to command line for Flac, 
Lame, Ogg, Mac, Shntool and FFmpeg audio libraries.

Usage: 
  aconvert-cli <infile>
  aconvert-cli [options] [indirectory]
  
Options:
  -b, --batch   (run a process on multiple files in a directory)
  -h, --help    (print this help and exit)
  -v, --version (print version and date of the program)
  -c, --copying (print license of the program)
  
Exemples:
  aconvert-cli '/path name/My directory/audiotrack.wav'
  aconvert-cli -b '/path name/My directory'
  aconvert-cli -b 
--------------------------------------------------------------
""" % (copyright, author)

  license = u"""
Copyright %s - %s
Author and Developer: %s
Mail: %s

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License 3 as published by
the Free Software Foundation; version .

This package is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this package; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
""" % (copyright, author, author, mail)

  short_license = u"'Gnu GPL3 (Gnu Public License)"

  return (author, mail, copyright, version, release, rls_name, prg_name, webpage, 
          short_decript, long_desript, usage, license, short_license)

############################################################## MENUs
def input_menu():
    """
    Menu for input audio selection format
    """
    print """\033[1m
    ======================= AUDIOMASS ==================                                                             
                A Simple Audio Converter Interface (cli)
    ==============================================================\033[0m"""

    print """
        select the files input format below:                 

        -----------------------------------------------
        \033[42;37;1m 1 \033[0m .. WAV   (WAVEform audio format, PCM uncompresed)

        \033[42;37;1m 2 \033[0m .. AIF   (Apple Interchange File Format)

        \033[42;37;1m 3 \033[0m .. FLAC  (Free Lossless Audio Codecs) 

        \033[42;37;1m 4 \033[0m .. APE   (Monkey's audio)

        \033[42;37;1m 5 \033[0m .. MP3   (MPEG-1 Audio Layer 3)

        \033[42;37;1m 6 \033[0m .. OGG   (ogg-vorbis lossy format)                    
        -----------------------------------------------
        \033[41;37;1m Q \033[0m \033[1m..EXIT\033[0m
        ----------------------------------------------- 
        """


def output_menu():
    """
    Menu for output audio selection format
    """
    graphic_a_format = [
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
    return graphic_a_format
