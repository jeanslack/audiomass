
# Audiomass - wrapper for multiple audio conversion libraries.

**Audiomass** is a command line audio wrapper of the Flac, Lame, Vorbis-tools, 
Monkey's Audio, Shntool and FFmpeg libraries. 
It supports conversions of different audio formats at a time and the ability 
to convert even groups of files in a directory, saving the output in a specific 
folder.

## Dependencies  

- python >=3.5.3   
- flac   
- lame   
- vorbis-tools *(include: oggenc, oggdec)*   
- shntool   
- ffmpeg   
- mac *(monkey's-audio, name depends to your O.S., try search: libmac2, mac)*   

## Usage

```
audiomass [-h HELP] [-v VERSION] [-c COPYING] [-C CHECK]
[-f FILE {..FILENAME}]
[-d DIRECTORY {..DIRNAME}]
[-b BATCH {..FILENAME_1 ..FILENAME_2 ..FILENAME_3 ..}] 
[-o OUTPUT {..DIRNAME}]
```   
  
Optional arguments:   

  `-f  --file`     single audio conversion.   
  `-d, --dir`      specifies a directory to process   
  `-b, --batch`    run a process for different queued file formats   
  `-o  --output`   save the output into specified folder   
  `-C, --check`    Check for required dependencies   
  `-h, --help`     print this help and exit   
  `-v, --version`  print version and date and exit   
  `-c, --copying`  print license and exit   

## Examples 

Convert a single file and save it into same directory:   

`audiomass -f '/home/Name/my Music/audiofile.wav'`   

Convert a bunch of audio files and save them in a specified folder:   

`audiomass -d /MyDirName/Music -o '/MyOtherDir/converted`   

Convert a queue of audio files and save the output in the specified folder:   

`audiomass -b '..STREAM1.wav' '..STREAM2.mp3' '..STREAM3.flac' '...' -o /output/dir`

## Installation

`pip install audiomass`   

## License and Copyright

Copyright © 2010 - 2020 Gianluca Pernigotto   
Author and Developer: Gianluca Pernigotto   
Mail: <jeanlucperni@gmail.com>   
License: GPL3 (see LICENSE file in the docs folder)   
