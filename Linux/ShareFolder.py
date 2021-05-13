#! /usr/bin/python3

from os import chdir, getcwd, system
from http.server import HTTPServer, CGIHTTPRequestHandler

# Import external modules
try:
    from FindMyIP import internal
except ModuleNotFoundError:
    system("pip install FindMyIP")
    from FindMyIP import internal

try:
    from colorama import init, Fore
    init(autoreset=True)
except ModuleNotFoundError:
    system("pip install colorama")
    from colorama import init, Fore
    init(autoreset=True)


class ShareFile:
    def __init__(self): 
        self.current_directory = getcwd()
        self.__port__ = int(input(f"[!] You Are sharing \"{self.current_directory}\" on your local network.\nEnter Your port here: "))

        self.green = Fore.GREEN
        self.red = Fore.RED
        self.reset = Fore.RESET

    def __server__(self):
        chdir(".")
        self.server = HTTPServer(("", self.__port__), CGIHTTPRequestHandler)
        print(f"Server is online on {self.green}{internal()}{self.reset}:{self.red}{self.__port__}")

    def run(self): 
        self.__server__()
        self.server.serve_forever()

if __name__ == '__main__':
    app = ShareFile()
    app.run()
    
