#!/usr/bin/python
"""
Setup script for Intrepyd
"""

import platform
import sys
import os
from setuptools import setup, find_packages

with open('VERSION') as version_file:
    version = version_file.read().strip()

system_str = platform.system()
bits, _ = platform.architecture()

if bits != "64bit":
    print('Error: only 64bits architectures are supported. For other OSes please write to roberto.bruttomesso@gmail.com.')
    sys.exit(1)

python_version = str(sys.version_info[0]) + '.' + str(sys.version_info[1])

libraries = None
if system_str == 'Linux':
    # yes, it will try to install the library to these three locations, I don't know
    # how to automatically select the proper one. Intrepyd will work, but some directory
    # will be polluted with unwanted _api.so
    libraries = [('lib/python' + python_version + '/site-packages/intrepyd', ['libs/linux64/_api.so']), # 'user mode' pip installs
                 ('lib/python' + python_version + '/dist-packages/intrepyd', ['libs/linux64/_api.so']), # 'superuser' pip installs
                 ('intrepyd', ['libs/linux64/_api.so'])]                                                # manual local install (egg)
elif system_str == 'Windows':
    libraries = [('Lib/site-packages/intrepyd', ['libs/windows/_api.pyd', 'libs/windows/libz3.dll'])]
elif system_str == 'Darwin':
    libraries = [('lib/python' + python_version + 'site-packages/intrepyd', ['libs/osx/_api.so'])]

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
      version=version,
      description='Intrepyd Model Checker',
      author='Roberto Bruttomesso',
      author_email='roberto.bruttomesso@gmail.com',
      maintainer='Roberto Bruttomesso',
      maintainer_email='roberto.bruttomesso@gmail.com',
      url='http://github.com/formalmethods/intrepid',
      download_url='http://github.com/formalmethods/intrepid/archive/' + version + '.tar.gz',
      install_requires=['pandas', 'antlr4-python3-runtime==4.9.1', 'flask', 'gunicorn'],
      packages=find_packages(),
      data_files=libraries,
      license='BSD-3-Clause',
      platforms=['Windows', 'Linux', 'Darwin'],
      long_description=long_desc
)
