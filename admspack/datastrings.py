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
  author = u"Gianluca Pernigotto aka Jeanslack"
  mail = u'<jeanlucperni@gmail.com>'
  copyright = u'© 2013-2017'
  version = u'v0.7.4'
  release = u'Dec. 15 2017'
  rls_name = u"Audiomass-CLI"
  prg_name = u"audiomass-cli"
  webpage = u"https://github.com/jeanslack/audiomass"
  short_decript = u'Audiomass-clc - Wrapper audio conversions interface'
  long_desript = u"""
**Audiomass-clc** is a command line wrapper that interfaces on differents 
audio codecs for multiple input data streams conversions. It can be easily 
implemented with other audio library codecs and currently supports: Flac, 
Lame, Vorbis-tools, Monkey's Audio, Shntool FFmpeg, etc.
"""

  usage = u"""This is a short help of Audiomass-cli.
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
  
  try_help = "Try: 'audiomass-cli --help' or 'man audiomass-cli'."

  license = (u"""==============================================================
%s version %s
Copyright %s - %s
Mail: %s

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; version 3

This package is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this package; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
==============================================================
""" % (short_decript, version, copyright, author, mail))

  short_license = u"'Gnu GPL3 (Gnu Public License)"

  return (author, mail, copyright, version, release, rls_name, prg_name, webpage, 
          short_decript, long_desript, usage, license, short_license, try_help)
