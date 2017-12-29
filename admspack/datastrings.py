# -*- coding: UTF-8 -*-
#
#########################################################
# Name: datastrings.py (module)
# Porpose: module for cosmetic command line 
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015/2016 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (Ver.0.6) Febbruary 2015
# Rev: 1 nov 22 2017, 2 Dec 15 2017
#########################################################

def info():################################### INFO
  """
  All general info of the audiomass-cli
  """
  AUTHOR = u"Gianluca Pernigotto aka Jeanslack"
  MAIL = u'<jeanlucperni@gmail.com>'
  COPYRIGHT = u'© 2013-2017'
  VERSION = u'v0.7.6'
  RELEASE = u'Dec. 29 2017'
  RLS_NAME = u"Audiomass-CLI"
  PRG_NAME = u"audiomass-cli"
  URL = u"https://github.com/jeanslack/audiomass"
  SHORT_DESCRIPT = u'Audiomass-cli is a Wrapper audio conversions interface'
  LONG_DESCRIPT = u"""
**Audiomass-clc** is a command line wrapper that interfaces on differents 
audio codecs for multiple input data streams conversions. It can be easily 
implemented with other audio library codecs and currently supports: Flac, 
Lame, Vorbis-tools, Monkey's Audio, Shntool FFmpeg, etc.
"""

  USAGE = u"""This is a short help of Audiomass-cli.
For more explanations, please read the manual: 'man audiomass-cli' 
or read the audiomass-cli.pdf into its source directory.

Usage: 
  audiomass-cli option <input filename/dirname>
  audiomass-cli option <input filename/dirname> [-o] [<output dirname>]
  
Options:
  -f  --file    (run process for single file-stream)
  -d, --dir     (run a process to multiple files in dir with single format)
  -b, --batch   (run a process for multiple files queued)
  -o  dirname, --output  (write the output streams into specified folder)
  -C, --check   (Check for required dependencies, no for python of course)
  -h, --help    (print this help and exit)
  -v, --version (print version and date of the program)
  -c, --copying (print license of the program)
  
Exemples:
  audiomass-cli -f '/path name/My directory/audiotrack.wav'
  audiomass-cli -d '/path name/My directory' -o '/path/otherDir'
  audiomass-cli -b 'STREAM1' 'STREAM2' 'STREAM3' 'STREAM4' -o /output/dir
--------------------------------------------------------------"""
  
  TRY = "Try: 'audiomass-cli --help' or 'man audiomass-cli'."

  LICENSE = (u"""==============================================================
%s version %s
Copyright %s - %s
Mail: %s

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at 
your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
==============================================================
""" % (SHORT_DESCRIPT, VERSION, COPYRIGHT, AUTHOR, MAIL))

  SHORT_LICENSE = u"'Gnu GPL3 (Gnu Public License)"

  return (AUTHOR, 
          MAIL, 
          COPYRIGHT, 
          VERSION, 
          RELEASE, 
          RLS_NAME, 
          PRG_NAME, 
          URL, 
          SHORT_DESCRIPT, 
          LONG_DESCRIPT, 
          USAGE, 
          LICENSE, 
          SHORT_LICENSE, 
          TRY
          )
