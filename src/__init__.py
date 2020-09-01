# -*- coding: utf-8 -*-
#
#########################################################
# Porpose: audiomass __init__ file that holds package information.
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015/2020 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# First Release: (Ver.0.6) April 2015
# Rev: July.25.2020
#########################################################

__author__ = ('Gianluca Pernigotto', '(aka jeanslack)')
__mail__ = '<jeanlucperni@gmail.com>'
__copyright__ = '© 2013-2020'
__version__ = '0.8.1'
__release__ = 'August 31 2020'
__rls_name__ = "Audiomass"
__prg_name__ = "audiomass"
__url__ = "https://github.com/jeanslack/audiomass"
__short_descript__ = 'Wrapper for multiple audio conversion libraries. '
__long_descript__ = """
**Audiomass** is a command line audio wrapper of the Flac, Lame, Vorbis-tools,
Monkey's Audio, Shntool and FFmpeg libraries. It supports conversions of
different audio formats at a time and the ability to convert even groups of
files in a directory, saving the output in a specific folder.
"""
synapsy = ("usage: audiomass [-h HELP] [-v VERSION] [-c COPYING] "
           "[-C CHECK] [-f FILE {..FILENAME}] [-d DIRECTORY {..DIRNAME}] "
           "[-b BATCH {..FILENAME_1 ..FILENAME_2 ..FILENAME_3 ..}] [-o OUTPUT {..DIRNAME}]"
               )
__usage__ = """%s

Optional arguments:
   -f  --file     single audio file conversion
   -d, --dir      specifies a directory to process
   -b, --batch    run a process for different queued file formats
   -o  --output   save the output into specified folder
   -C, --check    Check for required dependencies
   -h, --help     print this help and exit
   -v, --version  print version and date and exit
   -c, --copying  print license and exit """ % synapsy

__try__ = "type 'audiomass -h' and/or more detailed 'man audiomass'"
__license__ = ("""
    Copyright %s - %s %s
    Mail: %s

    Audiomass is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or (at
    your option) any later version.

    Audiomass is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with audiomass; if not, see <http://www.gnu.org/licenses/>
    or write to the Free Software Foundation, Inc., 51 Franklin St,
    Fifth Floor, Boston, MA  02110-1301 USA
    ==============================================================
    """ % (__copyright__, __author__[0], __author__[1], __mail__))

__short_license__ = "'Gnu GPL3 (Gnu Public License)"
