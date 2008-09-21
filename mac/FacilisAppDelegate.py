#
#  FacilisAppDelegate.py
#  Facilis
#
#  Created by Joao Moreno on 9/21/08.
#  Copyright __MyCompanyName__ 2008. All rights reserved.
#

import sys
from Foundation import *
from AppKit import *
from facilis.gui.mac import FacilisMac

class FacilisAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        try:
            self.app
        except:
            self.start()
    
    def application_openFile_(self, sender, file):
        try:
            self.app.addFile(file)
        except:
            self.start()
        finally:
            self.app.addFile(file)
        
    def start(self):
        self.app = FacilisMac()
        self.app.start()
