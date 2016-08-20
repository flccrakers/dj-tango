#!/usr/bin/python3
# -*- coding:Utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Frank Hoonakker aka FLCcrakers',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'frank.hoonakker@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)