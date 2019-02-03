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
from functionblock import FunctionBlock
from parsest import parseST
from variable import Variable
from datatype import Primitive, Struct, Datatype

def parsePlcOpenFile(infile):
    """
    Parse the provided PLCOPEN XML input file, extracts routines and tags
    """
    root = ElementTree.parse(infile).getroot()
    return parsePous(root)

def parsePous(root):
    for datatypes in root.iter('dataTypes'):
        for datatype in datatypes:
            parseDatatype(datatype)
    parsedPous = []
    for pou in root.iter('pou'):
        if pou.get('pouType') == 'functionBlock':
            parsedPous.append(parseFunctionBlock(pou))
        else:
            raise RuntimeError('Unsupported pou type ' + pou.pouType)
    return parsedPous 

def parseDatatype(datatype):
    name = datatype.get('name')
    for basetype in datatype.iter('baseType'):
        for struct in basetype.iter('struct'):
            fields = {}
            for var in struct.iter('variable'):
                fields[var] = parseVar(var, Variable.FIELD)
            Datatype.add(name, Struct(name, fields))

def parseFunctionBlock(functionBlock):
    inputVars, outputVars, localVars = parseFbInterface(functionBlock)
    name2var = {var.name: var for var in inputVars + outputVars + localVars}
    body = parsePouBody(functionBlock, name2var)
    return FunctionBlock(functionBlock.get('name'), inputVars, outputVars, localVars, body)

def parseFbInterface(functionBlock):
    inputVars = []
    outputVars = []
    localVars = []
    for interface in functionBlock.iter('interface'):
        for inVars in interface.iter('inputVars'):
            inputVars = [parseVar(var, Variable.INPUT) for var in inVars.iter('variable')]
        for outVars in interface.iter('outputVars'):
            outputVars = [parseVar(var, Variable.OUTPUT) for var in outVars.iter('variable')]
        for locVars in interface.iter('localVars'):
            localVars = [parseVar(var, Variable.LOCAL) for var in locVars.iter('variable')]
    return inputVars, outputVars, localVars

def parsePouBody(pou, name2var):
    code = None
    for body in pou.iter('body'):
        for st in body.iter('ST'):
            code = st[0].text
    if code is None:
        raise RuntimeError('Could not read FunctionBlock body')
    return parseST(code, name2var)
    
def parseVar(var, kind):
    dtName = var[0][0].tag
    datatype = None
    if Datatype.isPrimitive(dtName):
        datatype = Primitive(dtName)
    if datatype is None:
        raise RuntimeError('Could not determine variable type')
    return Variable(var.get('name'), datatype, kind)
