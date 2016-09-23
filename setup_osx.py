#!/usr/bin/python
"""
Setup script for Intrepid Model Checker Python package
"""

from distutils.core import setup
import os
import shutils

print 'Copying osx libraries'
shutils.copy('libs/osx/libz3.dylib', 'intrepid')
shutils.copy('libs/osx/libintrepid_dll.dylib', 'intrepid')
shutils.copy('libs/osx/_api.so', 'intrepid')

setup(name='intrepid',
      version='0.1',
      description='Intrepid Model Checker',
      author='Roberto Bruttomesso',
      author_email='roberto.bruttomesso@gmail.com',
      url='http://github.com/bobosoft/intrepid',
      packages=['intrepid'],
      package_data={'intrepid' : ['_api.so', 'libintrepid_dll.dylib', 'libz3.dylib']}
     )
