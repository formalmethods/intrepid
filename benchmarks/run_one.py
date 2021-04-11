"""
Copyright (C) 2021 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 19/01/2021

Runs a lustre benchmark
"""
from intrepyd.lustre2py import translator
from intrepyd.engine import EngineResult
import psutil
import intrepyd.context
import importlib
import multiprocessing as mp
import time
import argparse as ap

def worker_br(q):
    """
    Executes a translated benchmark
    """
    enc = importlib.import_module('encoding')
    start = time.time()
    try:
        ctx = intrepyd.context.Context()
        circ = enc.mk_instance(ctx, 'br')
        circ.mk_circuit()
        breach = ctx.mk_backward_reach()
        breach.add_target(ctx.mk_not(circ.outputs['OK']))
        eng_result = breach.reach_targets()
        result = 'Unknown'
        if eng_result == EngineResult.REACHABLE:
            result = 'Invalid'
        elif eng_result == EngineResult.UNREACHABLE:
            result = 'Valid'
    except:
        result = 'Exception'
    q.put([result, time.time() - start])

def worker_bmc(q):
    """
    Executes a translated benchmark
    """
    enc = importlib.import_module('encoding')
    start = time.time()
    result = 'Unknown'
    try:
        ctx = intrepyd.context.Context()
        circ = enc.mk_instance(ctx, 'bmc')
        circ.mk_circuit()
        bmc = ctx.mk_bmc()
        bmc.add_target(ctx.mk_not(circ.outputs['OK']))
        for depth in range(100000):
            bmc.set_current_depth(depth)
            eng_result = bmc.reach_targets()
            if eng_result == EngineResult.REACHABLE:
                result = 'Invalid'
                break
    except:
        result = 'Exception'
    q.put([result, time.time() - start])

def worker_bmc_ti(q):
    """
    Executes a translated benchmark
    """
    enc = importlib.import_module('encoding')
    start = time.time()
    result = 'Unknown'
    try:
        ctx = intrepyd.context.Context()
        circ = enc.mk_instance(ctx, 'bmc_ti')
        circ.mk_circuit()
        bmc = ctx.mk_bmc()
        bmc.add_target(ctx.mk_not(circ.outputs['OK']))
        bmc.set_use_induction()
        for depth in range(100000):
            bmc.set_current_depth(depth)
            # intrepyd.api.apitrace_dump_to_file('trace.cpp')
            eng_result = bmc.reach_targets()
            if eng_result == EngineResult.REACHABLE:
                result = 'Invalid'
                break
            elif eng_result == EngineResult.UNREACHABLE:
                result = 'Valid'
                break
    except Exception as e:
        result = 'Exception ' + str(e)
    q.put([result, time.time() - start])

def killer(proc_name):
    """
    Kills the process whose name is proc_name
    """
    for proc in psutil.process_iter():
        if proc.name() == proc_name:
            proc.kill()
            break

def run_with_timeout(timeout, tool):
    """
    Runs a benchmark with a time limit
    """
    if not tool in set(['br', 'bmc', 'bmc_ti']):
        raise RuntimeError('Could not find specified tool')
    q = mp.Queue()
    if tool == 'br':
        proc = mp.Process(target=worker_br, args=(q,))
    elif tool == 'bmc':
        proc = mp.Process(target=worker_bmc, args=(q,))
    elif tool == 'bmc_ti':
        proc = mp.Process(target=worker_bmc_ti, args=(q,))
    proc.start()
    proc.join(timeout=timeout)
    if proc.is_alive():
        proc.terminate()
        return 'Timeout', timeout
    return q.get()

def run():
    argument_parser = ap.ArgumentParser(description='Runs a lustre benchmark')
    argument_parser.add_argument('filepath', type=str,
                                 help='the file to run')
    argument_parser.add_argument('tool', type=str,
                                 help='specifies the tool to be run (br, bmc, bmc_ti)')
    argument_parser.add_argument('-t', '--timeout', type=int, default=60,
                                 help='specifies the timeout in seconds for each benchmark')
    parsed_args = argument_parser.parse_args()
    try:
        fname = parsed_args.filepath
        translator.translate(fname, 'top', 'encoding.py', 'real')
        time.sleep(1) # Give some extra time to write encoding.py to a file
        print('{} {}'.format(fname, parsed_args.tool), end='')
        res, elapsed = run_with_timeout(parsed_args.timeout, parsed_args.tool)
        print(' {} {}'.format(res, elapsed))
    except IOError:
        print("File not accessible")
    finally:
        pass

if __name__ == "__main__":
    run()
