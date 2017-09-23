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
import multiprocessing as mp
import time
import importlib
import subprocess as sp
import pandas as pd
import colorama as cl
import intrepyd.colors as ic
import intrepyd.lustre2py.translator as tr
import intrepyd.engine as en
import intrepyd.config as cg
import intrepyd.tools as ts
import intrepyd


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


def translate_infile(ctx, infile, cfg):
    """
    Translates an input file depending on the suffix
    """
    outputs = None
    if infile[-4:] == '.slx' or infile[-4:] == '.mdl':
        outputs = ts.translate_simulink(ctx, infile, cfg['type.real'])
    elif infile[-4:] == '.lus' or infile[-4:] == '.ec':
        outputs = ts.translate_lustre(ctx, infile, cfg['lustre.topnode'], cfg['type.real'])
    else:
        raise RuntimeError('Did not recognize a file extension in [slx, mdl, lus, ec]')
    return outputs


def run_bmc(engine, cfg):
    max_depth = cfg["bmc.max_depth"]
    verbose = cfg["verbose"]
    for depth in range(0, max_depth):
        if verbose:
            print "BMC depth", depth
        engine.set_current_depth(depth)
        res = engine.reach_targets()
        if res == en.EngineResult.REACHABLE:
            return res
    return en.EngineResult.UNKNOWN


def run_br(engine, cfg):
    return engine.reach_targets()


def verify(ctx, cfg, output):
    bad = ctx.mk_not(output)
    engine_string = cfg["verification.engine"]
    engine = None
    verbose = cfg["verbose"]
    if verbose:
        print 'Verifying using', engine_string
    if engine_string == "bmc":
        engine = ctx.mk_bmc()
    elif engine_string == "br":
        engine = ctx.mk_backward_reach() 
    else:
        raise RuntimeError("Unknown engine " + engine_string)
    engine.add_target(bad)
    intrepyd.api.apitrace_dump_to_file("trace.cpp")
    res = en.EngineResult.UNKNOWN
    if engine_string == "bmc":
        res = run_bmc(engine, cfg)
    elif engine_string == "br":
        res = run_br(engine, cfg)
    else:
        raise RuntimeError("Unknown engine " + engine_string)
    if res == en.EngineResult.REACHABLE:
        trace_file = os.path.basename(infile) + '.csv'
        trace = engine.get_last_trace()
        dataframe = trace.get_as_dataframe(ctx.net2name)
        dataframe.to_csv(trace_file)
        if verbose:
            print 'Trace written to ' + trace_file
    print res


def main():
    """
    Main
    """
    parsed_args = parse_arguments()
    infile = parsed_args.INFILE
    cfg = cg.Config.get_instance(parsed_args.config)
    verbose = cfg["verbose"]
    if verbose:
        print 'Parsing', infile
    ctx = intrepyd.Context()
    outputs = translate_infile(ctx, infile, cfg, 'main')
    if verbose:
        print 'Translated as encoding_main.py'
    if cfg["verification"]:
        for output in outputs:
            verify(ctx, cfg, output)


if __name__ == "__main__":
    cl.init()
    try:
        main()
    except:
        print ic.fail('ABORTED')
        raise
