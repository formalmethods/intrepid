"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017

Entry point
"""

import argparse as ap
import os
import importlib
import pandas as pd
import colorama as cl
import config
import intrepyd.colors as ic
import intrepyd.lustre2py.translator as tr


def parse_arguments():
    """
    Command-line parser
    """
    arg_parser = ap.ArgumentParser(prog='intrepyd',
                                   formatter_class=ap.ArgumentDefaultsHelpFormatter)
    arg_parser.add_argument('INFILE',
                            help='The input file to process')
    arg_parser.add_argument('-c', '--config', default='config.json',
                            help='Specifies a config file')
    return arg_parser.parse_args()


def translate_simulink(infile):
    """
    Translates a simulink file into intrepyd syntax
    """
    raise NotImplementedError
    return None


def translate_lustre(infile, topnode):
    """
    Translates a lustre file into intrepyd syntax
    """
    outmodule = 'encoding'
    outfilename = outmodule + '.py'
    tr.translate(infile, topnode, outfilename)
    enc = importlib.import_module(outmodule)
    ctx = enc.lustre2py_main()
    return ctx


def translate_infile(infile, cfg):
    """
    Translates an input file depending on the suffix
    """
    ctx = None
    if infile[-4:] == '.slx' or infile[-4:] == '.mdl':
        ctx = translate_simulink(infile)
    elif infile[-4:] == '.lus' or infile[-4:] == '.ec':
        ctx = translate_lustre(infile, cfg['lustre.topnode'])
    else:
        raise RuntimeError('Did not recognize a file extension in [slx, mdl, lus, ec]')
    return ctx


def simulate(ctx, infile, cfg, verbose, outputs):
    """
    Simulates the design using default values for inputs or by taking
    input values from an existing simulation file
    """
    sim_file = os.path.basename(infile) + '.csv'
    trace = ctx.mk_trace()
    depth = cfg["simulation.depth"]
    if os.path.isfile(sim_file):
        if verbose:
            print 'Re-simulating using input values from ' + sim_file
        sim_data = pd.read_csv(sim_file, index_col=0)
        depth = trace.set_from_dataframe(sim_data, ctx.inputs)
    else:
        if verbose:
            print 'Simulating using default values into ' + sim_file
        dpt = 0
        while dpt <= depth:
            for _, net in ctx.inputs.iteritems():
                trace.set_value(net, dpt, 'false')
            dpt += 1
    simulator = ctx.mk_simulator()
    for output in outputs:
        simulator.add_watch(output)
    simulator.simulate(trace, depth)
    dataframe = trace.get_as_dataframe(ctx.net2name)
    dataframe.to_csv(sim_file)
    if verbose:
        print 'Simulation result written to ' + sim_file
    print dataframe


def main():
    """
    Main
    """
    parsed_args = parse_arguments()
    cfg = config.Config.get_instance(parsed_args.config)
    verbose = cfg["verbose"]
    if verbose:
        print 'Parsing input file'
    ret = translate_infile(parsed_args.INFILE, cfg)
    ctx = ret[0]
    outputs = ret[1:]
    if cfg["simulation"]:
        simulate(ctx, parsed_args.INFILE, cfg, verbose, outputs)


if __name__ == "__main__":
    cl.init()
    try:
        main()
    except:
        print ic.fail('ABORTED')
        raise
