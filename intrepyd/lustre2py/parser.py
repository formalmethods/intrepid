"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017

This module implements the main parsing routine of Lustre files
"""

from antlr4 import FileStream, CommonTokenStream
from intrepyd.lustre2py.LustreLexer import LustreLexer
from intrepyd.lustre2py.LustreParser import LustreParser
from intrepyd.lustre2py.astbuilder import ASTBuilder
from intrepyd.lustre2py.ast import Ast

def parse(infile):
    """
    Parse the provided input file and translates
    into a python equivalent file for intrepyd
    """
    lexer = LustreLexer(FileStream(infile))
    stream = CommonTokenStream(lexer)
    parser = LustreParser(stream)
    tree = parser.program()
    ast_builder = ASTBuilder()
    ast_builder.visit(tree)
    return Ast(ast_builder.nodes)
