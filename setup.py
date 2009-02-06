#!/usr/bin/python
# -*- coding: utf-8 -*-

# Facilis

from setuptools import setup, find_packages
#import py2app

setup(
    name = "Facilis",
    version = "0.1",
    packages = find_packages(),
    install_requires = ['PyYaml'],
    entry_points = {
        'console_scripts': [
            'facilis = facilis.ui.cli:main'
        ]
    },
    author = "João Moreno",
    author_email = "alph.pt@gmail.com",
    description = "Send files through HTTP without hassle.",
    license = "GPL",
    keywords = "facilis share http hassle"
)
