#!/usr/bin/python
"""
Setup script for Intrepid Model Checker Python package
"""

from distutils.core import setup

print 'Copying osx libraries'
shutils.copy('libs/win64/libz3.dll', 'intrepid')
shutils.copy('libs/win64/libintrepid_dll.dll', 'intrepid')
shutils.copy('libs/win64/_api.pyd', 'intrepid')

setup(name='intrepid',
      version='0.1',
      description='Intrepid Model Checker',
      author='Roberto Bruttomesso',
      author_email='roberto.bruttomesso@gmail.com',
      url='http://github.com/bobosoft/intrepid',
      packages=['intrepid'],
      package_data={'intrepid' : ['_api.pyd', 'intrepid_dll.dll', 'libz3.dll']}
     )
