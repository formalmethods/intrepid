
"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 23/09/2017

Provides some tools that could be used almost out of the box
"""

import os
import importlib
import pandas as pd
import intrepyd.lustre2py.translator as tr
import intrepyd.engine as en
import intrepyd


def translate_simulink(ctx, infile, realtype):
    """
    Translates a simulink file into intrepyd syntax
    """
    raise NotImplementedError
    return None


def translate_lustre(ctx, infile, topnode, realtype):
    """
    Translates a lustre file into intrepyd syntax
    """
    outmodule = 'encoding'
    outfilename = outmodule + '.py'
    tr.translate(infile, topnode, outfilename, realtype)
    enc = importlib.import_module(outmodule)
    return enc.lustre2py_main(ctx)


def simulate(ctx, infile, depth, outputs):
    """
    Simulates the design using default values for inputs or by taking
    input values from an existing simulation file
    """
    sim_file = os.path.basename(infile) + '.csv'
    trace = ctx.mk_trace()
    if os.path.isfile(sim_file):
        print 'Re-simulating using input values from ' + sim_file
        sim_data = pd.read_csv(sim_file, index_col=0)
        depth = trace.set_from_dataframe(sim_data, ctx.inputs)
    else:
        print 'Simulating using default values into ' + sim_file
        dpt = 0
        while dpt <= depth:
            for _, net in ctx.inputs.iteritems():
                trace.set_value(net, dpt, ctx.get_default_value(net))
            dpt += 1
    simulator = ctx.mk_simulator()
    for output in outputs:
        simulator.add_watch(output)
    simulator.simulate(trace, depth)
    dataframe = trace.get_as_dataframe(ctx.net2name)
    dataframe.to_csv(sim_file)
    print 'Simulation result written to ' + sim_file
    print dataframe
