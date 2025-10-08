#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "127.0.0.1"
PORT = 8000

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            payload = json.dumps(data)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(payload)
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run():
    server = HTTPServer((HOST, PORT), MyHandler)
    print(f"Serving on http://{HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
