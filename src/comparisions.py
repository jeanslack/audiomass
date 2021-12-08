# -*- coding: utf-8 -*-
"""
Name:         comparisions.py (module)
Porpose:      module for output strings commands and formats comparisions
Writer:       Gianluca Pernigoto <jeanlucperni@gmail.com>
Copyright:    (c) 2015/2016 Gianluca Pernigoto <jeanlucperni@gmail.com>
license:      GPL3
Rev:          Dec 08 2021
Code checker: flake8, pylint
"""
import os


def graphic_menu():
    """
    Menu for output audio selection format used from all process(f,d,b)

    """
    return [
      "------------",
      " \033[1m 1 \033[0m> Wav   (WAVEform audio format, PCM uncompresed)",
      " \033[1m 2 \033[0m> Aiff  (Apple Interchange File Format)",
      " \033[1m 3 \033[0m> Flac  (Free Lossless Audio Codecs)",
      " \033[1m 4 \033[0m> Ape   (Monkey's audio)",
      " \033[1m 5 \033[0m> Mp3   (MPEG-1 Audio Layer 3)",
      " \033[1m 6 \033[0m> Ogg   (ogg-vorbis lossy format)",
      "------------",
      " \033[41;37;1m A \033[0m \033[1m..ABORT\033[0m",
      "------------"]


def supported_formats():
    """
    supported_format: it is useful to limit the choices within
    the available options of the graphic_menu.

    """
    return {'1': (1, 'WAV', 'wav', [1]),
            '2': (2, 'AIFF', 'aiff', [2, 4]),
            '3': (3, 'FLAC', 'flac', [3]),
            '4': (4, 'APE', 'ape', [3, 4]),
            '5': (5, 'MP3', 'mp3', [3, 4, 5, 6]),
            '6': (6, 'OGG', 'ogg', [3, 4, 5, 6]),
            }


def comparision(pair):
    """
    returns the required values for each pair of audio formats.
    Accept one only string argument in this form: 'example > example'.
    You can add or remove new formats modules from here.

    """

    # ###------------------------------  BITRATES MENU:
    flac_menu = (
                "\n\033[1m"
                "References on quality for Flac format:\033[0m\n"
                "  0 = low compression > more access space > better quality\n"
                "  1\n"
                "  2\n"
                "  3\n"
                "  4 = Great quality/compression ratio\n"
                "  5 = Is the default compression \n"
                "  6\n"
                "  7\n"
                "  8 = maximum compression > less space > lower quality\n"
                )

    ape_menu = ("\n\033[1m"
                "References on quality for Ape format:\033[0m\n"
                "  1    -c1000 = Fast (Best quality)\n"
                "  2    -c2000 = Normal\n"
                "  3    -c3000 = High\n"
                "  4    -c4000 = Extra\n"
                "  5    -c5000 = Insane\033[0m\n"
                )

    mp3_menu = ("\n\033[1m"
                "References on quality and bit-rate for MP3:\033[0m\n"
                "  0     medium    >  VBR 92 kbit\n"
                "  1     standard  >  VBR 112 kbit/s\n"
                "  2     extreme   >  VBR 150 kbit/s\n"
                "  3     insane    >  CBR 320 kbit/s\n\n"
                )

    ffmpeg_mp3_menu = ("\n\033[1m"
                       "References on quality and bit-rate for MP3:\033[0m\n"
                       "  0     >  VBR 128 kbit\n"
                       "  1     >  VBR 160 kbit/s\n"
                       "  2     >  VBR 192 kbit/s\n"
                       "  3     >  VBR 260 kbit/s\n"
                       "  4     >  CBR 320 kbit/s\n"
                       )

    ogg_menu = ("\n\033[1m"
                "References on the quality and bit-rate for OGG:\033[0m\n"
                "  1    >   80 kbit        |     6   >   192 kbit/s\n"
                "  2    >   92 kbit/s      |     7   >   200 kbit/s\n"
                "  3    >   100 kbit/s     |     8   >   260 kbit/s\n"
                "  4    >   128 kbit/s     |     9   >   320 kbit/s\n"
                "  5    >   134 kbit/s     |     10  >   520 kbit/s\n"
                )

    ffmpeg_ogg_menu = (
                "\n\033[1m"
                "References on the quality and bit-rate for OGG:\033[0m\n"
                "  0    >  VBR 128 kbit\n"
                "  1    >  VBR 160 kbit/s\n"
                "  2    >  VBR 192 kbit/s\n"
                "  3    >  VBR 260 kbit/s\n"
                "  4    >  CBR 320 kbit/s\n"
                )

    # ### ----------------------------- BITRATES LEVELS:

    flac_opt_comp = {"0": "-0", "1": "-1", "2": "-2", "3": "-3",
                     "4": "-4", "5": "-5", "6": "-6", "7": "-7",
                     "8": "-8"
                     }
    ape_opt_comp = {"1": "-c1000", "2": "-c2000", "3": "-c3000",
                    "4": "-c4000", "5": "-c5000"
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
    # ###-------------------------------  PAIRING ASSOCIATIONS FORMATS:
    object_assignment = {
        'wav > aiff': ('shntool', None, None, None, 'aiff'),
        'aiff > wav': ('shntool', None, None, None, 'wav'),
        # 'aiff > ape': ('shntool', None, None, None, 'ape'),
        'flac > wav': ('shntool', None, None, None, 'wav'),
        'flac > aiff': ('shntool', None, None, None, 'aiff'),
        'flac > ape': ('shntool', None, None, None, 'ape'),
        'ape > wav': ('shntool', None, None, None, 'wav'),
        'ape > aiff': ('shntool', None, None, None, 'aiff'),
        # 'ape > flac': ('shntool', None, None, None, 'flac'),

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
        'wav > ape': ('mac', ape_opt_comp, ape_menu, 'Type the compression '
                      'level in digits 1 to 5, and press enter key > ',
                      'ape'
                      ),
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
        'mp3 > aiff': ('ffmpeg', None, None, None, 'aiff'),
        'ogg > aiff': ('ffmpeg', None, None, None, 'aiff'),
        }
    return object_assignment.get(pair, 'key_error')


def build_cmd(id_codec, bitrate, path_name, norm):
    """
    Since each command associated with a type of codec appears to be
    different, the key of the 'command_dict' must match with
    the first value of the 'object assignment' dictionary.

    This function Return a string with the command correctly formed.

    The parameters accepted are:

    - id_codec: key of the command_dict
    - bitrate: str('value')
    - path_name: str('/dirname/filename.input_format')
    - norm: str('/dirname/filename.output_format')

    """
    output_format = os.path.splitext(os.path.basename(norm))[1]
    dirname = os.path.dirname(norm)
    command_dict = {
        'flac': f'flac -V {bitrate} "{path_name}" -o "{norm}"',
        'lame': f'lame --nohist {bitrate} "{path_name}" "{norm}"',
        'lame --decode': f'lame --decode "{path_name}" "{norm}"',
        'oggenc': f'oggenc {bitrate} "{path_name}" -o "{norm}"',
        'mac': f'mac "{path_name}" "{norm}" {bitrate}',
        'ffmpeg': f'ffmpeg -i "{path_name}" {bitrate} "{norm}"',
        'oggdec': f'oggdec "{path_name}" -o "{norm}"',
        'shntool': (f'shntool conv -o {output_format.split(".")[1]} '
                    f'-O always "{path_name}" -d "{dirname}"')
                    }

    return command_dict[id_codec]
