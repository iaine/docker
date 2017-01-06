import subprocess

class Container_Environment():
    '''
       Get the Docker information
    '''
    def __init__ (self):
        _dock = subprocess.check_output(["docker", "version"]).decode('utf8')
        d = _dock.split('\n\n')
        self.client={}
        dock = d[0].split('\n')
        for i in dock[1:]:
            _tmp = i.split(':')
            self.client[_tmp[0].strip()] = str(_tmp[1].strip())

    def get_docker_version(self):
        '''
          Get the Docker version
        '''
        return self.client['Version']

    def get_docker_api(self):
        return self.client['API version']


    def get_docker_go(self):
        return self.client['Go version']

    def get_docker_git(self):
        return self.client['Git commit']

    def get_docker_os(self):
        return self.client['OS/Arch']
