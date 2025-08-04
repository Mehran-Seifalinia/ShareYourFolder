#!/usr/bin/python3

from argparse import ArgumentParser
from os import chdir, getcwd
from socket import socket, AF_INET, SOCK_DGRAM
from http.server import HTTPServer, SimpleHTTPRequestHandler
from tkinter import filedialog, Tk
from sys import exit as sys_exit
from colorama import init as colorama_init, Fore, Style

# Initialize colorama for colored terminal output
colorama_init(autoreset=True)

def get_local_ip():
    """
    Retrieve the local IP address by connecting to an external host.
    Returns '127.0.0.1' if the connection fails, indicating no network access.
    """
    with socket(AF_INET, SOCK_DGRAM) as s:
        try:
            # Doesn't send packets, just determines local IP used for internet
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            if ip == "127.0.0.1":
                print(f"{Fore.RED}Warning: Could not detect local IP address. Using loopback (127.0.0.1). "
                      "Server will not be accessible from other devices.{Style.RESET_ALL}")
            return ip
        except Exception:
            print(f"{Fore.RED}Warning: Network unreachable. Using loopback IP (127.0.0.1). "
                  "Server will not be accessible from other devices.{Style.RESET_ALL}")
            return "127.0.0.1"

def choose_directory():
    """
    Allow the user to select a directory via a graphical dialog (Tkinter).
    If no selection is made, return current working directory and notify user.
    """
    root = Tk()
    root.withdraw()  # Hide the root window
    folder_selected = filedialog.askdirectory(title="Select Folder to Share")
    if folder_selected:
        return folder_selected
    else:
        cwd = getcwd()
        print(f"{Fore.YELLOW}No folder selected. Using current directory: {cwd}{Style.RESET_ALL}")
        return cwd

class ShareFolder:
    """
    Class to handle setting up and running the file-sharing HTTP server.
    """

    def __init__(self, directory=None, port=80):
        self.original_directory = getcwd()  # Save original working directory to restore later
        self.current_directory = directory if directory else choose_directory()
        self.port = port

        # Color setup for messages
        self.white = Fore.WHITE
        self.red = Fore.RED
        self.green = Fore.GREEN
        self.yellow = Fore.YELLOW
        self.reset = Style.RESET_ALL

    def setup_port(self):
        """
        Prompt user for a custom port number with input.
        Validates that port is integer and within valid range (1-65535).
        """
        while True:
            user_input = input(f"{self.green}Sharing folder: \"{self.current_directory}\"\n"
                               f"Enter port number (default: {self.port}): {self.reset}").strip()
            if not user_input:
                # No input, keep default
                break
            try:
                port_candidate = int(user_input)
                if 1 <= port_candidate <= 65535:
                    self.port = port_candidate
                    break
                else:
                    print(f"{self.red}Port number must be between 1 and 65535.{self.reset}")
            except ValueError:
                print(f"{self.red}Invalid input. Please enter a numeric port.{self.reset}")

    def run_server(self):
        """
        Change to the chosen directory and start the HTTP server.
        Handles keyboard interrupt cleanly.
        Restores original directory on exit.
        """
        chdir(self.current_directory)
        httpd = None
        try:
            server_address = ("", self.port)
            httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
            print(f"{self.green}Server running at: http://{get_local_ip()}:{self.port}{self.reset}")
            print(f"{self.yellow}Press Ctrl+C to stop the server.{self.reset}")
            httpd.serve_forever()
        except OSError as e:
            print(f"{self.red}Error: {e}{self.reset}")
            return 1
        except KeyboardInterrupt:
            print(f"\n{self.red}Server stopped by user.{self.reset}")
            if httpd:
                httpd.shutdown()
            return 0
        finally:
            # Restore original working directory
            chdir(self.original_directory)

    def run(self):
        """
        Main entry point: setup port and run server.
        """
        self.setup_port()
        return self.run_server()


def main():
    """
    Parse command line arguments for optional directory and port,
    then start the ShareFolder server.
    """
    parser = ArgumentParser(description="Share a folder over HTTP on local network.")
    parser.add_argument("-d", "--directory", type=str,
                        help="Directory to share. If omitted, graphical selection dialog is shown.")
    parser.add_argument("-p", "--port", type=int, default=80,
                        help="Port to listen on (default: 80)")
    args = parser.parse_args()

    # Validate port range from CLI argument
    if args.port < 1 or args.port > 65535:
        print(f"{Fore.RED}Error: Port must be between 1 and 65535.{Style.RESET_ALL}")
        return 1

    app = ShareFolder(directory=args.directory, port=args.port)
    return app.run()


if __name__ == "__main__":
    sys_exit(main())
