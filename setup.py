#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# First release: Version: (Ver.0.6) Febbruary 2015
# 
#########################################################
# Name: setup.py
# Porpose: script for building audiomass-cli and package for install
# Platform: Gnu/Linux
# Writer: jeanslack <jeanlucperni@gmail.com>
# Copyright: (c) 2015 jeanslack <jeanlucperni@gmail.com>
# license: GPL3
# Rev 
#########################################################

from distutils.core import setup
from setuptools import setup
import platform
from glob import glob
import sys
import os

VERSION = '0.6.0'
LICENSE = 'Gnu GPL3 (See LICENSE)'
DESCRIPTION = 'Audio format converter'

LONG_DESCRIPTION = """Audiomass-cli - Is a simple audio conversion interface to 
command line for Flac, Lame, Ogg, Mac, Shntool and FFmpeg 
audio libraries. it brings together the tools to encode and 
decode the most popular audio files, such as: MP3, FLAC, OGG, 
APE, WAV and AIFF.
"""

URL =  'https://github.com/jeanslack/audiomass'

 
def glob_files(pattern):
	"""
	this is a simple function for globbing that iterate 
	for list files in dir
	"""
	
	return [f for f in glob(pattern) if os.path.isfile(f)]



def LINUX_SLACKWARE(id_distro, id_version):
	
	
	setup(name = 'audiomass-cli',
		version = VERSION,
		description = DESCRIPTION,
		long_description = LONG_DESCRIPTION,
		author = 'Gianluca Pernigotto aka jeanslack',
		author_email = 'jeanlucperni@gmail.com',
		url = URL,
		license = LICENSE,
		platforms = ['Gnu/Linux (%s %s)' % (id_distro, id_version)],
		packages = ['admspack'],
		scripts = ['audiomass-cli'],
		)

def LINUX_DEBIAN_UBUNTU(id_distro, id_version):
	"""
		------------------------------------------------
		setup build videomass debian package
		------------------------------------------------
		
		TOOLS: 
		apt-get install python-all python-stdeb fakeroot

		USAGE: 
		- for generate both source and binary packages :
			python setup.py --command-packages=stdeb.command bdist_deb
			
		- Or you can generate source packages only :
			python setup.py --command-packages=stdeb.command sdist_dsc
			
		RESOURCES:
		- look at there for major info:
			https://pypi.python.org/pypi/stdeb
			http://shallowsky.com/blog/programming/python-debian-packages-w-stdeb.html
	"""
	
	# this is DATA_FILE structure: 
	# ('dir/file destination of the data', ['dir/file on current place sources']
	# even path must be relative-path
	DATA_FILES = [
		('share/man/man1', ['man/audiomass-cli.1.gz']),
		('share/doc/python-cliffwall', ['AUTHORS', 'BUGS', 'CHANGELOG', 
                              'COPYING', 'LICENSE', 'README.md', 'TODO']),
				]
	
	DEPENDENCIES = ['python >=2.6']
	
	EXTRA_DEPEND = {'vorbis-tools':  ["vorbis-tools"],'shntool':  ["shntool"],
					'flac':  ["flac"], 'monkeys-audio':  ["monkeys-audio"], 
					'lame':  ["lame"], 'sox':  ["sox"],'ffmpeg':  ["ffmpeg"]}
	
	setup(name = 'audiomass-cli',
		version = VERSION,
		description = DESCRIPTION,
		long_description = LONG_DESCRIPTION,
		author = 'Gianluca Pernigotto',
		author_email = 'jeanlucperni@gmail.com',
		url = URL,
		license = LICENSE,
		platforms = ['Gnu/Linux (%s %s)' % (id_distro, id_version)],
		packages = ['admspack'],
		scripts = ['audiomass-cli'],
		data_files = DATA_FILES,
		install_requires = DEPENDENCIES,
		extras_require = EXTRA_DEPEND,
		)

	
##################################################

if sys.platform.startswith('linux2'):
	
	dist_name = platform.linux_distribution()[0]
	dist_version = platform.linux_distribution()[1]
	
	if dist_name == 'Slackware ':
		LINUX_SLACKWARE(dist_name, dist_version)
		
	elif dist_name == 'debian' or dist_name == 'Ubuntu':
		LINUX_DEBIAN_UBUNTU(dist_name, dist_version)
		
	else:
		print 'this platform is not yet implemented: %s %s' % (dist_name, dist_version)
		

else:
	print 'OS not supported'
###################################################
