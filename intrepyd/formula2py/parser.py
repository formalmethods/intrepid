"""
Parses a formula
"""

from antlr4 import InputStream, CommonTokenStream
from intrepyd.formula2py.FormulaLexer import FormulaLexer
from intrepyd.formula2py.FormulaParser import FormulaParser
from intrepyd.formula2py.formulabuilder import FormulaBuilder

def parse_string(input_string):
    """
    Parse the provided string and create it in the provided
    intrepyd context. Returns the produced net or aborts with
    an error
    """
    lexer = FormulaLexer(InputStream(input_string))
    stream = CommonTokenStream(lexer)
    parser = FormulaParser(stream)
    tree = parser.formula()
    builder = FormulaBuilder()
    builder.visit(tree)
    return builder.formula
