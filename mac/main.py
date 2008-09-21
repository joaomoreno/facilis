#
#  main.py
#  Facilis
#
#  Created by Joao Moreno on 9/21/08.
#  Copyright __MyCompanyName__ 2008. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import FacilisAppDelegate

# pass control to AppKit
AppHelper.runEventLoop()
