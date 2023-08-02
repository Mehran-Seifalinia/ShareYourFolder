#! /usr/bin/python3

from os import chdir, getcwd, system
from http.server import HTTPServer, CGIHTTPRequestHandler

# Function to install required modules
def install_module(module_name):
    try:
        from importlib import import_module
        import_module(module_name)
        return True
    except ModuleNotFoundError:
        try:
            from pip import main
            main(["install", module_name])
            return True
        except:
            print(f"Failed to install {module_name}. Please install it manually.")
            return False

# List of external modules required for the program
reuired_modules = ["FindMyIP", "colorama"]

# Install required modules if not already installed
for module_name in reuired_modules:
    if not install_module(module_name):
        exit(1)

# Import required modules after successful installation
from FindMyIP import internal
from colorama import init, Fore
init(autoreset=True)


class ShareFile:
    """
    A simple file-sharing server for sharing files over the local network.

    Attributes:
        port (int): The port number on which the server will listen.
        current_directory (str): The current working directory for file sharing.
        green (str): ANSI escape code for green text color.
        red (str): ANSI escape code for red text color.
        reset (str): ANSI escape code to reset text color.

    Methods:
        setup(): Set up the file-sharing server by configuring the port.
        server(): Start the HTTP server to share files.
        run(): Run the file-sharing server.
    """

    def __init__(self, port=8080): 
        # Initialize instance attributes
        self.current_directory = getcwd()
        self.port = port
        self.green = Fore.GREEN
        self.red = Fore.RED
        self.reset = Fore.RESET

    def setup(self):
        try:
            # Allow user to set up the port for the server
            self.port = int(input(f"{self.red}[!] You Are sharing \"{self.current_directory}\" on your local network.{self.reset}\nEnter Your port here (default: {self.port}): "))
        except KeyboardInterrupt:
            # Handle KeyboardInterrupt to gracefully stop the server
            print(f"{self.red}\n[-] Server stopped by the user{self.reset}")
            exit(1)
    def server(self):
        try:
            # Set up the server and start serving files
            server_address = ("", self.port)
            httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
            print(f"{self.green}[+] Server is running on http://{internal()}:{self.port}")
            httpd.serve_forever()
        except KeyboardInterrupt:
            # Handle KeyboardInterrupt to gracefully stop the server
            print(f"{self.red}\n[-] Server stopped by the user{self.reset}")
            exit(1)

    def run(self):
        # Run the file-sharing server
        self.setup()
        self.server()

if __name__ == '__main__':
    app = ShareFile()
    app.run()
