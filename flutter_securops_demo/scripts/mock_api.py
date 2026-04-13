import http.server
import socketserver
import threading
import time

PORT = 5000

class MockHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('X-Content-Type-Options', 'nosniff') # Good security header
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"status": "success", "message": "SecurOps Debug Active"}')

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"status": "success", "message": "User Logged In"}')

def run_server():
    with socketserver.TCPServer(("", PORT), MockHandler) as httpd:
        print(f"SecurOps Mock Server started at port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
