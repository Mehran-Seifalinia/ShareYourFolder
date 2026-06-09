#!/usr/bin/python3

from argparse import ArgumentParser
from os import chdir, getcwd
from socket import socket, AF_INET, SOCK_DGRAM
from http.server import HTTPServer, SimpleHTTPRequestHandler
from tkinter import filedialog, Tk, simpledialog, messagebox, Label, Button
from sys import exit as sys_exit
from sys import stdin
from signal import signal, SIGINT
from threading import Thread


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
        
def is_console_available():
    """Return True if running in a real console (stdin is a TTY)."""
    try:
        return stdin.isatty()
    except Exception:
        return False

def choose_directory():
    """
    Show a GUI folder selection dialog using Tkinter.
    Falls back to current directory if user cancels.
    """
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(title="Select Folder to Share")
    root.destroy()
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
        Uses console if available, otherwise falls back to GUI dialog.
        """
        if is_console_available():
            # Console mode
            try:
                user_input = input(f"Sharing folder: \"{self.current_directory}\"\n"
                                f"Enter port number (default: {self.port}): ").strip()
                if user_input:
                    port_candidate = int(user_input)
                    if 1 <= port_candidate <= 65535:
                        self.port = port_candidate
                    else:
                        print(f"Port out of range (1-65535). Using default {self.port}.")
            except ValueError:
                print(f"Invalid number. Using default {self.port}.")
        else:
            # GUI mode (e.g., when running as --noconsole exe)
            root = Tk()
            root.withdraw()
            port_candidate = simpledialog.askinteger(
                "Port Selection",
                f"Enter port number (default: {self.port}):",
                minvalue=1,
                maxvalue=65535
            )
            root.destroy()
            if port_candidate:
                self.port = port_candidate

    def run_server(self):
        """Start the HTTP server. In GUI mode shows a control window; in console mode handles Ctrl+C."""
        chdir(self.current_directory)
        self.httpd = None
        try:
            self.httpd = HTTPServer(("", self.port), SimpleHTTPRequestHandler)
            ip = get_local_ip()
            server_url = f"http://{ip}:{self.port}"

            # Decide mode based on console availability
            if is_console_available():
                # Console mode: print info and wait for Ctrl+C
                print(f"Serving directory: {self.current_directory}")
                print(f"Server running at {server_url}")
                print("Press Ctrl+C to stop the server.")

                # Run server in a separate thread so we can catch signals
                server_thread = Thread(target=self.httpd.serve_forever, daemon=True)
                server_thread.start()

                # Setup signal handler for graceful shutdown
                def signal_handler(sig, frame):
                    print("\nStopping server...")
                    self.httpd.shutdown()
                    server_thread.join()
                    print("Server stopped.")
                    sys_exit(0)

                signal(SIGINT, signal_handler)

                # Keep main thread alive
                while server_thread.is_alive():
                    server_thread.join(timeout=0.5)
            else:
                # GUI mode: create control window with Stop button
                root = Tk()
                root.title("Share Folder Server")
                root.geometry("400x150")
                root.resizable(False, False)

                label = Label(root, text=f"Server running at:\n{server_url}\n\nClick 'Stop' to shutdown.")
                label.pack(pady=10)

                stop_btn = Button(root, text="Stop Server", command=lambda: self._shutdown_gui(root))
                stop_btn.pack(pady=5)

                # Run server in background thread
                server_thread = Thread(target=self.httpd.serve_forever, daemon=True)
                server_thread.start()

                # Close window also shuts down
                root.protocol("WM_DELETE_WINDOW", lambda: self._shutdown_gui(root))
                root.mainloop()

        except OSError as e:
            if not is_console_available():
                root = Tk()
                root.withdraw()
                messagebox.showerror("Server Error", f"Failed to start server:\n{str(e)}")
                root.destroy()
            else:
                print(f"Error: {str(e)}")
            return 1
        finally:
            chdir(self.original_directory)
        return 0

    def _shutdown_gui(self, root):
        """Helper to shutdown server and close GUI window."""
        if self.httpd:
            self.httpd.shutdown()
        root.quit()
        root.destroy()

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
        print("Error: Port must be between 1 and 65535.")
        return 1

    app = ShareFolder(directory=args.directory, port=args.port)
    return app.run()

if __name__ == "__main__":
    sys_exit(main())
