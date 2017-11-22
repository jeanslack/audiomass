
Audiomass-cli
----

## Description

**Audiomass-cli** is a audio conversion interface and front-end for Flac, Lame, 
Ogg, Mac, Shntool and FFmpeg audio libraries. it brings together the tools 
to encode and decode the most popular audio files, such as: MP3, FLAC, OGG, 
APE, WAV and AIFF.

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
- sox
- vorbis-tools [oggenc, oggdec]
- shntool
- ffmpeg
- monkey's audio (I've seen it has different names, this depends on the
                  your O.S. - try search: libmac2, mac. monkey's audio)

## Download

If you want a stable release of audiomass, suitable for common use and
packaging for Debian and Slackware distro, download here:
[Downloads](https://github.com/jeanslack/audiomass/releases)   

## Use

Have you installed all needed dependencies? Well!

**Examples:** 

Unzip the sources tarball of audiomass-cli, open a terminal 
window on its path-name and proceeded to convert a single audio file: 
`~$ ./audiomass-cli '/home/Name/my Music/audiofile.wav'`. 

Do you have many files with the same format to convert? then loads the 
folder that contains them and add the *-b* option (b = batch):
`~$ ./audiomass-cli -b '/home/Name/MyFolder/flac_files'`

For a shortcut help, type `audiomass-cli --help` or read the audiomass man page.

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
You can search on this site: [SlackBuild.org](http://slackbuilds.org/repository/14.1/python/pysetuptools/)

