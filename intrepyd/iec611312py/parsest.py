"""
Copyright (C) 2018 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 04/11/2018

This module implements the main parsing routine of PLCOPEN files
"""

from antlr4 import CommonTokenStream, InputStream
from intrepyd.iec611312py.stmtbuilder import STMTBuilder
from intrepyd.iec611312py.IEC61131ParserLexer import IEC61131ParserLexer
from intrepyd.iec611312py.IEC61131ParserParser import IEC61131ParserParser

def parseST(code, name2var, pou2inputs):
    lexer = IEC61131ParserLexer(InputStream(code))
    stream = CommonTokenStream(lexer)
    parser = IEC61131ParserParser(stream)
    tree = parser.body()
    stmtBuilder = STMTBuilder(name2var, pou2inputs)
    stmtBuilder.visit(tree)
    return stmtBuilder.statements
