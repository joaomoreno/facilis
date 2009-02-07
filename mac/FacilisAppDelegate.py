#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Facilis
#  João Moreno <http://www.joaomoreno.com/>

import sys
from os.path import split

from Foundation import *
from AppKit import *
from objc import nil, NO

from facilis.core.app import FacilisApp
from facilis.core.misc import IsADir
from growl import Growl

FILEADDED = "FileAdded"
ISDIR = "IsDir"
ERROR = "Error"
STARTUP = "Startup"

class FacilisAppDelegate(NSObject):
    def applicationWillFinishLaunching_(self, sender):
        self.start()
    
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application loaded")
    
    def application_openFile_(self, sender, fname):
        fname = fname.encode("utf-8")
        name = split(fname)[1]
        try:
            url = self.app.addFile(fname)
        except IOError:
            self.notifier.notify("Error", "Error", "Something bad happened. Try again.")
        except IsADir:
            self.notifier.notify("IsDir", "Error", name + " is a directory.")
        else:
            self.notifier.notify("FileAdded", u"File added to Facilis", u"\"" + name + u"\" was just added to Facilis; its URL was copied to the pasteboard. You can now paste it anywhere.")

    def start(self):
        self.app = FacilisApp()
        self.app.start()
        self.notifier = Growl.GrowlNotifier("Facilis", [FILEADDED, ISDIR, ERROR, STARTUP])
        self.notifier.register()
        self.notifier.notify("Startup", "Facilis", "Facilis just started on port " + str(self.app.config['port']))
