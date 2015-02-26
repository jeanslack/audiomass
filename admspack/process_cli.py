#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: process_cli.py (module)
# Porpose: execute processes in single and batch mode
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015/2016 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (Ver.0.6) Febbruary 2015
# Rev
#########################################################

import os
import subprocess
import glob
import sys
	
class Process_Conversion(object):
    """
    Run the processes for command line interface
    """
    def __init__(self, path_in, command, bitrate, batch, codec, input_format):
        
        self.command = command
        self.bitrate = bitrate
        self.path_in = path_in
        self.codec = codec
        self.input_format = input_format
        if batch == 'on':
            self.process_batch()
        if batch == 'off':
            self.single_convert()


    def single_convert(self):
        """
        process gor a single audio file name
        """
        # TODO make a process for different audio extension
        
        outpath = os.path.splitext(self.path_in)[0]# remove extension

        if os.path.exists('%s.%s' % (outpath, self.codec)):
            sys.exit("\n\033[1m Warning:\033[0m '%s.%s' already exists\n" % (
                                                outpath, self.codec))
        command_dict = {
            'flac -V':"flac -V %s '%s'" % (self.bitrate, self.path_in),
        
            'lame':'lame %s "%s" "%s.mp3"' % (self.bitrate, self.path_in, 
                                    outpath),
            
            'oggenc':'oggenc %s "%s"' % (self.bitrate, self.path_in),
                        
            'mac':'mac "%s" "%s.ape" %s' % (self.path_in, outpath, 
                                self.bitrate),
                        
            'ffmpeg':'ffmpeg -i "%s" %s "%s.%s" ' % (self.path_in, 
                                    self.bitrate, outpath, self.codec),
                        
            'oggdec':"oggdec '%s'" % (self.path_in),
                        
            'shntool':"shntool conv -o %s '%s'" % (self.codec,  self.path_in),
                        }
            
        print "\n\033[1m Convert '%s'\033[0m\n" % self.path_in
        subprocess.check_call(command_dict[self.command], shell=True)
        print "\n\033[1mDone...\033[0m\n"
            
        
    def process_batch(self):
        """
        batch process for multiple file extension
        """
        exe = 'False'
        count = 0
        
        for f in glob.glob("%s/*.%s" % (self.path_in, self.input_format)) :
            exe = None
            count += 1
            outpath = os.path.splitext(f)[0] # path
            if os.path.exists('%s.%s' % (outpath, self.codec)):
                print ("\n\033[1m Warning:\033[0m '%s.%s' already exists\n"
                                        % (outpath, self.codec))
                continue
            
            print "\n\033[1m %s) Convert '%s'\033[0m\n" % (str(count),f)
            
            command_dict = {
                
                'flac -V':"flac -V %s '%s'" % (self.bitrate, f),
        
                'lame':'lame %s "%s" "%s.mp3"' % (self.bitrate, f, outpath),
                        
                'oggenc':'oggenc %s "%s"' % (self.bitrate,f),
                        
                'mac':'mac "%s" "%s.ape" %s' % (f, outpath, self.bitrate),
                        
                'ffmpeg':'ffmpeg -i "%s" %s "%s.%s" ' % (f, self.bitrate, 
                                            outpath, self.codec),
                        
                'oggdec':"oggdec '%s'" % (f),
                        
                'shntool':"shntool conv -o %s '%s'" % (self.codec, f),
                            }
                
            subprocess.check_call(command_dict[self.command], shell=True)
                
        if exe == 'False':
            print ("\n\033[1m Error:\033[0m Files missing. No files '%s' "
                        "in '%s' \n" % (self.input_format, self.path_in)
                        )
        else:
            print "\033[1mDone...\033[0m\n"
