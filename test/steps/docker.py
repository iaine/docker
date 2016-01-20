'''
   Simple Docker testing
'''
from subprocess import Popen, PIPE

class BDDDocker():
    '''
       Class to run the Docker image to test it. 
       This is smoke testing that packages exist. 
    '''

    def __init__(self, image_name):
        '''
           Initialise the variables
        '''
        self.command = None
        self.image = image_name

    def image_build(self, build_dir):
        '''
           Run the image build
        '''
        out = Popen('docker build -t %s %s'%(self.name, build_dir), stdout=PIPE, stderr=PIPE)
    
    def image_start(self):
        '''
           Start the image
        '''
        start = self.build_command()
        self._command(start)

    def image_stop(self):
        '''
           Stop the image
        '''
        self._command("docker stop %s"% self.image)

    def system_distribution(self, distribution):
        '''
           Checks for the distribution
           Returns a string
        '''
        release = self._command("lsb_release -i")
        return release.split(':')[1]

    def system_package(self, package):
        '''
           Checks for a system package to be installed. 
           Returns a boolean
        '''
        p = self.build_command("dpkg-query -l '" + package + "' | grep '^.i' | cut -d ' ' -f 3")
        packages = self._command(p)
        if package in packages:
            return True
        else:
            return False

    def _command(self, command):
        '''
           Run the command
        '''
        p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
        return p.stdout.read()

    def build_command(self, commandstr):
        '''
           Build the command string
        ''' 
        cmd = "docker run -ti " + self.image + " /bin/bash "
        if commandstr is not None:
            cmd += "| " + commandstr
        print(cmd)
        return cmd

