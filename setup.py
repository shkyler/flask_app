#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from setuptools import setup

setup(
    name='my_app',
    version='1.0',
    license='GNU General Public License v3',
    author='Patrick Moore',
    author_email='moorepa@outlook.com',
    description='Hello World! appliction for Flask',
    packages=['my_app'],
    platfroms='any',
    install_required=[
        'flask'
    ],
    classifiers=[
        'Development Status :: 4 -Beta',
        'Environemtn :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ], 
)