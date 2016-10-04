#!/usr/bin/python
"""
Setup script for Intrepid Model Checker Python package
"""

from distutils.core import setup
import os
import shutil

print 'Copying linux64 libraries'
shutil.copy('libs/linux64/_api.so', 'intrepid')

setup(name='intrepid',
      version='0.1',
      description='Intrepid Model Checker',
      author='Roberto Bruttomesso',
      author_email='roberto.bruttomesso@gmail.com',
      url='http://github.com/bobosoft/intrepid',
      packages=['intrepid'],
      package_data={'intrepid' : ['_api.so']}
     )

print "Don't forget to do:"
print 'export LD_LIBRARY_PATH=`pwd`/libs/linux64'
