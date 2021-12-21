#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import itertools

def supported_formats():
    """
    """
    return {1: ('WAV', 'wav', [1]),
            2: ('AIFF', 'aiff', [2, 4]),
            3: ('FLAC', 'flac', [3]),
            4: ('APE', 'ape', [3, 4]),
            5: ('MP3', 'mp3', [3, 4, 5, 6]),
            6: ('OGG', 'ogg', [3, 4, 5, 6]),
            }

f_list = ['Beneath The Geyser.flac', 'South East Wind.flac', 'Etna - Etna.log',
         '01 - Beneath The Geyser.ogg', '01 - Beneath The Geyser.mp3',
         '04 - French Picadores.wav', 'foo_dr.txt']

filecatalog = {}

if __name__ == '__main__':

    for infile in f_list:
        ext = os.path.splitext(infile)[1].replace(".", "")

        for frmt in supported_formats().values():
            if ext in frmt:
                print('è in format')
                if frmt[1] not in filecatalog:
                    #print('creo la chiave %s' % frmt[1])
                    filecatalog[frmt[1]] = {'files': [],
                                            'index': None}
                #print('setto il diz')
                filecatalog[frmt[1]]['files'].append(infile)
                filecatalog[frmt[1]]['index'] = frmt[2]
            else:
                print(infile)

    print(filecatalog)



#if __name__ == '__main__':
    #from audiomass import batch_conversion
    #x = batch_conversion.get_format_and_bitrate(sys.argv[1], sys.argv[2])
    #print(x)

#if __name__ == '__main__':
    #from audiomass import comparisions
    #x = comparisions.comparing(sys.argv[3])
    #print(x)


    #from audiomass.audio_formats import AudioFormats
    #main = AudioFormats('wav')
    #output_format = main.output_selector('2')
    ##codec_data = main.pairing_formats()

    ##print(output_format)
    ##print(codec_data)
