
import os
from shutil import which

def check_dependencies(arg=None):
    """
    Check for dependencies into your system (compatible with Linux, 
    MacOsX, Windows)
    When not arg, print a list of all required dependencies, otherwise accept
    *one* name only to pass at the function parameter and return *None* if 
    not exist or return its executable path-name.
    """
    if not arg:
        listing = ['ffmpeg', 'flac', 'lame', 'oggdec', 'oggenc', 
                   'shntool', 'mac']
        #listing = ['sox', 'wavpack']# this are for futures implementations
        for required in  listing:
            #if which(required):
            if which(required, mode=os.F_OK | os.X_OK, path=None):
                print ("Check for: '%s' ..Ok" % required)
            else:
                print ("Check for: '%s' ..Not Installed" % required)
    else:
        return which(arg, mode=os.F_OK | os.X_OK, path=None)

