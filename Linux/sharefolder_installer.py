import re
from os.path import isfile
from os import WIFSTOPPED, getuid, system
from shutil import copyfile
from socket import gethostname


class sharefolder:
    def __init__(self): 
        self.ok = '\033[92m' #GREEN
        self.progess = "\033[034m"
        self.fail = '\033[31m' #RED
        self.reset = '\033[0m' #RESET COLOR
        self.__path__ = '/usr/local/bin/ShareFolder.py'


        # check root or not 
        if not getuid() == 0:
            print(f'{self.fail}[E]{self.reset} This script must be run as root!')

        elif getuid() == 0:
            print(f"{self.ok}[ OK ]{self.reset} Start installation ..")
            self.install()


    def __bashrc__(self):   
        # open bashrc and read | write  
        echo_command = f"alias sharefolder='python3 {self.__path__}'"    
        with open('/root/.bashrc', 'r+') as bashrc_write: 
            if echo_command in bashrc_write.read(): 
                bashrc_write.close()
                return True
            elif echo_command not in bashrc_write.read(): 
                bashrc_write.write(echo_command)
                bashrc_write.close()
                return False


    def __steps__(self): 
        # check ShareFolder.py 
        if isfile(self.__path__) and self.__bashrc__() is True:
            print(f"{self.ok}[ OK ]{self.reset} The program is already installed :)")

        elif not isfile(self.__path__) and self.__bashrc__() is False:

            self.__ad__ = re.search(r"/(.*?)ShareFolder.py", self.__path__).group(1)
            print(f"{self.progess}[ INSTALL ]{self.reset} Copying File in System ... -> /{self.__ad__}")
            
            copyfile('./ShareFolder.py', self.__path__)
            print(f"{self.progess}[ INSTALL ]{self.reset} Set command in the system -> /root/.bashrc")
            
            self.__bashrc__()

            print(f"{self.ok}[ OK ]{self.reset} The program was successfully installed :)")
            print(f"{self.progess}[ OK ]{self.reset} Restart you terminal")


    def install(self):
        self.__steps__()

sharefolder()