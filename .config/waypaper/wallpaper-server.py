import http.server
import os
import sys

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def do_GET(self):
        # Serve the current wallpaper image
        self.path = os.listdir(os.path.expanduser("~/current_wallpaper/"))[0]  # Path to symlink
        super().do_GET()

def run_server():
    # Set the directory to serve files from
    os.chdir(os.path.expanduser("/home/saai/current_wallpaper/"))

    # Start the server on localhost and port 8000
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, NoCacheHTTPRequestHandler)
    print("Server running at http://localhost:8000/current.png")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
