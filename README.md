
Audiomass-cli
=============

## Description

**Audiomass-cli** is a command line wrapper that interfaces on differents 
audio codecs for multiple input data streams conversions. It can be easily 
implemented with other audio library codecs and currently supports: Flac, 
Lame, Vorbis-tools, Monkey's Audio, Shntool and FFmpeg, etc.

## License and Copyright

Copyright © 2010 - 2017 Gianluca Pernigotto   
Author and Developer: Gianluca Pernigotto   
Mail: <jeanlucperni@gmail.com>   
License: GPL3 (see LICENSE file in the docs folder)

## System Requirements

* Gnu/Linux
* OSX 10.7 or later

There is not yet a Windows implementation

## Essential Dependencies

**Required:**

- python >=2.6 (no python 3)

**Recommended:**

- flac
- lame
- vorbis-tools [oggenc, oggdec]
- shntool
- ffmpeg
- monkey's audio (I've seen it has different names, this depends on the
                  your O.S. - try search: libmac2, mac, monkey's audio)

## Download

If you want a stable release of audiomass, suitable for common use and
packaging for Debian and Slackware distribuitions, download [here](https://github.com/jeanslack/audiomass/releases)   

## Use

`audiomass-cli option <input filename/dirname>`   
`audiomass-cli option <input filename/dirname> [-o] [<output dirname>]`

**Options:**

 * -f  --file    (run process for single file-stream)
 * -d, --dir     (run a process to multiple files in dir with single format)
 * -b, --batch   (run a process for multiple files queued)
 * -o, --output  (write the output streams into specified directory)
 * -C, --check   (Check for required dependencies, no for python of course)
 * -h, --help    (show help and exit)
 * -v, --version (show version and date of the program)
 * -c, --copying (show license of the program)

**Examples:** 

Unzip the sources tarball of audiomass-cli, open a terminal window on its 
path-name them and add the *-f* option (f=file) and proceeded to convert a 
single audio file:   
`~$ ./audiomass-cli -f '/home/Name/my Music/audiofile.wav'`. 

Do you have many files with the same format to convert? then loads the folder 
that contains them and add the *-d* option, (d=dir):   
`~$ ./audiomass-cli -d '/home/Name/MyFolder/flac_files'`

Load audio streams queue with differents formats also on differents locations on
the user-space. The *-b* option (b=batch), the *-o* option indicates the output 
directory for saving. If  more  than one stream is specified, they must either 
be quoted and separated to one or more white-space.   
`~$ ./audiomass-cli -b 'STREAM1' 'STREAM2' 'STREAM3' 'STREAM4' -o /output/dir`   

For a shortcut help, type `audiomass-cli --help` or read the best audiomass man page.

## Installation

audiomass-cli not require installation, but if you are interested build an 
installable package, see below:

**Debian:**

Extra dependencies for build package with distutils:
`~# apt-get install python-all python-stdeb fakeroot`

Enter in unzipped sources folder and type (with not root):
`~$ python setup.py --command-packages=stdeb.command bdist_deb`

This should create a python-pysplitcue_version_all.deb in the new deb_dist directory.

see the setup.py for more info on how-to build .deb package

**Slackware**

Is available a SlackBuild script to build a package *.tgz* for Slackware and Slackware based 
distributions. See here [pysplitcue.SlackBuild](https://github.com/jeanslack/slackbuilds/tree/master/audiomass)

Remember: install **pysetuptools** if not present first.
You can search on this site: 
[SlackBuild.org](http://slackbuilds.org/repository/14.1/python/pysetuptools/)

