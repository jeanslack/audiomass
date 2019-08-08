#
#########################################################
# Name: datastrings.py (module)
# Porpose: module for cosmetic output command line 
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015/2019 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# First Release: (Ver.0.6) April 2015
# Rev: nov 22 2017, Dec 15 2017, Aug 8 2019
#########################################################

def info():################################### INFO
    """
    All general info of the audiomass-cli
    """
    AUTHOR = "Gianluca Pernigotto aka Jeanslack"
    MAIL = '<jeanlucperni@gmail.com>'
    COPYRIGHT = '© 2013-2019'
    VERSION = '0.8.0'
    RELEASE = 'Aug. 8 2019'
    RLS_NAME = "Audiomass"
    PRG_NAME = "audiomass"
    URL = "https://github.com/jeanslack/audiomass"
    SHORT_DESCRIPT = 'Audiomass is a audio conversion utility.'
    LONG_DESCRIPT = """
**Audiomass** is a command line wrapper that interfaces on differents 
audio codecs for multiple input data streams conversions. It can be easily 
implemented with other audio library codecs and currently supports: Flac, 
Lame, Vorbis-tools, Monkey's Audio, Shntool FFmpeg, etc.
"""

    SINAPSY = ("usage: audiomass [-h HELP] [-v VERSION] [-c COPYING] "
               "[-C CHECK] [-f FILE] [-d DIRECTORY] "
               "[-b BATCH [..FILE1 ..FILE2 ..FILE3 ..]] [-o DIRNAME]")
    USAGE = """%s 
  
Optional arguments:
   -f  --file     single audio stream conversion.   
   -d, --dir      specifies a directory to process   
   -b, --batch    run a process for different queued file formats   
   -o  --output   write the output streams into specified folder   
   -C, --check    Check for required dependencies   
   -h, --help     print this help and exit   
   -v, --version  print version and date and exit   
   -c, --copying  print license and exit """ % SINAPSY
  
    TRY = "type 'audiomass -h' and/or more detailed 'man audiomass'."

    LICENSE = ("""
    Copyright %s - %s
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
    """ % (COPYRIGHT, AUTHOR, MAIL))

    SHORT_LICENSE = "'Gnu GPL3 (Gnu Public License)"

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
