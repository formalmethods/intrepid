#!/usr/bin/python
"""
Setup script for Intrepid Model Checker Python package
"""

from distutils.core import setup
from subprocess import call
import os
import shutil

print 'Copying osx libraries'
cwd = os.getcwd()
call(["install_name_tool", "-change", "libintrepid_dll.dylib", cwd + "/libs/osx/libintrepid_dll.dylib", "libs/osx/_api.so"])
call(["install_name_tool", "-change", "libz3.dylib", cwd + "/libs/osx/libz3.dylib", "libs/osx/_api.so"])
call(["install_name_tool", "-change", "libz3.dylib", cwd + "/libs/osx/libz3.dylib", "libs/osx/libintrepid_dll.dylib"])
shutil.copy('libs/osx/_api.so', 'intrepid')

setup(name='intrepid',
      version='0.1',
      description='Intrepid Model Checker',
      author='Roberto Bruttomesso',
      author_email='roberto.bruttomesso@gmail.com',
      url='http://github.com/bobosoft/intrepid',
      packages=['intrepid'],
      package_data={'intrepid' : ['_api.so']}
     )
