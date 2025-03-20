#! /usr/bin/python3

import os
import sys
import socket
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
from tkinter import filedialog, Tk
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def get_local_ip():
    """Retrieve the local IP address."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
        except Exception:
            return "127.0.0.1"

def choose_directory():
    """Allow the user to select a directory for sharing."""
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected if folder_selected else os.getcwd()

class ShareFolder:
    """Class to handle the file-sharing server."""
    
    def __init__(self, port=8080):
        self.current_directory = choose_directory()
        os.chdir(self.current_directory)
        self.port = port
        self.green = Fore.GREEN
        self.red = Fore.RED
        self.reset = Style.RESET_ALL
    
    def setup(self):
        """Prompt user for a custom port if needed."""
        try:
            user_input = input(f"{self.red}[!] Sharing: \"{self.current_directory}\" on the local network.{self.reset}\nEnter port (default: {self.port}): ")
            if user_input.strip():
                self.port = int(user_input)
        except KeyboardInterrupt:
            print(f"{self.red}\n[-] Operation canceled by the user.{self.reset}")
            sys.exit(1)
    
    def server(self):
        """Start the HTTP server."""
        try:
            server_address = ("", self.port)
            httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
            print(f"{self.green}[+] Server running at: http://{get_local_ip()}:{self.port}{self.reset}")
            httpd.serve_forever()
        except OSError as e:
            print(f"{self.red}[-] Error: {e}{self.reset}")
            sys.exit(1)
        except KeyboardInterrupt:
            print(f"{self.red}\n[-] Server stopped by user.{self.reset}")
            httpd.shutdown()
            sys.exit(0)
    
    def run(self):
        """Run the file-sharing server."""
        self.setup()
        self.server()

if __name__ == '__main__':
    app = ShareFolder()
    app.run()
