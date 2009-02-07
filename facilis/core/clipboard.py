#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Facilis
#  João Moreno <http://www.joaomoreno.com/>
#  GPLv3

from sys import platform
import os

def copy(text):
    if platform == "darwin":
        outf = os.popen("pbcopy", "w")
        outf.write(text)
        outf.close()
    elif platform == "win32":
        try:
            import win32clipboard as w
            import win32con
            w.OpenClipboard()
            w.EmptyClipboard()
            w.SetClipboardData(win32con.CF_TEXT, text) 
            w.CloseClipboard()
        except ImportError:
            pass
