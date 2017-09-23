#!/usr/bin/python
"""
Setup script for Intrepyd
"""

# from distutils.core import setup
from setuptools import setup, find_packages
from subprocess import call
import shutil
import platform
import sys
import os

systemStr = platform.system()
bits, _ = platform.architecture()

packageDataList = []

if systemStr == 'Linux':
      if bits == "32bit":
      	   print 'Copying linux32 libraries'
      	   shutil.copy('libs/linux32/_api.so', 'intrepyd')
           packageDataList = ['_api.so']
      elif bits == "64bit":
      	   print 'Copying linux64 libraries'
      	   shutil.copy('libs/linux64/_api.so', 'intrepyd')
           packageDataList = ['_api.so']
      else:
           print 'Unsupported number of bits', bits
           sys.exit(1)

elif systemStr == 'Windows':
      print 'Copying win64 libraries'
      shutil.copy('libs/win64/libz3.dll', 'intrepyd')
      shutil.copy('libs/win64/intrepid_dll.dll', 'intrepyd')
      shutil.copy('libs/win64/_api.pyd', 'intrepyd')
      packageDataList = ['_api.pyd', 'intrepid_dll.dll', 'libz3.dll']
elif systemStr == 'Darwin':
      cwd = os.getcwd()
      call(["install_name_tool", "-change", "libintrepid_dll.dylib", cwd + "/libs/osx/libintrepid_dll.dylib", "libs/osx/_api.so"])
      call(["install_name_tool", "-change", "libz3.dylib", cwd + "/libs/osx/libz3.dylib", "libs/osx/_api.so"])
      call(["install_name_tool", "-change", "libz3.dylib", cwd + "/libs/osx/libz3.dylib", "libs/osx/libintrepid_dll.dylib"])
      print 'Copying osx libraries'
      shutil.copy('libs/osx/_api.so', 'intrepyd')
      packageDataList = ['_api.so']
else:
      print 'Unsupported OS', systemStr
      sys.exit(1)

# Retrieves version
VERSION = open('VERSION').readlines()[0].strip()

setup(name='intrepyd',
      version=VERSION,
      description='Intrepyd',
      author='Roberto Bruttomesso',
      author_email='roberto.bruttomesso@gmail.com',
      url='http://github.com/formalmethods/intrepyd',
      download_url='http://github.com/formalmethods/intrepyd/archive/' + VERSION + 'tar.gz',
      packages=find_packages(),
      package_data={'intrepyd' : packageDataList},
      install_requires=[
          'numpy>=1.12',
          'pandas==0.19.1',
          'enum>=0.4.6',
          'colorama>=0.3.9',
          'antlr4-python2-runtime==4.6'
      ],
      classifiers = []
)

suffix = "32"
if bits == "64bit":
    suffix = "64"

if systemStr == 'Linux':
      print ""
      print "*************************************************"
      print "Don't forget to do:"
      print 'export LD_LIBRARY_PATH=`pwd`/libs/linux' + suffix
      print "*************************************************"
elif systemStr == 'Darwin':
      print ""
      print "*************************************************"
      print "Don't forget to do:"
      print 'export DYLD_LIBRARY_PATH=`pwd`/libs/osx'
      print "*************************************************"
