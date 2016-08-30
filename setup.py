#!/usr/bin/python3
# -*- coding:Utf-8 -*-
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ..
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

config = {
    'description': 'The ultimate tools for DJing Milongas (Tango bal)',
    'author': 'FLCcrakers',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'frank.hoonakker@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['djtango', 'tests', 'mutagen'],
    'scripts': [],
    'name': 'dj-tango',
    'long_description': read('README.md'),
    'classifiers':[
        "Development Status :: 3 - Alpha",
        "Topic :: Multimedia :: Sound/Audio :: Players",
        "License :: OSI Approved :: MIT License",
    ],

}

setup(**config)