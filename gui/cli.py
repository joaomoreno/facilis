# -*- coding: utf-8 -*-

# Facilis

from sys import stdin, stdout
import os
import re
from .core.misc import IsADir

class CLI(object):
    """Command line interface for Facilis."""
    
    def __init__(self, app, cin=stdin):
        """Gives directions to the user and starts the interface."""        
        print "\nFacilis - Send files and folders through HTTP without hassle"
        self.app = app
        self.cin = cin
    
    def __run(self):
        """This is the core of the interface."""
        
        while True:
            # Read input
            stdout.write("> ")
            stdout.flush()
            try:
                line = self.cin.readline()
            except KeyboardInterrupt:
                print "\nBye!"
                break
            
            f = re.sub(r'\\(.)', r'\1', line.rstrip()) # filename
            argv = f.split(' ') # commands
            
            # Is empty line?
            if (len(argv) < 0 or argv[0] == '') and line != '':
                continue
            
            # Parse commands
            if line == '' or argv[0] == 'exit' or argv[0] == 'quit':
                print "Bye!"
                break
            #elif argv[0] == 'list':
            #    print "# All files under Facilis:"
            elif argv[0] == 'help':
                self.__printHelp()
            elif argv[0] == 'set':
                self.__set(argv)
            #elif self.app.debug and argv[0] == 'db':
            #    print self.app.db.file2url
            #    print self.app.db.url2file
            else:
                self.__addFile(f)
        
        self.app.kill()
    
    def __addFile(self, fname):
        """Adds a file to the app and prints its URL to the screen."""
        try:
            url = self.app.addFile(fname)
        except IOError:
            print "# Path does not exist or is unreadable"
        except IsADir:
            print "# Path is a directory"
        else:
            print "#", url
    
    def __printHelp(self):
        """Prints the help information."""
        print """Available commands:
- <filename>\t\tAdds the file to Facilis and returns the respective URL (also adds it to the clipboard).
- help\t\t\tPrints these instructions.
- set [option] [value]\tLists, gets and sets (an) option(s). Type 'set' for all the options available.
- exit\t\t\tExits the application.
"""

    def __set(self, argv):
        """Manages the 'set' command."""
        if len(argv) < 2:
            print self.app.config
        
        elif len(argv) < 3 and argv[1] in ('port', 'domain', 'use_domain'):
            try:
                o = str(self.app.config[argv[1]])
                print "%s: %s" % (argv[1].capitalize(), o)
            except:
                print "Unkown option %s" % argv[1]
        
        elif argv[1] == 'port':
            try:
                p = int(argv[2])
            except:
                print "That is not a valid port number"
            else:
                if p < 1024 or p > 49151:
                    print "Port must be between 1024 and 49151"
                else:
                    self.app.setPort(p)
                    print "Port set to %i" % p
        
        elif argv[1] == 'domain':
            self.app.setDomain(argv[2])
            print "Domain set to %s" % argv[2]
        
        elif argv[1] == 'use_domain':
            val = argv[2].lower()
            if val == 'true':
                self.app.useDomain(True)
                print "Using domain %s from now on" % self.app.config['domain']
            elif val == 'false':
                self.app.useDomain(False)
                print "Stopped using domain %s" % self.app.config['domain']
            else:
                print "'use_domain' only accepts the values 'true' and 'false'"
        
        else:
            print "Unkown option %s" % argv[1]
    
    def start(self):
        """Starts the interface."""
        print "URL prefix:", self.app.getUrl()
        print """Usage:
- Write or paste the filename in the shell and the respective URL will be output to the screen and added to the clipboard.
- If you feel a little lost, just enter 'help'.
- To quit just enter 'quit' or press ^D.
"""
        self.__run()
