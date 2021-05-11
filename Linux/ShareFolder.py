#! /usr/bin/python3

from os import chdir, getcwd
from http.server import HTTPServer, CGIHTTPRequestHandler


class ShareFile:
    def __init__(self): 
        self.current_directory = getcwd()
        self.__port__ = int(input(f"[!] You Are sharing \"{self.current_directory}\" on your local network.\nEnter Your port here: "))
       
        self.ok = '\033[92m' #GREEN
        self.fail = '\033[31m' #RED
        self.reset = '\033[0m' #RESET COLOR


    def __color__green__(self, text): 
        return self.ok + text + self.reset 


    def __server__(self):
        chdir(".")
        self.server = HTTPServer(("", self.__port__), CGIHTTPRequestHandler)
        print(f"Server is online on 127.0.0.1:{self.__color__green__(f'{self.__port__}')}")


    def run(self): 
        self.__server__()
        self.server.serve_forever()


if __name__ == '__main__':
    app = ShareFile()
    app.run()