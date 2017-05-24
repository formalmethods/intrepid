"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017

Unit tests for lustre parser
"""

import unittest
from os import listdir
from os.path import isfile, join
from intrepyd.lustre2py import parser

class TestParserKind2(unittest.TestCase):
    """
    Unit tests for lustre parser
    """

    PATH_TO_KIND2_BENCHMARKS_ROOT = '../kind2-benchmarks'

    @staticmethod
    def test_parser_simulation():
        """
        Tests for sub-directory simulation
        """
        bpath = TestParserKind2.PATH_TO_KIND2_BENCHMARKS_ROOT + '/simulation/'
        bfiles = [bpath + f for f in listdir(bpath)\
                                if isfile(join(bpath, f)) and f.endswith('.lus')]
        for fname in bfiles:
            print 'Parsing', fname
            parser.parse(fname)

    @staticmethod
    def test_parser_protocol():
        """
        Tests for sub-directory protocol
        """
        bpath = TestParserKind2.PATH_TO_KIND2_BENCHMARKS_ROOT + '/protocol/'
        bfiles = [bpath + f for f in listdir(bpath)\
                                if isfile(join(bpath, f)) and f.endswith('.lus')]
        for fname in bfiles:
            print 'Parsing', fname
            parser.parse(fname)

    @staticmethod
    def test_parser_memory2():
        """
        Tests for sub-directory memory2
        """
        bpath = TestParserKind2.PATH_TO_KIND2_BENCHMARKS_ROOT + '/memory2/'
        bfiles = [bpath + f for f in listdir(bpath)\
                                if isfile(join(bpath, f)) and f.endswith('.lus')]
        for fname in bfiles:
            print 'Parsing', fname
            parser.parse(fname)

    @staticmethod
    def test_parser_memory1():
        """
        Tests for sub-directory memory1
        """
        bpath = TestParserKind2.PATH_TO_KIND2_BENCHMARKS_ROOT + '/memory1/'
        bfiles = [bpath + f for f in listdir(bpath)\
                                if isfile(join(bpath, f)) and f.endswith('.lus')]
        for fname in bfiles:
            print 'Parsing', fname
            parser.parse(fname)

if __name__ == "__main__":
    unittest.main()
