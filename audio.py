#!/usr/bin/python
# -*- coding: UTF-8 -*-
#

import os
import os.path

path = '/home/gianluca/Musica'

filenames = [filename for filename in os.listdir(path) 
			 if filename.endswith('.wav')
			 ]

print filenames


################# NOTE this is original, do not touch it
#import os
#import os.path
#import sys
#from subprocess import call

#def main():
    #path = '/path/to/directory/'
    #filenames = [
        #filename
        #for filename
        #in os.listdir(path)
        #if filename.endswith('.wav')
        #]
    #for filename in filenames:
        #call(['lame', '-V0',
              #os.path.join(path, filename),
              #os.path.join(path, '%s.mp3' % filename[:-4])
              #])
    #return 0

#if __name__ == '__main__':
    #status = main()
    #sys.exit(status)
################ NOTE end
