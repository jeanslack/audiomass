#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#########################################################
# Name:          setup.py
# Porpose:       building and setup audiomass package
# Platform:      Gnu/Linux, Unix
# Writer:        jeanslack <jeanlucperni@gmail.com>
# Copyright:     (c) 2015 jeanslack <jeanlucperni@gmail.com>
# license:       GPL3
# Rev:           July.25.2020
#########################################################
from setuptools import setup, find_packages
from src import (
    __author__,
    __mail__,
    __copyright__,
    __version__,
    __release__,
    __rls_name__,
    __prg_name__,
    __url__,
    __short_descript__,
    __long_descript__,
    __license__,
    __short_license__,
    )


def build():
    """build"""

    # ---- categorize with ----#
    classifiers = [
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

    # get the package data
    data_files = [('share/man/man1', ['man/audiomass.1.gz']),
                  ('share/audiomass', ['AUTHORS',
                                       'BUGS',
                                       'CHANGELOG',
                                       'COPYING',
                                       'README.md',
                                       'TODO']),
                  ]
    # Setup
    setup(name=__prg_name__,
          version=__version__,
          description=__short_descript__,
          long_description=open('README.md').read(),
          long_description_content_type='text/markdown',
          author=__author__[0],
          author_email=__mail__,
          url=__url__,
          license=__short_license__,
          platforms=["Linux", "Unix", "MacOS"],
          packages=find_packages(),
          data_files=data_files,
          zip_safe=False,
          python_requires=">=3.5.3, <4",
          entry_points={'gui_scripts': ['audiomass=src.audiomass:main']},
          classifiers=classifiers,
          )


if __name__ == '__main__':
    build()
