
# Audiomass - wrapper for multiple audio conversion libraries.

**Audiomass** is a command line audio wrapper of the Flac, Lame, Vorbis-tools, 
Monkey's Audio, Shntool and FFmpeg libraries. 
It supports conversions of different audio file formats at a time and the ability 
to convert even groups of files in a directory, saving the output in a specific 
folder.

For each input file, audiomass writes to a filename based on the name of the
input file. If the (**-o**) option is not specified, it save any file at
same destination as input file.

It is possible to choose one or more conversion formats, based on the imported
files, and then choose the respective bitrates.

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
audiomass [-h]
          [--version]
          [-c]
          [-d INPUT_FOLDER, --directory INPUT_FOLDER]
          [-f FILE [FILE.. FILE.. ...], --files FILE [FILE.. FILE.. ...]]
          [-o OUTPUT_FOLDER, --output OUTPUT_FOLDER]
```   

## Examples 

Convert a single audio file and save it into same directory:   

`audiomass -f '/home/Name/my Music/audiofile.wav'`   

Convert a bunch of audio files inside a folder and save them in another folder:   

`audiomass -d '/MyDirName/Music' -o '/MyOtherDir/converted'`   

Convert a queue of audio files and save them in a specified folder:   

`audiomass -f '..FILE 1.wav' '..FILE 2.mp3' '..FILE 3.flac' '...' -o '/MyOtherDir/converted'`

## Installation

`python3 -m pip install audiomass`   

## License and Copyright

Copyright © 2010 - 2021 Gianluca Pernigotto   
Author and Developer: Gianluca Pernigotto   
Mail: <jeanlucperni@gmail.com>   
License: GPL3 (see LICENSE file in the docs folder)   
