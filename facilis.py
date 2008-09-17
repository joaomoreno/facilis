#!/usr/bin/python
# -*- coding: utf-8 -*-

# Facilis

from core.app import FacilisApp
from gui.cli import CLI

if __name__ == '__main__':
    app = FacilisApp(CLI, debug=True)
    app.start()
