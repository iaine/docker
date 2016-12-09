'''
   Gets the Operating System details
'''

import os

class OS_Environment():
    '''
       Gets the OS environment
    '''
    def __init__(self):
        self.uname = os.uname()

    def get_os_name(self):
        '''
          Gets the name of OS
        '''
        return self.uname[0]

    def get_os_build(self):
        '''
           Gets the build of the OS
        '''
        return self.uname[3]

    def get_os_kernel(self):
        '''
           Gets the kernel of the OS
        '''
        return self.uname[2] 

    def get_os_arch(self):
        '''
           Get the architecture of the OS
        '''
        return self.uname[4]

class Container_Environment():
    '''
       Get the Docker information
    '''


    def get_docker_version():
        '''
          Get the Dokcer version
        '''
        return '1.12.1'
