#!/usr/bin/python3

from os import chdir, getcwd
from socket import socket, AF_INET, SOCK_DGRAM
from http.server import HTTPServer, SimpleHTTPRequestHandler
from tkinter import filedialog, Tk
from sys import exit
from colorama import init as colorama_init, Fore, Style

# Initialize colorama
colorama_init(autoreset=True)

def get_local_ip():
    """Retrieve the local IP address."""
    with socket(AF_INET, SOCK_DGRAM) as s:
        try:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
        except Exception:
            return "127.0.0.1"

def choose_directory():
    """Allow the user to select a directory for sharing using a graphical dialog."""
    root = Tk()
    root.withdraw()  # Hide the root window
    folder_selected = filedialog.askdirectory(title="Select Folder to Share")
    return folder_selected if folder_selected else getcwd()

class ShareFolder:
    """Class to handle the file-sharing server."""

    def __init__(self, port=80):
        self.current_directory = choose_directory()
        chdir(self.current_directory)
        self.port = port
        # Color setup for messages
        self.white = Fore.WHITE
        self.red = Fore.RED
        self.green = Fore.GREEN
        self.reset = Style.RESET_ALL

    def setup(self):
        """Prompt user for a custom port if needed via input."""
        user_input = input(f"{self.green}Sharing: \"{self.current_directory}\"\nEnter port (default: {self.port}): {self.reset}")
        if user_input.strip():
            try:
                self.port = int(user_input.strip())
            except ValueError:
                print(f"{self.red}Invalid port. Using default: {self.port}{self.reset}")

    def server(self):
        """Start the HTTP server."""
        try:
            server_address = ("", self.port)
            httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
            print(f"{self.green}Server running at: http://{get_local_ip()}:{self.port}{self.reset}")
            httpd.serve_forever()
        except OSError as e:
            print(f"{self.red}Error: {e}{self.reset}")
            exit(1)
        except KeyboardInterrupt:
            print(f"{self.red}\nServer stopped by user.{self.reset}")
            httpd.shutdown()
            exit(0)

    def run(self):
        """Run the file-sharing server."""
        self.setup()
        self.server()

if __name__ == '__main__':
    app = ShareFolder()
    app.run()
