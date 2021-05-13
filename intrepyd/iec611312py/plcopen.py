"""
This module implements the main parsing routine of PLCOPEN files
"""

from xml.etree import ElementTree
from intrepyd.iec611312py.functionblock import FunctionBlock
from intrepyd.iec611312py.function import Function
from intrepyd.iec611312py.parsest import parse_st
from intrepyd.iec611312py.variable import Variable
from intrepyd.iec611312py.datatype import Primitive, Struct, Datatype

def parse_plc_open_file(infile):
    """
    Parse the provided PLCOPEN XML input file, extracts routines and tags
    """
    root = ElementTree.parse(infile).getroot()
    return _parse_pous(root)

def _parse_pous(root):
    for datatypes in root.iter('dataTypes'):
        for datatype in datatypes:
            _parse_datatype(datatype)
    pou2inputs = {}
    for pou in root.iter('pou'):
        poutype = pou.get('pouType')
        if poutype == 'function':
            inputVars, _, _ = _parse_interface(pou)
            pou2inputs[pou.get('name')] = inputVars
    parsed_pous = []
    for pou in root.iter('pou'):
        poutype = pou.get('pouType')
        if poutype == 'functionBlock':
            parsed_pous.append(_parse_function_block(pou, pou2inputs))
        elif poutype == 'function':
            parsed_pous.append(_parse_function(pou, pou2inputs))
        else:
            raise RuntimeError('Unsupported pou type ' + poutype)
    return parsed_pous

def _parse_datatype(datatype):
    name = datatype.get('name')
    for basetype in datatype.iter('baseType'):
        for struct in basetype.iter('struct'):
            fields = {}
            for var in struct.iter('variable'):
                fields[var.get('name')] = _parse_var(var, Variable.FIELD)
            Datatype.add(name, Struct(name, fields))

def _parse_function_block(functionBlock, pou2inputs):
    input_vars, output_vars, local_vars = _parse_interface(functionBlock)
    name2var = {var.name: var for var in input_vars + output_vars + local_vars}
    body = _parse_pou_body(functionBlock, name2var, pou2inputs)
    return FunctionBlock(functionBlock.get('name'), input_vars, output_vars, local_vars, body)

def _parse_function(function, pou2inputs):
    input_vars, output_vars, local_vars = _parse_interface(function)
    name = function.get('name')
    return_type = _parse_function_return_type(function)
    Datatype.add(name, return_type)
    output_vars.append(Variable(name, return_type, Variable.OUTPUT))
    name2var = {var.name: var for var in input_vars + output_vars + local_vars}
    body = _parse_pou_body(function, name2var, pou2inputs)
    return Function(name, input_vars, output_vars, local_vars, body)

def _parse_interface(pou):
    input_vars = []
    output_vars = []
    local_vars = []
    for interface in pou.iter('interface'):
        for in_vars in interface.iter('inputVars'):
            input_vars = [_parse_var(var, Variable.INPUT) for var in in_vars.iter('variable')]
        for out_vars in interface.iter('outputVars'):
            output_vars = [_parse_var(var, Variable.OUTPUT) for var in out_vars.iter('variable')]
        for loc_vars in interface.iter('localVars'):
            local_vars = [_parse_var(var, Variable.LOCAL) for var in loc_vars.iter('variable')]
    return input_vars, output_vars, local_vars

def _parse_pou_body(pou, name2var, pou2inputs):
    code = None
    for body in pou.iter('body'):
        for st in body.iter('ST'):
            code = st[0].text
    if code is None:
        raise RuntimeError('Could not read Pou body ' + pou.dtname)
    return parse_st(code, name2var, pou2inputs)

def _parse_function_return_type(pou):
    dt_name = None
    datatype = None
    for return_type in pou.iter('returnType'):
        dt_name = return_type[0].tag
    if dt_name is None:
        raise RuntimeError('Could not read Function type')
    if Datatype.is_primitive(dt_name):
        datatype = Primitive(dt_name)
    if dt_name == 'derived':
        name = pou.iter('returnType')[0].get('name')
        datatype = Datatype.get(name)
    return datatype

def _parse_var(var, kind):
    dt_name = var[0][0].tag
    datatype = None
    if Datatype.is_primitive(dt_name):
        datatype = Primitive(dt_name)
    if dt_name == 'derived':
        name = var[0][0].get('name')
        datatype = Datatype.get(name)
    if datatype is None:
        raise RuntimeError('Could not determine variable type')
    return Variable(var.get('name'), datatype, kind)
