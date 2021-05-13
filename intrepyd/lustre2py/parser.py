"""
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
