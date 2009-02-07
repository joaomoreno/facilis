#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Facilis
#  João Moreno <http://www.joaomoreno.com/>
#  GPLv3

from facilis.core.misc import IsADir, PortInUse
from facilis.core.app import FacilisApp

def main():
    app = FacilisMac()
    app.start()

class FacilisMac(object):
    """Cocoa interface for Facilis."""
    
    def __init__(self):
        """Gives directions to the user and starts the interface."""
        self.app = FacilisApp()
    
    def start(self):
        """Starts the interface."""
        try:
            self.app.start()
        except PortInUse, p:
            print "Port already in use:", p
            exit(-2)
    
    def addFile(self, fname):
        """Adds a file to the app and prints its URL to the screen."""
        try:
            url = self.app.addFile(fname)
            return url
        except IOError:
            print "# Path does not exist or is unreadable"
        except IsADir:
            print "# Path is a directory"
        else:
            print "#", url
