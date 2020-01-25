#!/usr/bin/python
"""
Setup script for Intrepyd
"""

import platform
import sys
from setuptools import setup, find_packages

VERSION = '0.8.2'

system_str = platform.system()
bits, _ = platform.architecture()

if bits != "64bit":
    print 'Error: only 64bits architectures are supported. For other OSes please write to roberto.bruttomesso@gmail.com.'
    sys.exit(1)

arch_data_files = None
if system_str == 'Linux':
    arch_data_files = [('intrepyd', ['libs/linux64/libz3.so', 'libs/linux64/libintrepid_dll.so', 'libs/linux64/_api.so'])]
elif system_str == 'Windows':
    arch_data_files = [('Lib/site-packages/intrepyd', ['libs/win64/libz3.dll', 'libs/win64/intrepid_dll.dll', 'libs/win64/_api.pyd'])]
elif system_str == 'Darwin':
    arch_data_files = [('intrepyd', ['libs/osx/libz3.dylib', 'libs/osx/libintrepid_dll.dylib', 'libs/osx/_api.so'])]

long_desc = """
========
Intrepyd
========
Intrepyd is a python module that provides a simulator and model checkers in form of
a rich API, to allow the rapid prototyping of **formal methods** algorithms
for the rigorous analysis of circuits, specifications, models.

============================
Formal Methods Little Corner
============================
A collection of experiences using Intrepyd can be found `here <https://formalmethods.github.io>`_.

====
FAQs
====
Please refer to the dedicated `Wiki page <https://github.com/formalmethods/intrepyd/wiki/FAQs>`_.
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
      install_requires=['pandas', 'antlr4-python2-runtime', 'enum'],
      packages=find_packages(),
      data_files=arch_data_files,
      # Does not work for sdist!
      package_data={'libs' : ['linux64/*.so', 'win64/*.dll', 'win64/*.pyd', 'osx/*.so']},
      license='BSD-3-Clause',
      platforms=['Windows', 'Linux', 'Darwin'],
      long_description=long_desc
)

