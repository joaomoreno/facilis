#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Facilis
#  João Moreno <http://www.joaomoreno.com/>
#  GPLv3

from SocketServer import ThreadingMixIn
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
import sys
from misc import UnknownURL, UnknownFile
from os.path import split, getsize
from pkg_resources import resource_string, resource_filename

CHUNK_SIZE = 65536

print sys.version_info

class HTTPRequestHandler(BaseHTTPRequestHandler):
    """HTTP request handler for Facilis"""    
    def do_GET(self):
        """Respond to a GET request."""
        req = self.path[1:]
        
        if req == "logo.png":
            self.__sendFile(resource_filename(__name__, "resources/logo.png"), "image/png")
        else:
            try:
                fname, mime = self.server.getFile(req)
                print fname, mime
                self.__sendFile(fname, mime)
            except:
                self.send_response(404)
                self.send_header("Content-type", "text/html")
                self.send_header("Connection", "close")
                self.end_headers()
                self.wfile.write(resource_string(__name__, "resources/404.html"))
    
    def __sendFile(self, fname, mime):
        print mime
        
        name = split(fname)[1]

        self.send_response(200)
        if mime:
            self.send_header("Content-type", mime)
        self.send_header("Connection", "close")
        self.send_header("Content-Disposition", 'attachment; filename="' + name + '"')
        self.send_header("Content-Length", getsize(fname))
        self.end_headers()
        
        f = open(fname, "rb")
        self.wfile.write(f.read())
        f.close()

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
        try:
            httpd = FacilisServer(('', self.port), HTTPRequestHandler, self.app)
            httpd.serve_forever()
            httpd.server_close()
        except:
            exit(-2)
        
