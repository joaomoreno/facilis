#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Facilis
#  João Moreno <http://www.joaomoreno.com/>
#  GPLv3

from setuptools import setup, find_packages

setup(
    name = "Facilis",
    version = "0.1",
    packages = find_packages(),
    package_data = {
        'facilis':['resources/*']
    },
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
