'''
   Script to check the checksum for the tarred version of the container
'''

import glob
import hashlib
import sys
import tarfile

def untar(fname, depth=1):
    '''
       Untarring the file
    '''
    open_tar = tarfile.open(fname)
    
    if depth == 1:
        open_tar.extractall()
        open_tar.close()
        [ glob.glob('*.tar', 2)]


if __name__ == '__main__':
    docker_tar = sys.argv[1]
    untar(docker_tar, 1)
