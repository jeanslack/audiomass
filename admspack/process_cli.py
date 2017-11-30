#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: process_cli.py (module)
# Porpose: execute processes for file, files in dir and batch
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015/2016 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (Ver.0.6) Febbruary 2015
# Rev 1 Nov. 22 2017
#########################################################

import os
import subprocess
import glob
import sys

class Process_Conversion(object):
    """
    Run the processes for command line interface
    """
    def __init__(self, path_in, command, bitrate, type_proc, codec, input_format):

        self.command = command
        self.bitrate = bitrate
        self.path_in = path_in
        self.codec = codec
        self.input_format = input_format
        if type_proc == 'dir':
            self.dir_process()
        if type_proc == 'file':
            self.file_process()
        if type_proc == 'batch':
            #self.batch_process()
            #print path_in
            #print command
            #print bitrate
            #print type_proc
            #print codec
            #print input_format
            print

    def file_process(self):
        
        # QUESTO SONO LE VARIABILI NECESSARIE PER PROCESSO FILE E DIRECTORY
        path_in = 'percorso di input dello stream, es: /home/Musica'
        stream = 'Nome dello stream senza nessuna estensione, es: nome_canzone'
        stream_in = 'Nome dello stream di input, es: nome-canzone.wav'
        stream_out = 'Nome dello stream di output, es: nome-canzone.flac'
        path_out = 'percorso di output dello stream, es: /home/name/Documenti'
        """
        process gor a single audio file name
        """
        # TODO make a process for different audio extension
        
        path_out = os.path.splitext(self.path_in)[0]# remove extension

        if os.path.exists('%s.%s' % (path_out, self.codec)):
            sys.exit("\n\033[33;1mWarning:\033[0m '%s.%s' already exists\n" % (
                                                path_out, self.codec))
        command_dict = {
            'flac -V':"flac -V %s '%s' -o '%s.%s'" % (self.bitrate, self.path_in, path_out, codec),
        
            'lame':'lame %s "%s" "%s.%s"' % (self.bitrate, self.path_in, path_out, codec),
            
            'oggenc':'oggenc %s "%s" -o "%s.%s"' % (self.bitrate, self.path_in, path_out, codec),
                        
            'mac':'mac "%s" "%s.%s" %s' % (self.path_in, path_out, codec, self.bitrate),
                        
            'ffmpeg':'ffmpeg -i "%s" %s "%s.%s" ' % (self.path_in, 
                                    self.bitrate, path_out, self.codec),
                        
            'oggdec':"oggdec '%s' -o %s.%s" % (self.path_in, path_out, cedec),
                        
            'shntool':"shntool conv -o %s '%s' -d '%s'" % (self.codec,  self.path_in, path_out),
                    }
        print command_dict[self.command]
        try:
            print "\n\033[1mConvert '%s'\033[0m\n" % self.path_in
            subprocess.check_call(command_dict[self.command], shell=True)
            print "\n\033[1mDone...\033[0m\n"
        except subprocess.CalledProcessError as err:
            sys.exit("\033[31;1mERROR!\033[0m %s" % (err))

    def dir_process(self):
        """
        (dir)ectory process for multiple conversion with same format
        """
        exe = 'False'
        count = 0
        
        try:
        
            for f in glob.glob("%s/*.%s" % (self.path_in, self.input_format)) :
                exe = None
                count += 1
                path_out = os.path.splitext(f)[0] # path
                if os.path.exists('%s.%s' % (path_out, self.codec)):
                    print ("\n\033[33;1mWarning:\033[0m '%s.%s' already exists\n"
                                    % (path_out, self.codec))
                    continue
            
                print "\n\033[1m %s) Convert '%s'\033[0m\n" % (str(count),f)
            
                command_dict = {
                
                'flac -V':"flac -V %s '%s'" % (self.bitrate, f),
        
                'lame':'lame %s "%s" "%s.mp3"' % (self.bitrate, f, path_out),
                        
                'oggenc':'oggenc %s "%s"' % (self.bitrate,f),
                        
                'mac':'mac "%s" "%s.ape" %s' % (f, path_out, self.bitrate),
                        
                'ffmpeg':'ffmpeg -i "%s" %s "%s.%s" ' % (f, self.bitrate, 
                                            path_out, self.codec),
                        
                'oggdec':"oggdec '%s'" % (f),
                        
                'shntool':"shntool conv -o %s '%s'" % (self.codec, f),
                            }
                
                subprocess.check_call(command_dict[self.command], shell=True)
            
            if exe == 'False':
                print ("\033[31;1mError:\033[0m Files missing. No files '%s' "
                    "in '%s' \n" % (self.input_format, self.path_in)
                        )
            else:
                print "\033[1mDone...\033[0m\n"

        except subprocess.CalledProcessError as err:
            sys.exit("\033[31;1mERROR!\033[0m %s" % (err))
        
    def batch_process(self):
        print 'sono su process'
        print self.command
        print self.bitrate
        print self.path_in
        print self.codec
        print self.input_format
