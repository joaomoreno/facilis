# -*- coding: utf-8 -*-

# Facilis

from SocketServer import ThreadingMixIn
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
import sys
from misc import UnknownURL, UnknownFile
from os.path import split

CHUNK_SIZE = 65536

class HTTPRequestHandler(BaseHTTPRequestHandler):
    """HTTP request handler for Facilis"""
    def do_GET(self):
        """Respond to a GET request."""
        try:
            fname, mime = self.server.getFile(self.path[1:])
            name = split(fname)[1]

            self.send_response(200)
            if mime:
                self.send_header("Content-type", mime)
            self.send_header("Content-Disposition", 'attachment; filename="' + name + '"')
            self.end_headers()
            
            f = open(fname, "rb")
            
            while True:
                data = f.read(CHUNK_SIZE)
                if data == '':
                    break
                self.wfile.write(data)
            
            f.close()
        except:
            self.send_error(404)

class FacilisServer(ThreadingMixIn, HTTPServer):
    def __init__(self, address, handler, app):
        HTTPServer.__init__(self, address, handler)
        self.app = app
    
    def getFile(self, url):
        return self.app.getFile(url)

class ServerHandler(Thread):
    def __init__(self, app, port):
        Thread.__init__(self)
        self.app = app
        self.port = port
    
    def run(self):
        httpd = FacilisServer(('', self.port), HTTPRequestHandler, self.app)
        httpd.serve_forever()
        httpd.server_close()
