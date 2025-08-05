#!/usr/bin/python3

from argparse import ArgumentParser
from os import chdir, getcwd
from socket import socket, AF_INET, SOCK_DGRAM
from http.server import HTTPServer, SimpleHTTPRequestHandler
from tkinter import filedialog, Tk, simpledialog, messagebox
from sys import exit as sys_exit
from colorama import init as colorama_init, Fore, Style

# Initialize colorama for consistent color output (only used if console is available)
colorama_init(autoreset=True)

def get_local_ip():
    """
    Retrieve the local IP address used for outgoing internet connections.
    Returns 127.0.0.1 if no network is available.
    """
    with socket(AF_INET, SOCK_DGRAM) as s:
        try:
            s.connect(("8.8.8.8", 80))  # This doesn't send data, just determines the local IP
            return s.getsockname()[0]
        except Exception:
            return "127.0.0.1"

def choose_directory():
    """
    Show a GUI folder selection dialog using Tkinter.
    Falls back to current directory if user cancels.
    """
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(title="Select Folder to Share")
    if folder_selected:
        return folder_selected
    else:
        return getcwd()

class ShareFolder:
    """
    Class responsible for setting up and running the HTTP file-sharing server.
    """

    def __init__(self, directory=None, port=80):
        self.original_directory = getcwd()  # Save original directory for later restoration
        self.current_directory = directory if directory else choose_directory()
        self.port = port

    def setup_port(self):
        """
        Ask user for a custom port number.
        Tries console input; falls back to GUI dialog if console is unavailable.
        """
        try:
            # Try console input (works only if console is available)
            user_input = input(f"Sharing folder: \"{self.current_directory}\"\n"
                               f"Enter port number (default: {self.port}): ").strip()
            if user_input:
                port_candidate = int(user_input)
                if 1 <= port_candidate <= 65535:
                    self.port = port_candidate
        except (RuntimeError, EOFError):
            # If running in --noconsole mode, use GUI instead
            root = Tk()
            root.withdraw()
            port_candidate = simpledialog.askinteger(
                "Port Selection",
                f"Enter port number (default: {self.port}):",
                minvalue=1,
                maxvalue=65535
            )
            if port_candidate:
                self.port = port_candidate

    def run_server(self):
        """
        Start the HTTP server and show connection info using GUI.
        If the port is in use, show an error popup.
        """
        chdir(self.current_directory)
        httpd = None
        try:
            server_address = ("", self.port)
            httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

            # Build the server URL and show it
            ip = get_local_ip()
            server_url = f"http://{ip}:{self.port}"

            root = Tk()
            root.withdraw()
            messagebox.showinfo("Server Started", f"Server is running at:\n{server_url}\n\n"
                                                  "Leave this window open while sharing files.\n"
                                                  "Close it to stop the server.")

            httpd.serve_forever()

        except OSError as e:
            root = Tk()
            root.withdraw()
            messagebox.showerror("Server Error", f"Failed to start server:\n{str(e)}")
            return 1

        finally:
            chdir(self.original_directory)

    def run(self):
        """
        Entry point: configure the port and start the server.
        """
        self.setup_port()
        return self.run_server()

def main():
    """
    Parse command-line arguments (optional) and launch the ShareFolder server.
    """
    parser = ArgumentParser(description="Share a folder over HTTP on the local network.")
    parser.add_argument("-d", "--directory", type=str,
                        help="Directory to share. If omitted, a folder selection dialog will appear.")
    parser.add_argument("-p", "--port", type=int, default=80,
                        help="Port to listen on (default: 80)")
    args = parser.parse_args()

    # Validate the port range
    if args.port < 1 or args.port > 65535:
        print(f"{Fore.RED}Error: Port must be between 1 and 65535.{Style.RESET_ALL}")
        return 1

    app = ShareFolder(directory=args.directory, port=args.port)
    return app.run()

if __name__ == "__main__":
    sys_exit(main())
