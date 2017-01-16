#!/usr/bin/env python3
 
from http.server import BaseHTTPRequestHandler, HTTPServer
 
class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        self.send_response(200)
        message = self.client_address[0] + "\n"
        self.wfile.write(bytes(message, "utf8"))
        return

def run():
  server_address = ('', 80)
  httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
  httpd.serve_forever()

run()
