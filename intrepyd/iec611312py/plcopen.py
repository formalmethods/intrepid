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
import intrepyd
from intrepyd.iec611312py.functionblock import FunctionBlock
from intrepyd.iec611312py.function import Function
from intrepyd.iec611312py.parsest import parseST
from intrepyd.iec611312py.variable import Variable
from intrepyd.iec611312py.datatype import Primitive, Struct, Datatype

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
    pou2inputs = {}
    for pou in root.iter('pou'):
        poutype = pou.get('pouType')
        if poutype == 'function':
            inputVars, _, _ = parseInterface(pou)
            pou2inputs[pou.get('name')] = inputVars
    parsedPous = []
    for pou in root.iter('pou'):
        poutype = pou.get('pouType')
        if poutype == 'functionBlock':
            parsedPous.append(parseFunctionBlock(pou, pou2inputs))
        elif poutype == 'function':
            parsedPous.append(parseFunction(pou, pou2inputs))
        else:
            raise RuntimeError('Unsupported pou type ' + poutype)
    return parsedPous 

def parseDatatype(datatype):
    name = datatype.get('name')
    for basetype in datatype.iter('baseType'):
        for struct in basetype.iter('struct'):
            fields = {}
            for var in struct.iter('variable'):
                fields[var.get('name')] = parseVar(var, Variable.FIELD)
            Datatype.add(name, Struct(name, fields))

def parseFunctionBlock(functionBlock, pou2inputs):
    inputVars, outputVars, localVars = parseInterface(functionBlock)
    name2var = {var.name: var for var in inputVars + outputVars + localVars}
    body = parsePouBody(functionBlock, name2var, pou2inputs)
    return FunctionBlock(functionBlock.get('name'), inputVars, outputVars, localVars, body)

def parseFunction(function, pou2inputs):
    inputVars, outputVars, localVars = parseInterface(function)
    name = function.get('name')
    returnType = parseFunctionReturnType(function)
    Datatype.add(name, returnType)
    outputVars.append(Variable(name, returnType, Variable.OUTPUT))
    name2var = {var.name: var for var in inputVars + outputVars + localVars}
    body = parsePouBody(function, name2var, pou2inputs)
    return Function(name, inputVars, outputVars, localVars, body)

def parseInterface(pou):
    inputVars = []
    outputVars = []
    localVars = []
    for interface in pou.iter('interface'):
        for inVars in interface.iter('inputVars'):
            inputVars = [parseVar(var, Variable.INPUT) for var in inVars.iter('variable')]
        for outVars in interface.iter('outputVars'):
            outputVars = [parseVar(var, Variable.OUTPUT) for var in outVars.iter('variable')]
        for locVars in interface.iter('localVars'):
            localVars = [parseVar(var, Variable.LOCAL) for var in locVars.iter('variable')]
    return inputVars, outputVars, localVars

def parsePouBody(pou, name2var, pou2inputs):
    code = None
    for body in pou.iter('body'):
        for st in body.iter('ST'):
            code = st[0].text
    if code is None:
        raise RuntimeError('Could not read Pou body ' + pou.dtname)
    return parseST(code, name2var, pou2inputs)

def parseFunctionReturnType(pou):
    dtName = None 
    datatype = None
    for returnType in pou.iter('returnType'):
        dtName = returnType[0].tag
    if dtName is None:
        raise RuntimeError('Could not read Function type')
    if Datatype.isPrimitive(dtName):
        datatype = Primitive(dtName)
    if dtName == 'derived':
        name = returnType[0].get('name')
        datatype = Datatype.get(name)
    return datatype
    
def parseVar(var, kind):
    dtName = var[0][0].tag
    datatype = None
    if Datatype.isPrimitive(dtName):
        datatype = Primitive(dtName)
    if dtName == 'derived':
        name = var[0][0].get('name')
        datatype = Datatype.get(name)
    if datatype is None:
        raise RuntimeError('Could not determine variable type')
    return Variable(var.get('name'), datatype, kind)
