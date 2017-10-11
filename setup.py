#!/usr/bin/python
"""
Setup script for Intrepyd
"""

from setuptools import setup, find_packages
import platform
import sys
import os

VERSION = '0.5.5'

systemStr = platform.system()
bits, _ = platform.architecture()

if bits != "64bit":
    print 'Error: only 64bits architectures are supported. For other OSes please write to roberto.bruttomesso@gmail.com.'
    sys.exit(1)

if systemStr != 'Linux' and systemStr != 'Windows':
    print 'Error: only Linux and Windows OSes are officially supported. For other OSes please write to roberto.bruttomesso@gmail.com.'
    sys.exit(1)

arch_data_files = None
if systemStr == 'Linux':
    arch_data_files = [('/usr/lib/', ['libs/linux64/libz3.so', 'libs/linux64/libintrepid_dll.so', 'libs/linux64/_api.so'])]
elif systemStr == 'Windows':
    arch_data_files = [('', ['libs/win64/libz3.dll', 'libs/win64/intrepid_dll.dll', 'libs/win64/_api.pyd'])]

long_desc="""
# Intrepyd
Intrepyd is a python module that provides a simulator and a model checker in form of
a rich API, to allow the rapid prototyping of **formal methods** algorithms
for the rigorous analysis of circuits, specifications, models.

## Formal Methods Little Corner
A collection of experiences using Intrepyd can be found at https://formalmethods.github.io.

## FAQs
Please refer to the dedicated Wiki page at https://github.com/formalmethods/intrepyd/wiki/FAQs.
"""

setup(name='intrepyd',
      version=VERSION,
      description='Intrepyd Model Checker',
      author='Roberto Bruttomesso',
      author_email='roberto.bruttomesso@gmail.com',
      maintainer='Roberto Bruttomesso',
      maintainer_email='roberto.bruttomesso@gmail.com',
      url='http://github.com/formalmethods/intrepyd',
      download_url='http://github.com/formalmethods/intrepyd/archive/' + VERSION + '.tar.gz',
      packages=find_packages(),
      data_files=arch_data_files,
      package_data={'libs' : ['linux64/*.so', 'win64/*.dll', 'win64/*.pyd']},
      license='BSD-3-Clause',
      platforms=['Windows', 'Linux'],
      long_description=long_desc
)

