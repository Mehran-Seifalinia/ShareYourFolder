from re import search
from os.path import isfile
from os import getuid
from subprocess import run


class ShareFolderInstaller:
    def __init__(self): 
        self.ok = '\033[92m' #GREEN
        self.progess = "\033[034m"
        self.fail = '\033[31m' #RED
        self.reset = '\033[0m' #RESET COLOR
        self.__path__ = '/usr/local/bin/ShareFolder.py'


        # check root or not 
        if not getuid() == 0:
            print(f'{self.fail}[E]{self.reset} This script must be run as root!')
        else:
            print(f"{self.ok}[ OK ]{self.reset} Start installation ..")
            self.install()


    def __bashrc__(self):   
        try:
            # open bashrc and read/write  
            echo_command = f"alias sharefolder='python3 {self.__path__}'"    
            with open('/root/.bashrc', 'r+') as bashrc_write: 
                if echo_command in bashrc_write.read(): 
                    bashrc_write.close()
                    return True
                else:
                    # If the alias is not present, write it to the bashrc
                    bashrc_write.write(echo_command)
                    bashrc_write.close()
                    return False
        except Exception as error:
            print(f"{self.fail}[!] Error:{self.reset} {error}")
            exit(1)


    def __steps__(self): 
        try:
            # Check if ShareFolder.py and the alias are already installed 
            if isfile(self.__path__) and self.__bashrc__() is True:
                print(f"{self.ok}[ OK ]{self.reset} The program is already installed :)")
            
            # Install ShareFolder.py and set the alias in bashrc if they are not already present
            elif not isfile(self.__path__) and self.__bashrc__() is False:
                self.__ad__ = search(r"/(.*?)ShareFolder.py", self.__path__).group(1)
                print(f"{self.progess}[ INSTALL ]{self.reset} Copying File in System ... -> /{self.__ad__}")
                
                # Use subprocess to copy the file, providing more control over the process
                run(['cp', './ShareFolder.py', self.__path__])
                print(f"{self.progess}[ INSTALL ]{self.reset} Set command in the system -> /root/.bashrc")
                self.__bashrc__()
                print(f"{self.ok}[ OK ]{self.reset} The program was successfully installed :)\n{self.progess}[ OK ]{self.reset} Restart you terminal")
        except Exception as error:
            print(f"{self.fail}[!] Error:{self.reset} {error}")
            exit(1)

    def install(self):
        self.__steps__()

ShareFolderInstaller()
