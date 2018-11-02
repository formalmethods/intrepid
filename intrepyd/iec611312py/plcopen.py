"""
Copyright (C) 2018 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 29/10/2018

This module implements the main parsing routine of PLCOPEN files
"""

from antlr4 import CommonTokenStream, InputStream
from xml.etree import ElementTree
from intrepyd.iec611312py.functionblock import FunctionBlock
from intrepyd.iec611312py.datatype import Datatype
from intrepyd.iec611312py.variable import Variable
from intrepyd.iec611312py.astbuilder import ASTBuilder
from intrepyd.iec611312py.IEC61131ParserLexer import IEC61131ParserLexer
from intrepyd.iec611312py.IEC61131ParserParser import IEC61131ParserParser
from intrepyd.iec611312py.astbuilder import ASTBuilder
# from intrepyd.iec611312py.ast import Ast
import re

def parsePlcOpenFile(infile):
    """
    Parse the provided PLCOPEN XML input file, extracts routines and tags
    """
    root = ElementTree.parse(infile).getroot()
    return parsePous(root)

def parsePous(root):
    for pou in root.iter('pou'):
        if pou.get('pouType') == 'functionBlock':
            parseFunctionBlock(pou)
        else:
            raise RuntimeError('Unsupported pou type ' + pou.pouType)

def parseFunctionBlock(functionBlock):
    inputVars, outputVars = parseFbInterface(functionBlock)
    name2var = {var.name: var for var in inputVars + outputVars}
    body = parseFbBody(functionBlock, name2var)
    return FunctionBlock(functionBlock.get('name'), inputVars, outputVars, None, body)

def parseFbInterface(functionBlock):
    inputVars = None
    outputVars = None
    for interface in functionBlock.iter('interface'):
        for inVars in interface.iter('inputVars'):
            inputVars = [parseVar(var, Variable.INPUT) for var in inVars.iter('variable')]
        for outVars in interface.iter('outputVars'):
            outputVars = [parseVar(var, Variable.OUTPUT) for var in outVars.iter('variable')]
    return inputVars, outputVars

def parseFbBody(functionBlock, name2var):
    code = None
    for body in functionBlock.iter('body'):
        for st in body.iter('ST'):
            code = st[0].text
    if code is None:
        raise RuntimeError('Could not read FunctionBlock body')
    lexer = IEC61131ParserLexer(InputStream(code))
    stream = CommonTokenStream(lexer)
    parser = IEC61131ParserParser(stream)
    tree = parser.body()
    ast_builder = ASTBuilder(name2var)
    ast_builder.visit(tree)
    return ast_builder.statements
    
def parseVar(var, kind):
    dtName = var[0][0].tag
    dtKind = computeDataKind(dtName)
    datatype = Datatype(dtName, dtKind)
    return Variable(var.get('name'), datatype, kind)

def computeDataKind(dtName):
    intPattern = re.compile('[SDL]?U?INT')
    realPattern = re.compile('L?REAL')
    if dtName == 'BOOL' or intPattern.match(dtName) or realPattern.match(dtName):
        return 'PRIMITIVE'
    raise RuntimeError('Unsupported variable type ' + dtName)
