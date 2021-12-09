
# Audiomass - wrapper for multiple audio conversion libraries.

**Audiomass** is a command line audio wrapper of the Flac, Lame, Vorbis-tools, 
Monkey's Audio, Shntool and FFmpeg libraries. 
It supports conversions of different audio formats at a time and the ability 
to convert even groups of files in a directory, saving the output in a specific 
folder.

## Dependencies  

- python >=3.6   
- flac   
- lame   
- vorbis-tools *(include: oggenc, oggdec)*   
- shntool   
- ffmpeg   
- mac *(monkey's-audio, name depends to your O.S., try search: libmac2, mac)*   

## Usage

```
audiomass [-h HELP] [-v VERSION] [-C COPYING] [-c CHECK]
[-f FILE {..FILENAME}]
[-d DIRECTORY {..DIRNAME}]
[-b BATCH {..FILENAME_1 ..FILENAME_2 ..FILENAME_3 ..}] 
[-o OUTPUT {..DIRNAME}]
```   
  
Optional arguments:   

  `-f  --file`     Convert only one audio file at a time.   
  `-d, --dir`      Converts a bunch of audio files contained in a directory.   
  `-b, --batch`    Convert a queue of files even with different formats.   
  `-o  --output`   Save the output files to a specified folder.   
  `-c, --check`    Check of available audio libraries used by audiomass   
  `-h, --help`     print this help and exit   
  `-v, --version`  print version and date and exit   
  `-C, --copying`  print license and exit   

## Examples 

Convert a single audio file and save it into same directory:   

`audiomass -f '/home/Name/my Music/audiofile.wav'`   

Convert a bunch of audio files inside a folder and save them in another folder:   

`audiomass -d /MyDirName/Music -o '/MyOtherDir/converted'`   

Convert a queue of audio files and save them in a specified folder:   

`audiomass -b '..FILE 1.wav' '..FILE 2.mp3' '..FILE 3.flac' '...' -o '/MyOtherDir/converted'`

## Installation

`python3 -m pip install audiomass`   

## License and Copyright

Copyright © 2010 - 2021 Gianluca Pernigotto   
Author and Developer: Gianluca Pernigotto   
Mail: <jeanlucperni@gmail.com>   
License: GPL3 (see LICENSE file in the docs folder)   
