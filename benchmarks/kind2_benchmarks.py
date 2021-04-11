"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 19/01/2021

Unit tests for lustre parser
"""
import helper
from os.path import join
from intrepyd.lustre2py import translator
from intrepyd.engine import EngineResult
import intrepyd.context
import importlib
import multiprocessing as mp
import time

PATH_TO_KIND2_BENCHMARKS_ROOT = helper.from_fixture_path('kind2-benchmarks/')

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

def test_benchmark():
    """
    Tries to parse some selected benchamarks from kind2-benchmarks repo
    """
    with open('kind2-benchmarks-result-{}.txt'.format(int(time.time())), 'w') as log:
        with open('kind2-benchmarks.txt', 'r') as lines:
            count = 1
            for line in lines.readlines():
                fname = join(PATH_TO_KIND2_BENCHMARKS_ROOT, line.split()[0])
                try:
                    pos = fname.find('kind2-benchmarks')
                    name = fname[pos:]
                    translator.translate(fname, 'top', 'encoding.py', 'real')
                    time.sleep(1) # Give some extra time to write encoding.py to a file
                    for engine in ['br', 'bmc', 'bmc_ti']:
                        print('[{:3}/848] {} {}'.format(count, name, engine), end='')
                        res, elapsed = run_with_timeout(5, engine)
                        print(' {} {}'.format(res, elapsed))
                        log.write('{} {} {} {}\n'.format(name, engine, res, elapsed))
                except:
                    raise('Exception during parsing of ' + fname)
                count += 1

if __name__ == "__main__":
    test_benchmark()
