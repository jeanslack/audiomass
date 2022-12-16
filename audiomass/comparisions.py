# -*- coding: utf-8 -*-
"""
Name:         comparisions.py (module)
Porpose:      module for output strings commands and formats comparisions
Writer:       Gianluca Pernigoto <jeanlucperni@gmail.com>
Copyright:    (c) 2015/2022 Gianluca Pernigoto <jeanlucperni@gmail.com>
license:      GPL3
Rev:          Dec 16 2022
Code checker: flake8, pylint
"""


def text_menu():
    """
    Returns a pre-formatted list of string items of audio formats.
    To index this list do:

    ```
    menu = text_menu()
    if indexes:  # get from input_formats() function below
        setmenu = [menu[i] for i in range(len(menu)) if i not in set(indexes)]
        for items in setmenu:
            print(items)
    ```
    The example above prints all items minus those of the
    indexes var, in this case removes index(3) .

    Also, see `output_formats() function.

    """
    return (
      "------------",
      " \033[1m 1 \033[0m> WAV   (WAVEform audio format, PCM uncompresed)",
      " \033[1m 2 \033[0m> AIFF  (Apple Interchange File Format)",
      " \033[1m 3 \033[0m> FLAC  (Free Lossless Audio Codecs)",
      " \033[1m 4 \033[0m> MP3   (MPEG-1 Audio Layer 3)",
      " \033[1m 5 \033[0m> OGG   (ogg-vorbis lossy format)",
      "------------",
      " \033[41;37;1m A \033[0m \033[1m..ABORT\033[0m",
      "------------")


def output_formats():
    """
    Return a tupla of supported output format to conversion.
    If you plan to extend support for program output formats,
    you should start here and add the new format to the
    text_menu() function in the same indexing order of
    output_formats().

    """
    return 'wav', 'aiff', 'flac', 'mp3', 'ogg'


def input_formats():
    """
    Returns a sequence of the currently supported input
    formats. Each item of the sequence contains two items
    of type tuple: format(s) and the associative indices
    for use with the text menu.
    If you plan to extend support for program input formats,
    you should start here.

    Usage example:
    ```
    for formats in input_formats():
        if 'mp3' in formats[0]:
            indexes = formats[1]  # list of output formats indexes for menu
            break
        else:
            indexes = None

    menu = text_menu()
    setmenu = [menu[i] for i in range(len(menu)) if i not in set(indexes)]

    for outformat in setmenu:
        print(outformat)
        #  or `msgcustom(f"{outformat}")`
    ```
    Also, see `text_menu()` function.

    """
    return (
        (('wav', 'wave',), (1,)),
        (('aiff', 'aif', 'aifc',), (2,)),
        (('flac',), (3,)),
        (('ape',), (3, 4, 5)),
        (('mp3',), (3, 4, 5)),
        (('ogg', 'oga', 'spx',), (3, 4, 5))
           )


def comparing(pair):
    """
    Returns the required values (codec data) for each pair
    of audio formats. Accept one only string argument in
    this form:

        pair = `inputformat > outputformat`

    if no pair match with keys of `object_assignment` dict,
    it returns `None`

    Example:

    ```
    # to get data to convert files from wav format to mp3:
    comparing('wav > mp3')
    ```

    Note, you can implement new audio formats
    modules by editing this file.
    """

    # ------------------------------  BITRATES MENU:
    flac_menu = (
                "\n\033[1m"
                "Choose the quality for Flac format:\033[0m\n"
                "  0 = low compression > more access space > better quality\n"
                "  1\n"
                "  2\n"
                "  3\n"
                "  4 = Great quality/compression ratio\n"
                "  5 = default\n"
                "  6\n"
                "  7\n"
                "  8 = maximum compression > less space > lower quality\n"
                )
    mp3_menu = ("\n\033[1m"
                "Choose the quality and bit-rate for MP3 format:\033[0m\n"
                "  0     medium    >  VBR 92 kbit\n"
                "  1     standard  >  VBR 112 kbit/s\n"
                "  2     extreme   >  VBR 150 kbit/s\n"
                "  3     insane    >  CBR 320 kbit/s\n\n"
                )
    ffmpeg_mp3_menu = (
                "\n\033[1m"
                "Choose the quality and bitrate for MP3 format:\033[0m\n"
                "  0     >  VBR 128 kbit\n"
                "  1     >  VBR 160 kbit/s\n"
                "  2     >  VBR 192 kbit/s\n"
                "  3     >  VBR 260 kbit/s\n"
                "  4     >  CBR 320 kbit/s\n"
                )
    ogg_menu = ("\n\033[1m"
                "Choose the quality and bit-rate for OGG format:\033[0m\n"
                "  1    >   80 kbit        |     6   >   192 kbit/s\n"
                "  2    >   92 kbit/s      |     7   >   200 kbit/s\n"
                "  3    >   100 kbit/s     |     8   >   260 kbit/s\n"
                "  4    >   128 kbit/s     |     9   >   320 kbit/s\n"
                "  5    >   134 kbit/s     |     10  >   520 kbit/s\n"
                )
    ffmpeg_ogg_menu = (
                "\n\033[1m"
                "Choose the quality and bit-rate for OGG format:\033[0m\n"
                "  0    >  VBR 128 kbit\n"
                "  1    >  VBR 160 kbit/s\n"
                "  2    >  VBR 192 kbit/s\n"
                "  3    >  VBR 260 kbit/s\n"
                "  4    >  CBR 320 kbit/s\n"
                )

    # ----------------------------- BITRATES LEVELS:

    flac_opt_comp = {"0": "-0", "1": "-1", "2": "-2", "3": "-3",
                     "4": "-4", "5": "-5", "6": "-6", "7": "-7",
                     "8": "-8"
                     }
    mp3_opt_comp = {"0": "--preset medium", "1": "--preset standard",
                    "2": "--preset extreme", "3": "--preset insane"
                    }
    ffmpeg_mp3_opt_comp = {"0": "-acodec libmp3lame -b:a 128k -ar 44100",
                           "1": "-acodec libmp3lame -b:a 160k -ar 44100",
                           "2": "-acodec libmp3lame -b:a 192k -ar 44100",
                           "3": "-acodec libmp3lame -b:a 260k -ar 44100",
                           "4": "-acodec libmp3lame -b:a 320k -ar 44100",
                           }
    ogg_opt_comp = {"1": "-q 1", "2": "-q 2", "3": "-q 3", "4": "-q 4",
                    "5": "-q 5", "6": "-q 6", "7": "-q 7", "8": "-q 8",
                    "9": "-q 9", "10": "-q 10"
                    }
    ffmpeg_ogg_opt_comp = {"0": "-vn -acodec libvorbis -ar 44100 -ab 128k",
                           "1": "-vn -acodec libvorbis -ar 44100 -ab 160k",
                           "2": "-vn -acodec libvorbis -ar 44100 -ab 192k",
                           "3": "-vn -acodec libvorbis -ar 44100 -ab 260k",
                           "4": "-vn -acodec libvorbis -ar 44100 -ab 320k",
                           }

    # -------------------------------  PAIRING FORMATS:

    object_assignment = {
        'wav > aiff': ('ffmpeg', None, None, None, 'aiff'),
        'aiff > wav': ('ffmpeg', None, None, None, 'wav'),
        'flac > wav': ('ffmpeg', None, None, None, 'wav'),
        'flac > aiff': ('ffmpeg', None, None, None, 'aiff'),
        'wav > flac': ('flac', flac_opt_comp, flac_menu, 'Type the '
                       'compression level in digits 0 to 8, and press '
                       'enter key > ', 'flac'
                       ),
        'aiff > flac': ('flac', flac_opt_comp, flac_menu, 'Type the '
                        'compression level in digits 0 to 8, and press '
                        'enter key > ', 'flac'
                        ),
        'wav > mp3': ('lame', mp3_opt_comp, mp3_menu, 'Type the compression '
                      'level in digits 0 to 3, and press enter key > ', 'mp3'
                      ),
        'aiff > mp3': ('lame', mp3_opt_comp, mp3_menu, 'Type the compression '
                       'level in digits 0 to 3, and press enter key > ',
                       'mp3'
                       ),
        'mp3 > wav': ('lame --decode', None, None, None, 'wav'),
        'wav > ogg': ('oggenc', ogg_opt_comp, ogg_menu, 'Type the compression '
                      'level in digits 1 to 10, and press enter key > ',
                      'ogg'
                      ),
        'aiff > ogg': ('oggenc', ogg_opt_comp, ogg_menu, 'Type the '
                       'compression level in digits 1 to 10, and press '
                       'enter key > ', 'ogg'
                       ),
        'flac > ogg': ('oggenc', ogg_opt_comp, ogg_menu, 'Type the '
                       'compression level in digits 1 to 10, and press '
                       'enter key > ', 'ogg'
                       ),
        'ogg > wav': ('oggdec', None, None, None, 'wav'),
        'flac > mp3': ('ffmpeg', ffmpeg_mp3_opt_comp, ffmpeg_mp3_menu,
                       'Type the compression level in digits 0 to 4, '
                       'and press enter key > ',
                       'mp3'
                       ),
        'ape > mp3': ('ffmpeg', ffmpeg_mp3_opt_comp, ffmpeg_mp3_menu,
                      'Type the compression level in digits 0 to 4, '
                      'and press enter key > ',
                      'mp3'
                      ),
        'ape > ogg': ('ffmpeg', ffmpeg_ogg_opt_comp, ffmpeg_ogg_menu,
                      'Type the compression level in digits 0 to 4, '
                      'and press enter key > ',
                      'ogg'
                      ),
        'ape > wav': ('ffmpeg', None, None, None, 'wav'),
        'ape > aiff': ('ffmpeg', None, None, None, 'aiff'),
        'mp3 > aiff': ('ffmpeg', None, None, None, 'aiff'),
        'ogg > aiff': ('ffmpeg', None, None, None, 'aiff'),
        }
    return object_assignment.get(pair)
