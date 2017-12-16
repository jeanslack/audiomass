#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# First release: Version: (Ver.0.6) Febbruary 2015
# 
#########################################################
# Name: setup.py
# Porpose: script for building audiomass-cli package
# Platform: Gnu/Linux
# Writer: jeanslack <jeanlucperni@gmail.com>
# Copyright: (c) 2015 jeanslack <jeanlucperni@gmail.com>
# license: GPL3
# Rev 1 november 22 2017
#########################################################
from distutils.core import setup
from setuptools import setup
import platform
from glob import glob
import sys
import os
from admspack.datastrings import info

cr = info()
AUTHOR = cr[0]
MAIL = cr[1]
COPYRIGHT = cr[2]
VERSION = cr[3]
RELEASE = cr[4]
RLS_NAME = cr[5]# release name first letter is Uppercase
PRG_NAME = cr[6]
URL = cr[7]
DESCRIPTION = cr[8]
LONG_DESCRIPTION = cr[9]
LONG_HELP = cr[10]
LICENSE = cr[12]# short_license

def glob_files(pattern):
    """
    this is a simple function for globbing that iterate 
    for list files in dir
    """
    return [f for f in glob(pattern) if os.path.isfile(f)]

def LINUX_SLACKWARE(id_distro, id_version):
    """
    Slackware distribuitions use the slackbuild for automatize 
    the building package. Here there are some informations to pass
    at slackbuild for compile this package.
    """

    setup(name = RLS_NAME,
        version = VERSION,
        description = DESCRIPTION,
        long_description = LONG_DESCRIPTION,
        author = AUTHOR,
        author_email = MAIL,
        url = URL,
        license = LICENSE,
        platforms = ['Gnu/Linux (%s %s)' % (id_distro, id_version)],
        packages = ['admspack'],
        scripts = [PRG_NAME],
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
        ('share/doc/python-audiomass-cli', ['AUTHORS', 'BUGS', 'CHANGELOG', 
                              'COPYING', 'README.md', 'TODO']),
                ]
    DEPENDENCIES = ['python >=3.5']
    EXTRA_DEPEND = {'vorbis-tools':  ["vorbis-tools"],'shntool':  ["shntool"],
                    'flac':  ["flac"], 'monkeys-audio':  ["monkeys-audio"], 
                    'lame':  ["lame"], 'ffmpeg':  ["ffmpeg"]}
    setup(name = RLS_NAME,
        version = VERSION,
        description = DESCRIPTION,
        long_description = LONG_DESCRIPTION,
        author = AUTHOR,
        author_email = MAIL,
        url = URL,
        license = LICENSE,
        platforms = ['Gnu/Linux (%s %s)' % (id_distro, id_version)],
        packages = ['admspack'],
        scripts = [PRG_NAME],
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
        print 'this platform is not yet implemented: %s %s' % (
                                       dist_name, dist_version)
else:
    print 'OS not supported'
###################################################
