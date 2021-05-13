"""
This module implements the main parsing routine of PLCOPEN files
"""

from antlr4 import CommonTokenStream, InputStream
from intrepyd.iec611312py.stmtbuilder import STMTBuilder
from intrepyd.iec611312py.IEC61131ParserLexer import IEC61131ParserLexer
from intrepyd.iec611312py.IEC61131ParserParser import IEC61131ParserParser

def parse_st(code, name2var, pou2inputs):
    """
    Parses ST code
    """
    lexer = IEC61131ParserLexer(InputStream(code))
    stream = CommonTokenStream(lexer)
    parser = IEC61131ParserParser(stream)
    tree = parser.body()
    stmt_builder = STMTBuilder(name2var, pou2inputs)
    stmt_builder.visit(tree)
    return stmt_builder.statements
