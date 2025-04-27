#! /usr/bin/python3

from os import chdir, getcwd
from sys import exit
from socket import socket, AF_INET, SOCK_DGRAM
from http.server import HTTPServer, SimpleHTTPRequestHandler
from tkinter import filedialog, Tk, simpledialog, messagebox
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
    """Allow the user to select a directory for sharing."""
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(title="Select Folder to Share")
    return folder_selected if folder_selected else getcwd()

class ShareFolder:
    """Class to handle the file-sharing server."""

    def __init__(self, port=80):
        self.root = Tk()
        self.root.withdraw()
        self.current_directory = choose_directory()
        chdir(self.current_directory)
        self.port = port
        self.green = Fore.GREEN
        self.red = Fore.RED
        self.reset = Style.RESET_ALL

    def setup(self):
        """Prompt user for a custom port if needed via GUI."""
        try:
            user_input = simpledialog.askstring(
                "Set Port",
                f"Sharing: \"{self.current_directory}\"\nEnter port (default: {self.port}):",
                parent=self.root
            )
            if user_input and user_input.strip():
                self.port = int(user_input.strip())
        except Exception as e:
            messagebox.showerror("Error", f"Error while setting port: {e}")
            exit(1)

    def server(self):
        """Start the HTTP server."""
        try:
            server_address = ("", self.port)
            httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
            messagebox.showinfo(
                "Server Running",
                f"Server is running!\n\nURL: http://{get_local_ip()}:{self.port}"
            )
            print(f"{self.green}[+] Server running at: http://{get_local_ip()}:{self.port}{self.reset}")
            httpd.serve_forever()
        except OSError as e:
            messagebox.showerror("Server Error", f"Error: {e}")
            exit(1)
        except KeyboardInterrupt:
            print(f"{self.red}\n[-] Server stopped by user.{self.reset}")
            httpd.shutdown()
            exit(0)

    def run(self):
        """Run the file-sharing server."""
        self.setup()
        self.server()

if __name__ == '__main__':
    app = ShareFolder()
    app.run()
