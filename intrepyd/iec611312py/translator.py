"""
Copyright (C) 2018 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 10/01/2019
"""

from intrepyd.iec611312py.plcopen import parsePlcOpenFile
from intrepyd.iec611312py.flattener import flattenStmtBlock
from intrepyd.iec611312py.flatstmt2intrepyd import FlatStmt2Intrepyd
import datetime

TAB = 4 * ' '
FIRSTTICK = 'first_tick'
CONTEXT = 'self.context'

def translate(filename, outfilename):
    """
    Translates an openPLC ST file into intrepyd
    """
    pous = parsePlcOpenFile(filename)
    flattened_statements = flattenStmtBlock(pous[0].statements)

    with open(outfilename, 'w') as outfile:
        today = str(datetime.date.today())
        outfile.write('# Translated from ' + filename + ' using intrepyd.iec611312py on ' + today)
        outfile.write('\n\n')
        outfile.write('import intrepyd as ip\n')
        outfile.write('import intrepyd.circuit\n')
        outfile.write('import collections\n\n')
        outfile.write('class IEC61131Circuit(ip.circuit.Circuit):\n')
        outfile.write(TAB + 'def __init__(self, ctx, name):\n')
        outfile.write(TAB + TAB + 'ip.circuit.Circuit.__init__(self, ctx, name)\n')
        outfile.write(TAB + TAB + 'bool_type = ' + CONTEXT + '.mk_boolean_type()\n')
        outfile.write(TAB + TAB + FIRSTTICK + ' = ' + CONTEXT +\
                      '.mk_latch("' + FIRSTTICK + '", bool_type)\n')
        outfile.write(TAB + TAB + CONTEXT +\
                      '.set_latch_init_next(' + FIRSTTICK + ', ctx.mk_true(), ctx.mk_false())\n')
        outfile.write('\n')
        outfile.write(TAB + 'def _mk_inputs(self):\n')
        for inp in pous[0].input_vars:
            outfile.write(TAB + TAB + inp.name + ' = ' + CONTEXT +\
                          ".mk_input('" + inp.name + "', "\
                                        + datatype2py(inp.datatype) + ')\n')
            outfile.write(TAB + TAB + "self.inputs['" + inp.name + "'] = " + inp.name + '\n')
        if len(pous[0].input_vars) == 0:
            outfile.write(TAB + TAB + 'pass\n')
        outfile.write('\n')
        outfile.write(TAB + 'def _mk_naked_circuit_impl(self, inputs):\n')
        outfile.write(TAB + TAB + 'input_keys = list(inputs)\n')
        args = ''
        sep = ''
        for inp in pous[0].input_vars:
            args += sep + 'inputs[input_keys["' + inp.name + '"]]'
            sep = ', '
        sep = ''
        outs = ''
        if len(pous[0].output_vars) == 0:
            raise RuntimeError('Pou has no outputs')
        for out in pous[0].output_vars:
            outs += sep + out.name
            sep = ', '
        outfile.write(TAB + TAB + outs + ' = self.' + pous[0].dtname + '(' + args + ')\n')
        outfile.write(TAB + TAB + 'outputs = collections.OrderedDict()\n')
        for out in pous[0].output_vars:
            outfile.write(TAB + TAB + "outputs['" + out.name + "'] = " + out.name + "\n")
        outfile.write(TAB + TAB + 'return outputs\n')
        outfile.write('\n')
        args = ''
        sep = ''
        for inp in pous[0].input_vars:
            args += sep + inp.name
            sep = ', '
        outfile.write(TAB + 'def ' + pous[0].dtname + '(self, ' + args + '):\n')
        var2latch = {}
        for var in pous[0].local_vars:
            outfile.write(TAB + TAB +\
                          CONTEXT + '.mk_latch("' + var.name + '", ' +\
                          datatype2py(var.datatype) + ')\n')
            # COMPUTE INIT VALUE
            var2latch[var.name] = (var.name, init)
        flatstmt2intrepyd = FlatStmt2Intrepyd(8, CONTEXT, var2latch)
        flatstmt2intrepyd.processStatements(flattened_statements)
        outfile.write(flatstmt2intrepyd.result)
        sep = ''
        outs = ''
        if len(pous[0].output_vars) == 0:
            raise RuntimeError('Pou has no outputs')
        for out in pous[0].output_vars:
            outs += sep + out.name
            sep = ', '
        outfile.write(TAB + TAB + 'return ' + outs)
        outfile.write('\n\n')
        outfile.write('def mk_instance(ctx, name):\n')
        outfile.write(TAB + 'return IEC61131Circuit(ctx, name)\n')
        outfile.write('\n')

def datatype2py(datatype):
    if datatype.dtname == 'USINT':
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
    raise RuntimeError('Type not found ' + datatype.dtname)
