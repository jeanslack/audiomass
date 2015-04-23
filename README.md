================================================================================ 
Audiomass-cli - A simple audio conversion interface 
================================================================================ 

Audiomass-cli - Is a simple audio conversion interface to command line for Flac, 
Lame, Ogg, Mac, Shntool and FFmpeg audio libraries. it brings together the tools 
to encode and decode the most popular audio files, such as: MP3, FLAC, OGG, APE, 
WAV and AIFF.

--------------------------------------------------------------------------------

Copyright © 2015/2016 jeanslack 
 
  Author and Developer: jeanslack 
  Mail: <jeanlucperni@gmail.com>
  License: GPL3 (see LICENSE file in the docs folder)

--------------------------------------------------------------------------------

Dependencies requires:

	python >=2.6 (no python 3)
	
Dependencies recommended:

	flac
	lame
	sox (optional)
	mac [monkeys-audio or libmac2]
	vorbis-tools [oggenc, oggdec]
	shntool
	ffmpeg


Use
-------

- Unzip the sources tarball of audiomass-cli
- Open a terminal window in unzipped folder and type:

		audiomass-cli -h

for a shortcut help

Installation
-------

audiomass-cli not require installation, but if you are interested build an 
installable package, see below:


--------------------------------------------------------------------------------

DEBIAN:

--------------------------------------------------------------------------------

Extra dependencies for build package with distutils:

		# apt-get install python-all python-stdeb fakeroot

Enter in unzipped sources folder and type (with not root):

		python setup.py --command-packages=stdeb.command bdist_deb

This should create a python-pysplitcue_version_all.deb in the new deb_dist directory.

see the setup.py script-file for more info on how-to build .deb package

--------------------------------------------------------------------------------

SLACKWARE:

--------------------------------------------------------------------------------

Require pysetuptools at: [slackbuild.org](http://slackbuilds.org/repository/14.1/python/pysetuptools/)

Then download the SlackBuild: [My-Repo-Slackware](https://github.com/jeanslack/My-Repo-Slackware/tree/master/slackware/multimedia/audiomass)


--------------------------------------------------------------------------------
The installations includes a man page
--------------------------------------------------------------------------------
