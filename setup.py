#!/usr/bin/python
"""
Setup script for Intrepid Model Checker Python package
"""

from distutils.core import setup
from subprocess import call
import shutil
import platform
import sys
import os

systemStr = platform.system()

packageDataList = []

if systemStr == 'Linux':
      print 'Copying linux64 libraries'
      shutil.copy('libs/linux64/_api.so', 'intrepid')
      packageDataList = ['_api.so']
elif systemStr == 'Windows':
      print 'Copying win64 libraries'
      shutil.copy('libs/win64/libz3.dll', 'intrepid')
      shutil.copy('libs/win64/intrepid_dll.dll', 'intrepid')
      shutil.copy('libs/win64/_api.pyd', 'intrepid')
      packageDataList = ['_api.pyd', 'intrepid_dll.dll', 'libz3.dll']
elif systemStr == 'Darwin':
      print 'Copying osx libraries'
      cwd = os.getcwd()
      call(["install_name_tool", "-change", "libintrepid_dll.dylib", cwd + "/libs/osx/libintrepid_dll.dylib", "libs/osx/_api.so"])
      call(["install_name_tool", "-change", "libz3.dylib", cwd + "/libs/osx/libz3.dylib", "libs/osx/_api.so"])
      call(["install_name_tool", "-change", "libz3.dylib", cwd + "/libs/osx/libz3.dylib", "libs/osx/libintrepid_dll.dylib"])
      shutil.copy('libs/osx/_api.so', 'intrepid')
      packageDataList = ['_api.so']
else:
      print 'Unsupported OS', systemStr
      sys.exit(1)


setup(name='intrepid',
      version='0.1.1',
      description='Intrepid Model Checker',
      author='Roberto Bruttomesso',
      author_email='roberto.bruttomesso@gmail.com',
      url='http://github.com/bobosoft/intrepid',
      packages=['intrepid'],
      package_data={'intrepid' : packageDataList}
)

if systemStr == 'Linux':
      print "Don't forget to do:"
      print 'export LD_LIBRARY_PATH=`pwd`/libs/linux64'