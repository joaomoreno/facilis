# -*- coding: utf-8 -*-

# Facilis

class IsADir(Exception):
    def __init__(self, dname):
        self.dname = dname
    def __str__(self):
        return repr(self.dname)

class UnknownURL(Exception):
    def __init__(self, url):
        self.url = url
    def __str__(self):
        return repr(self.url)

class UnknownFile(Exception):
    def __init__(self, fname):
        self.fname = fname
    def __str__(self):
        return repr(self.fname)

class PortInUse(Exception):
    def __init__(self, port):
        self.port = port
    def __str__(self):
        return repr(self.port)
