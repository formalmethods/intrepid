"""
Copyright (C) 2018 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 10/01/2019
"""

from intrepyd.iec611312py.plcopen import parsePlcOpenFile
from intrepyd.iec611312py.flattener import Flattener
from intrepyd.iec611312py.flatstmt2intrepyd import FlatStmt2Intrepyd
from intrepyd.iec611312py.inferdatatype import InferDatatypeBottomUp, InferDatatypeTopDown
from intrepyd.iec611312py.datatype import Datatype
from utils import sanitizeName
import datetime
import sys

TAB = 4 * ' '
FIRSTTICK = 'first_tick'
CONTEXT = 'self.context'


def flush():
    sys.stdout.flush()


def translate(filename, outfilename):
    """
    Translates an openPLC ST file into intrepyd
    """
    print('Parsing')
    pous = parsePlcOpenFile(filename)
    print('... done')
    flush()
    outfile = open(outfilename, 'w')
    top_level = True
    for pou in pous:
        name2var = {var.name: var for var in pou.input_vars +
                    pou.local_vars + pou.output_vars}
        if top_level:
            dumpHeader(pou, name2var, filename, outfile)
        translatePou(pou, name2var, outfile)
        top_level = False
    dumpFooter(outfile)


def translatePou(pou, name2var, outfile):
    print('Translating POU', pou.dtname)

    print('Flattening')
    flattener = Flattener()
    flattened_statements = flattener.flattenStmtBlock(pou.statements)
    print('... done')
    flush()

    print('Inferring datatypes bottom up')
    idbu = InferDatatypeBottomUp()
    idbu.processStatements(flattened_statements)
    print('... done')
    flush()

    print('Inferring datatypes top down')
    idtd = InferDatatypeTopDown()
    idtd.processStatements(flattened_statements)
    print('... done')
    flush()

    #
    # Prepare the formal arguments of the main function
    #
    args = ''
    sep = ''
    for var in pou.input_vars:
        if not Datatype.isPrimitive(var.datatype.dtname):
            for name, _ in var.datatype.fields.items():
                args += sep + sanitizeName(var.name + '.' + name)
                sep = ', '
        else:
            args += sep + var.name
            sep = ', '
    #
    # Function declaration
    #
    outfile.write(
        TAB + 'def ' + pou.dtname + '(self, ' + args + '):\n')
    flush()
    var2latch = {}
    for var in pou.local_vars:
        declareLocal(var, outfile, var2latch, name2var)
    for var in pou.output_vars:
        declareOutput(var, outfile, name2var)
    flush()
    print('  Writing statements')
    flatstmt2intrepyd = FlatStmt2Intrepyd(8, CONTEXT, var2latch, outfile)
    flatstmt2intrepyd.processStatements(flattened_statements)
    print('  ... done')
    flush()
    sep = ''
    outs = ''
    if len(pou.output_vars) == 0:
        raise RuntimeError('Pou has no outputs')
    print('  Writing outputs')
    for out in pou.output_vars:
        if not Datatype.isPrimitive(out.datatype.dtname):
            for name, _ in out.datatype.fields.items():
                qualifiedName = out.name + '.' + name
                outs += sep + sanitizeName(qualifiedName)
                sep = ', '
        else:
            outs += sep + out.name
            sep = ', '
    print('  ... done')
    flush()
    outfile.write(TAB + TAB + 'return ' + outs)
    outfile.write('\n\n')


def dumpHeader(pou, name2var, filename, outfile):
    today = str(datetime.date.today())
    outfile.write('# Translated from ' + filename +
                  ' using intrepyd.iec611312py on ' + today)
    outfile.write('\n\n')
    outfile.write('import intrepyd as ip\n')
    outfile.write('import intrepyd.circuit\n')
    outfile.write('import collections\n\n')
    outfile.write('class IEC61131Circuit(ip.circuit.Circuit):\n')
    outfile.write(TAB + 'def __init__(self, ctx, name):\n')
    outfile.write(
        TAB + TAB + 'ip.circuit.Circuit.__init__(self, ctx, name)\n')
    outfile.write(TAB + TAB + 'bool_type = ' +
                  CONTEXT + '.mk_boolean_type()\n')
    outfile.write(TAB + TAB + FIRSTTICK + ' = ' + CONTEXT +
                  '.mk_latch("' + FIRSTTICK + '", bool_type)\n')
    outfile.write(TAB + TAB + CONTEXT +
                  '.set_latch_init_next(' + FIRSTTICK + ', ' + CONTEXT + '.mk_true(), ' + CONTEXT + '.mk_false())\n')
    outfile.write('\n')
    outfile.write(TAB + 'def _mk_inputs(self):\n')
    for inp in pou.input_vars:
        declareInput(inp, outfile, name2var)
    if len(pou.input_vars) == 0:
        outfile.write(TAB + TAB + 'pass\n')
    outfile.write('\n')
    outfile.write(TAB + 'def _mk_naked_circuit_impl(self, inputs):\n')
    outfile.write(TAB + TAB + 'input_keys = list(inputs)\n')
    #
    # Prepare input keys that are actual arguments of main function
    #
    args = ''
    sep = ''
    i = 0
    for var in pou.input_vars:
        if not Datatype.isPrimitive(var.datatype.dtname):
            for _, _ in var.datatype.fields.items():
                args += sep + 'inputs[input_keys[' + str(i) + ']]'
                sep = ', '
                i += 1
        else:
            args += sep + 'inputs[input_keys[' + str(i) + ']]'
            sep = ', '
            i += 1
    #
    # Prepare the outputs
    #
    sep = ''
    outs = ''
    if len(pou.output_vars) == 0:
        raise RuntimeError('Pou has no outputs')
    for out in pou.output_vars:
        if not Datatype.isPrimitive(out.datatype.dtname):
            for name, _ in out.datatype.fields.items():
                outs += sep + sanitizeName(out.name + '.' + name)
                sep = ', '
        else:
            outs += sep + out.name
            sep = ', '
    #
    # Calls the main function
    #
    outfile.write(TAB + TAB + outs + ' = self.' +
                  pou.dtname + '(' + args + ')\n')
    outfile.write(TAB + TAB + 'outputs = collections.OrderedDict()\n')
    #
    # Inserts the outputs into the dictionary
    #
    for out in pou.output_vars:
        if not Datatype.isPrimitive(out.datatype.dtname):
            for name, _ in out.datatype.fields.items():
                qualifiedName = out.name + '.' + name
                outfile.write(
                    TAB + TAB + "outputs['" + qualifiedName + "'] = " + sanitizeName(qualifiedName) + "\n")
        else:
            outfile.write(
                TAB + TAB + "outputs['" + out.name + "'] = " + out.name + "\n")
    outfile.write(TAB + TAB + 'return outputs\n')
    outfile.write('\n')


def dumpFooter(outfile):
    outfile.write('def mk_instance(ctx, name):\n')
    outfile.write(TAB + 'return IEC61131Circuit(ctx, name)\n')
    outfile.write('\n')


def datatype2py(datatype):
    if datatype.dtname == 'BOOL':
        return CONTEXT + '.mk_boolean_type()'
    elif datatype.dtname == 'USINT':
        return CONTEXT + '.mk_uint8_type()'
    elif datatype.dtname == 'UINT':
        return CONTEXT + '.mk_uint16_type()'
    elif datatype.dtname == 'UDINT':
        return CONTEXT + '.mk_uint32_type()'
    elif datatype.dtname == 'ULINT':
        return CONTEXT + '.mk_uint64_type()'
    elif datatype.dtname == 'SINT':
        return CONTEXT + '.mk_int8_type()'
    elif datatype.dtname == 'INT':
        return CONTEXT + '.mk_int16_type()'
    elif datatype.dtname == 'DINT':
        return CONTEXT + '.mk_int32_type()'
    elif datatype.dtname == 'LINT':
        return CONTEXT + '.mk_int64_type()'
    elif datatype.dtname == 'REAL':
        return CONTEXT + '.mk_float32_type()'
    elif datatype.dtname == 'LREAL':
        return CONTEXT + '.mk_float64_type()'
    return None


def datatype2init(datatype):
    if datatype.dtname == 'BOOL':
        return CONTEXT + '.mk_false()'
    return CONTEXT + '.mk_number("0", ' + datatype2py(datatype) + ')'


def declareInputHelper(name, datatype, outfile):
    saneName = sanitizeName(name)
    datatypepy = datatype2py(datatype)
    if datatypepy is None:
        raise RuntimeError('Datatype for ' + datatype.dtname + ' is None')
    outfile.write(TAB + TAB + saneName + ' = ' + CONTEXT +
                  ".mk_input('" + name + "', "
                                + datatypepy + ')\n')
    outfile.write(
        TAB + TAB + "self.inputs['" + name + "'] = " + saneName + '\n')


def declareInput(inp, outfile, name2var):
    datatypepy = datatype2py(inp.datatype)
    if datatypepy is None:
        if not inp.name in name2var:
            raise RuntimeError('Could not find datatype for ' + inp.name)
        var = name2var[inp.name]
        for fieldName, fieldVar in var.datatype.fields.items():
            declareInputHelper(var.name + '.' + fieldName,
                               fieldVar.datatype, outfile)
    else:
        declareInputHelper(inp.name, inp.datatype, outfile)


def declareOutput(out, outfile, name2var):
    datatypepy = datatype2py(out.datatype)
    if datatypepy is None:
        if not out.name in name2var:
            raise RuntimeError('Could not find datatype for ' + out.name)
        var = name2var[out.name]
        for fieldName, fieldVar in var.datatype.fields.items():
            declareOutputHelper(var.name + '.' + fieldName,
                                fieldVar.datatype, outfile)
    else:
        declareOutputHelper(out.name, out.datatype, outfile)


def declareOutputHelper(name, datatype, outfile):
    saneName = sanitizeName(name)
    datatypepy = datatype2py(datatype)
    if datatypepy is None:
        raise RuntimeError('Datatype for ' + datatype.dtname + ' is None')
    outfile.write(TAB + TAB + saneName + ' = ' + datatype2init(datatype) + '\n')


def declareLocalHelper(name, datatype, outfile, var2latch):
    saneName = sanitizeName(name)
    datatypepy = datatype2py(datatype)
    if datatypepy is None:
        raise RuntimeError('Datatype for ' + datatype.dtname + ' is None')
    outfile.write(TAB + TAB +
                  saneName + ' = ' + CONTEXT + '.mk_latch("' + name + '", ' +
                  datatypepy + ')\n')
    init = datatype2init(datatype)
    var2latch[name] = (saneName, init)


def declareLocal(var, outfile, var2latch, name2var):
    datatypepy = datatype2py(var.datatype)
    if datatypepy is None:
        if not var.name in name2var:
            raise RuntimeError('Could not find datatype for ' + var.name)
        var = name2var[var.name]
        for fieldName, fieldVar in var.datatype.fields.items():
            declareLocalHelper(var.name + '.' + fieldName,
                               fieldVar.datatype, outfile, var2latch)
    else:
        declareLocalHelper(var.name, var.datatype, outfile, var2latch)
