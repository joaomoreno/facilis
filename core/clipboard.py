# -*- coding: utf-8 -*-

# Facilis

from sys import platform
import os

def copy(text):
    if platform == 'darwin':
        outf = os.popen("pbcopy", "w")
        outf.write(text)
        outf.close()
    elif sys.platform == "win32":
        import win32clipboard as w
        import win32con
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_TEXT, text) 
        w.CloseClipboard()
