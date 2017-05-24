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
import lustre2py.parser as lusp
from lustre2py.ast2intrepyd import Ast2Intrepyd, TAB, CONTEXT, FIRSTTICK,\
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

def translate(filename, topnode):
    """
    Translates a lustre file into a python
    """
    # Parse lustre into AST
    ast = lusp.parse(filename)
    # Compute nodes prototypes
    node2proto = {node.name : compute_node_prototype(node) for node in ast.nodes}
    # Translate AST into intrepyd
    encoding = ''
    properties = []
    top = None
    ast_printer = Ast2Intrepyd(node2proto)
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

    outfilename = 'encoding.py'
    with open(outfilename, 'w') as outfile:
        today = str(datetime.date.today())
        outfile.write('# Translated from ' + filename + ' using lustre2py on ' + today)
        outfile.write('\n\n')
        outfile.write('import time\n')
        outfile.write('import intrepyd\n\n')
        outfile.write(LATCH2PRE + ' = {}\n')
        outfile.write(LATCHEQUIV + ' = []\n\n')
        outfile.write(encoding)
        outfile.write('def lustre2py_main():\n')
        outfile.write(TAB + 'start = time.time()\n')
        outfile.write(TAB + CONTEXT + ' = intrepyd.Context()\n')
        outfile.write(TAB + BOOLTYPE + ' = ' + CONTEXT + '.mk_boolean_type()\n')
        outfile.write(TAB + INTTYPE + ' = ' + CONTEXT + '.mk_int32_type()\n')
        outfile.write(TAB + REALTYPE + ' = ' + CONTEXT + '.mk_real_type()\n')
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
        outfile.write(TAB + 'prop = ' + top.name + '(' + args + ')\n')

        use_br = True
        if use_br:
            outfile.write(TAB + 'br = ctx.mk_backward_reach()\n')
            outfile.write(TAB + 'br.add_target(ctx.mk_not(prop))\n')
            outfile.write(TAB + 'intrepyd.api.apitrace_dump_to_file("trace.cpp")\n')
            outfile.write(TAB + 'result = br.reach_targets()\n')
        else:
            outfile.write(TAB + 'bmc = ctx.mk_bmc()\n')
            outfile.write(TAB + 'bmc.add_target(ctx.mk_not(prop))\n')
            outfile.write(TAB + 'intrepyd.api.apitrace_dump_to_file("trace.cpp")\n')
            outfile.write(TAB + 'depth = 0\n')
            outfile.write(TAB + 'result = intrepyd.engine.EngineResult.UNKNOWN\n')
            outfile.write(TAB + 'while True:\n')
            outfile.write(TAB + TAB + 'bmc.set_current_depth(depth)\n')
            outfile.write(TAB + TAB + 'result = bmc.reach_targets()\n')
            outfile.write(TAB + TAB + 'if result == intrepyd.engine.EngineResult.REACHABLE:\n')
            outfile.write(TAB + TAB + TAB + 'break\n')
            outfile.write(TAB + TAB + 'depth += 1\n')
        outfile.write(TAB + 'return result, time.time() - start\n')

        outfile.write('\nif __name__ == "__main__":\n')
        outfile.write(TAB + 'result, mtime = lustre2py_main()\n')
        outfile.write(TAB + 'print result, mtime\n')
