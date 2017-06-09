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
import intrepyd.api as api
import intrepyd.engine as en
import intrepyd
import multiprocessing as mp
import time
import random as rm


global_ctx = intrepyd.Context()


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


def translate_simulink(ctx, infile):
    """
    Translates a simulink file into intrepyd syntax
    """
    raise NotImplementedError
    return None


def translate_lustre(ctx, infile, topnode):
    """
    Translates a lustre file into intrepyd syntax
    """
    outmodule = 'encoding'
    outfilename = outmodule + '.py'
    tr.translate(infile, topnode, outfilename)
    enc = importlib.import_module(outmodule)
    return enc.lustre2py_main(ctx)


def translate_infile(ctx, infile, cfg):
    """
    Translates an input file depending on the suffix
    """
    outputs = None
    if infile[-4:] == '.slx' or infile[-4:] == '.mdl':
        outputs = translate_simulink(ctx, infile)
    elif infile[-4:] == '.lus' or infile[-4:] == '.ec':
        outputs = translate_lustre(ctx, infile, cfg['lustre.topnode'])
    else:
        raise RuntimeError('Did not recognize a file extension in [slx, mdl, lus, ec]')
    return outputs


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


def run_bmc(target): #, queue):
    """
    Worker for bmc
    """
    print 'Running BMC'
    # bmc = global_ctx.mk_bmc()
    # bmc.add_target(target)
    # i = 0
    # while True:
    #     bmc.set_current_depth(i)
    #     result_bmc = bmc.reach_targets()
    #     if result_bmc == en.EngineResult.REACHABLE:
    #         break
    #     i += 1
    # queue.put('r')


def run_backward_reach(target): #, queue):
    """
    Worker for backward reach
    """
    print 'Running BREACH'
    # breach = global_ctx.mk_backward_reach()
    # breach.add_target(target)
    # result_breach = breach.reach_targets()
    # if result_breach == en.EngineResult.REACHABLE:
    #     queue.put('r')
    # else:
    #     queue.put('u')


def reach_target_in_parallel(target, timeout=31536000):
    """
    Solve the given target using bmc and backward reach in parallel
    """
    assert not global_ctx is None
    # queue = mp.Queue()
    proc_bmc = mp.Process(target=run_bmc, args=(target, )) #queue))
    proc_br = mp.Process(target=run_backward_reach, args=(target, )) #queue))
    print 'Here'
    start = time.time()
    proc_bmc.start()
    proc_br.start()
    res = 'Unknown'
    # while True:
    #     time.sleep(.1)
    #     if time.time() - start >= timeout:
    #         res = 'Timeout'
    #         proc_bmc.terminate()
    #         proc_br.terminate()
    #         break
    #     if not proc_bmc.is_alive():
    #         # assert not queue.empty()
    #         # res = queue.get()
    #         proc_br.terminate()
    #         proc_br.join()
    #         break
    #     if not proc_br.is_alive():
    #         # assert not queue.empty()
    #         # res = queue.get()
    #         proc_bmc.terminate()
    #         proc_bmc.join()
    #         break
    proc_bmc.join()
    proc_br.join()
    print res, time.time() - start


def main():
    """
    Main
    """
    parsed_args = parse_arguments()
    cfg = config.Config.get_instance(parsed_args.config)
    verbose = cfg["verbose"]
    if verbose:
        print 'Parsing input file'
    outputs = translate_infile(global_ctx, parsed_args.INFILE, cfg)
    # if cfg["simulation"]:
    # simulate(ctx, parsed_args.INFILE, cfg, verbose, outputs)
    target = global_ctx.mk_not(outputs)
    # breach = ctx.mk_backward_reach()
    # breach.add_target(bad)
    # result = breach.reach_targets()
    # print result
    print reach_target_in_parallel(target)


# def maindiff():
#     """
#     Main
#     """
#     parsed_args = parse_arguments()
#     cfg = config.Config.get_instance(parsed_args.config)
#     ret = translate_infile(parsed_args.INFILE, cfg)
#     ctx = ret[0]
#     outputs = ret[1:]
#     bad = ctx.mk_not(outputs[0])
#     bmc = ctx.mk_bmc()
#     bmc.add_target(bad)
#     bmc.set_current_depth(10)
#     result_bmc = bmc.reach_targets()
#     # trace = breach.get_last_trace()
#     # print trace.get_as_dataframe(ctx.net2name)
#     print 'BMC   ', result_bmc
#     breach = ctx.mk_backward_reach()
#     breach.add_target(bad)
#     api.apitrace_dump_to_file('trace.cpp')
#     result_breach = breach.reach_targets()
#     # trace = breach.get_last_trace()
#     # print trace.get_as_dataframe(ctx.net2name)
#     print 'BREACH', result_breach



if __name__ == "__main__":
    cl.init()
    try:
        main()
        # maindiff()
    except:
        print ic.fail('ABORTED')
        raise
