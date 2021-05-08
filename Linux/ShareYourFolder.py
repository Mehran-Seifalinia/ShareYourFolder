from os import chdir, getcwd
from http.server import HTTPServer, CGIHTTPRequestHandler

def shareIt():
    port = int(input(f"[!] You Are sharing \"{current_directory}\" on your local network.\nEnter Your port here: "))
    chdir(".")
    server = HTTPServer(("", port), CGIHTTPRequestHandler)
    print(f"Server is online on 127.0.0.1:{port}")
    server.serve_forever()

current_directory = getcwd()
shareIt()