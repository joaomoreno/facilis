#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Facilis
#  João Moreno <http://www.joaomoreno.com/>
#  GPLv3

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import FacilisAppDelegate

# pass control to AppKit
AppHelper.runEventLoop()
