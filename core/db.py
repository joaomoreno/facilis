# -*- coding: utf-8 -*-

# Facilis

from hashlib import sha1
from time import time
from mimetypes import guess_type
import os
from misc import UnknownURL, UnknownFile, IsADir

class FilesDatabase(object):
    
    def __init__(self):
        self.url2file = {}
        self.file2url = {}
    
    def __checkFile(self, fname):
        """Does the file exist and is it readable?"""
        return os.access(fname, os.R_OK)
    
    def addFile(self, fname):
        """Add a file to the database.
        Returns the sha-1 of 'filename' + timestamp."""
        if fname in self.file2url:
            return self.file2url[fname]
        
        if not self.__checkFile(fname):
            raise IOError, "File does not exist or is unreadable"
        
        if os.path.isfile(fname):
            d = sha1()
            d.update(fname + str(time()))
            d = d.hexdigest()
            
            mmtype = guess_type(fname)[0]
        
            self.url2file[d] = (fname, mmtype)
            self.file2url[fname] = d
        
            return d
        elif os.path.isdir(fname):
            raise IsADir, fname
        else:
            raise IOError, "Invalid path"
    
    def getFile(self, url):
        if url in self.url2file:
            fname, mime = self.url2file[url]
            
            # If the file isn't found, just clean the database and throw exception
            if not self.__checkFile(fname):
                del self.url2file[url]
                del self.file2url[fname]
                raise UnknownFile, fname
            
            return (fname, mime)
        else:
            raise UnknownURL, url
