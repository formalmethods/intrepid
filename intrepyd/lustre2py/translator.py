"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 07/05/2017

Translates a lustre file into an intrepyd equivalent
"""

import datetime
import intrepyd.lustre2py.parser as lusp
from intrepyd.lustre2py.ast2intrepyd import Ast2Intrepyd, TAB, CONTEXT, FIRSTTICK,\
                                            LUSTREDT2INTREPYDDT, BOOLTYPE, INTTYPE,\
                                            REALTYPE, LATCH2PRE, LATCHEQUIV

def compute_node_prototype(node):
    """
    Extracts node prototype
    """
    inputs = []
    for decl in node.input_decls:
        inputs += [decl.datatype.name] * len(decl.variables)
    outputs = []
    for decl in node.output_decls:
        outputs += [decl.datatype.name] * len(decl.variables)
    return (inputs, outputs)

def translate(filename, topnode, outfilename, realtype):
    """
    Translates a lustre file into a python
    """
    if not realtype in ['real', 'float16', 'float32', 'float64']:
        raise Exception('Unsupported real type ' + realtype)
    # Parse lustre into AST
    ast = lusp.parse(filename)
    # Compute nodes prototypes
    node2proto = {node.name : compute_node_prototype(node) for node in ast.nodes}
    # Translate AST into intrepyd
    encoding = ''
    properties = []
    top = None
    ast_printer = Ast2Intrepyd(node2proto, realtype)
    for node in ast.nodes:
        # Important: sort equations by dependencies!
        node.sort_equations()
        # Important: push pre operators to leaves!
        node.push_pre_in_equations()
        # ast_printer = AstPrinter()
        # print node.accept(ast_printer)
        result, props = node.accept(ast_printer)
        encoding = result
        properties += props
        if node.main:
            top = node
        elif node.name == topnode:
            top = node
    if top is None:
        raise Exception('Top node not found')

    with open(outfilename, 'w') as outfile:
        today = str(datetime.date.today())
        outfile.write('# Translated from ' + filename + ' using intrepyd.lustre2py on ' + today)
        outfile.write('\n\n')
        outfile.write('import intrepyd\n\n')
        outfile.write(LATCH2PRE + ' = {}\n')
        outfile.write(LATCHEQUIV + ' = []\n\n')
        outfile.write(encoding)
        outfile.write('def lustre2py_main(' + CONTEXT +'):\n')
        outfile.write(TAB + BOOLTYPE + ' = ' + CONTEXT + '.mk_boolean_type()\n')
        outfile.write(TAB + INTTYPE + ' = ' + CONTEXT + '.mk_int32_type()\n')
        outfile.write(TAB + REALTYPE + ' = ' + CONTEXT + '.mk_' + realtype + '_type()\n')
        outfile.write(TAB + FIRSTTICK + ' = ' + CONTEXT +\
                      '.mk_latch("' + FIRSTTICK + '", ctx.mk_boolean_type())\n')
        outfile.write(TAB + CONTEXT +\
                      '.set_latch_init_next(' + FIRSTTICK + ', ctx.mk_true(), ctx.mk_false())\n')
        index = 0
        inputs = []
        for ttype in node2proto[top.name][0]:
            name = 'i%d' % index
            outfile.write(TAB + name + ' = ' + CONTEXT + '.mk_input("' + name + '", ' +\
                          LUSTREDT2INTREPYDDT[ttype] + ')\n')
            inputs.append(name)
            index += 1
        args = CONTEXT + ', ' + FIRSTTICK
        for inp in inputs:
            args += ', ' + inp
        index = 0
        sep = ''
        outs = ''
        if len(node2proto[top.name][1]) == 0:
            raise RuntimeError('Top node has no outputs')
        for _ in node2proto[top.name][1]:
            name = 'o%d' % index
            index += 1
            outs += sep + name
            sep = ', '
        outfile.write(TAB + outs + ' = ' + top.name + '(' + args + ')\n')
        outfile.write(TAB + 'return ' + outs + '\n')
        outfile.write('\ndef lustre2py_main_ctxless():\n')
        outfile.write(TAB + CONTEXT + ' = intrepyd.Context()\n')
        outfile.write(TAB + 'return ' + CONTEXT + ', lustre2py_main(' + CONTEXT + ')\n')
        outfile.write('\nif __name__ == "__main__":\n')
        outfile.write(TAB + 'lustre2py_main_ctxless()\n\n')
