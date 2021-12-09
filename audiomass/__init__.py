# -*- coding: utf-8 -*-
"""
Porpose: audiomass __init__ file that holds package information.
Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
Copyright: (c) 2015/2020 Gianluca Pernigoto <jeanlucperni@gmail.com>
license: GPL3
Rev: July.25.2020, Dec 08 2021
Code checker: flake8, pylint
"""

__author__ = ('Gianluca Pernigotto', '(aka jeanslack)')
__mail__ = '<jeanlucperni@gmail.com>'
__copyright__ = '© 2013-2021'
__version__ = '0.9.0'
__release__ = 'December 08 2021'
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
SYNAPSY = ("usage: audiomass [-h HELP] [-v VERSION] [-C COPYING] "
           "[-c CHECK] [-f FILE {..FILENAME}] [-d DIRECTORY {..DIRNAME}] "
           "[-b BATCH {..FILENAME_1 ..FILENAME_2 ..FILENAME_3 ..}] "
           "[-o OUTPUT {..DIRNAME}]"
           )
__usage__ = f"""{SYNAPSY}

Optional arguments:
   -f  --file     Convert only one audio file at a time
   -d, --dir      Converts a bunch of audio files contained in a directory
   -b, --batch    Convert a queue of files even with different formats
   -o  --output   Save the output files to a specified folder
   -c, --check    Check of available audio libraries
   -h, --help     print this help and exit
   -v, --version  print version and date and exit
   -C, --copying  print license and exit """

__try__ = "type 'audiomass -h' for help or, more detailed, run 'man audiomass'"
__license__ = (f"""
    Copyright {__copyright__} - {__author__[0]} {__author__[1]}
    Mail: {__mail__}

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
    """)

__short_license__ = "'Gnu GPL3 (Gnu Public License)"
