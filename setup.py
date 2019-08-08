#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#########################################################
# Name: setup.py
# Porpose: script for building and setup audiomass package
# Platform: Gnu/Linux, Unix
# Writer: jeanslack <jeanlucperni@gmail.com>
# Copyright: (c) 2015 jeanslack <jeanlucperni@gmail.com>
# license: GPL3
# Rev: nov 22 2017, aug 8 2019
#########################################################

from distutils.core import setup
from setuptools import setup, find_packages
from admspack.datastrings import info

cr = info()
AUTHOR = cr[0]
MAIL = cr[1]
VERSION = cr[3]
RLS_NAME = cr[5]# release name first letter is Uppercase
PRG_NAME = cr[6]
URL = cr[7]
SHORT_DESCRIPTION = cr[8]
LONG_DESCRIPTION = cr[9]
SHORT_LICENSE = cr[12]# short_license

# ---- categorize with ----#
CLASSIFIERS = [
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Natural Language :: English',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: POSIX',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Topic :: Multimedia :: Sound/Audio :: Conversion',
            'Topic :: Utilities',
                ]

#----------  Source/Build distributions  ----------------#

# get the package data
DATA_FILES = [('share/man/man1', ['man/audiomass.1.gz']),
              ('share/audiomass', ['AUTHORS', 'BUGS', 'CHANGELOG', 
               'COPYING', 'README.md', 'TODO']),
              ]
# Setup
setup(name=PRG_NAME,
        version=VERSION,
        description=SHORT_DESCRIPTION,
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        author=AUTHOR,
        author_email=MAIL,
        url=URL,
        license=SHORT_LICENSE,
        platforms=["Linux","Unix","MacOS"],
        packages=find_packages(),
        scripts=['audiomass'],
        data_files=DATA_FILES,
        classifiers=CLASSIFIERS,
        #install_requires=REQUIRES,
        )
