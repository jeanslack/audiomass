
# Audiomass - audio conversion utility.

**Audiomass-cli** is a command line wrapper that interfaces on differents 
audio codecs for multiple input data streams conversions. It can be easily 
implemented with other audio library codecs and currently supports: Flac, 
Lame, Vorbis-tools, Monkey's Audio, Shntool and FFmpeg, etc.

## Essential Dependencies

**Required:**   

- python >=3.5.3   

**Recommended:**   

- flac   
- lame   
- vorbis-tools *(include: oggenc, oggdec)*   
- shntool   
- ffmpeg   
- mac *(monkey's-audio, name depends to your O.S., try search: libmac2, mac)*   

## Usage

usage: `audiomass [-h HELP] [-v VERSION] [-c COPYING] [-C CHECK] [-f FILE] [-d DIRECTORY] [-b BATCH] [..FILE1 ..FILE2 ..FILE3 ..]] [-o DIRNAME]`   
  
Optional arguments:   

  `-f  --file`     single audio stream conversion.   
  `-d, --dir`      specifies a directory to process   
  `-b, --batch`    run a process for different queued file formats   
  `-o  --output`   write the output streams into specified folder   
  `-C, --check`    Check for required dependencies   
  `-h, --help`     print this help and exit   
  `-v, --version`  print version and date and exit   
  `-c, --copying`  print license and exit   

## Examples 

Convert a single file and write into same directory:   

`audiomass -f '/home/Name/my Music/audiofile.wav'`   

Convert a group of audio stream and put output stream into specified folder:   

`audiomass-cli -d /MyDirName/Music -o '/MyOtherDir/converted`   

Convert a queue audio streams and put output stream into specified folder:   

`audiomass -b '..STREAM1.wav' '..STREAM2.mp3' '..STREAM3.flac' '...' -o /output/dir`

## Installation

`pip install audiomass`   

## License and Copyright

Copyright © 2010 - 2019 Gianluca Pernigotto   
Author and Developer: Gianluca Pernigotto   
Mail: <jeanlucperni@gmail.com>   
License: GPL3 (see LICENSE file in the docs folder)   
