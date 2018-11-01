"""
Copyright (C) 2018 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 29/10/2018

This module implements the main parsing routine of PLCOPEN files
"""

from antlr4 import FileStream, InputStream, CommonTokenStream
from xml.etree import ElementTree

def parsePlcOpenFile(infile):
    """
    Parse the provided PLCOPEN XML input file, extracts routines and tags
    """
    root = ElementTree.parse(infile).getroot()
    return parseXmlFunctionBlocks(root)

def parseXmlFunctionBlocks(root):
    pass

def parseXmlFunctionBlock(root):
    return FunctionBlock()
