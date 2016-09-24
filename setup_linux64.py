#!/usr/bin/python
"""
Setup script for Intrepid Model Checker Python package
"""

from distutils.core import setup
import os
import shutil

print 'Copying osx libraries'
shutil.copy('libs/linux64/libz3.so', 'intrepid')
shutil.copy('libs/linux64/libintrepid_dll.so', 'intrepid')
shutil.copy('libs/linux64/_api.so', 'intrepid')

setup(name='intrepid',
      version='0.1',
      description='Intrepid Model Checker',
      author='Roberto Bruttomesso',
      author_email='roberto.bruttomesso@gmail.com',
      url='http://github.com/bobosoft/intrepid',
      packages=['intrepid'],
      package_data={'intrepid' : ['_api.so', 'libintrepid_dll.so', 'libz3.so']}
     )
