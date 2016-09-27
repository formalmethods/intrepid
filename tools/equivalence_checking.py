#!/usr/bin/python
"""
Equivalence checking tool
"""

import utils
import argparse
import sys
import time
import intrepid as Int
import imp
import ntpath

def equivalence_check(ctx, 
                      name1, filename1, index1, 
                      name2, filename2, index2):
    """Equivalence checking of two circuits from two files passed as input"""
    print 'Importing', filename1, '...'
    script1 = imp.load_source(name1, filename1)
    print 'Importing', filename2, '...'
    script2 = imp.load_source(name2, filename2)
    print 'Constructing the miter ...'
    circuit1 = script1.get_circuit(ctx, index1)
    circuit2 = script2.get_circuit(ctx, index2)
    miter = Int.mk_circuit_miter(ctx, circuit1, circuit2)
    print 'The miter has', Int.get_outputs_size(miter), 'outputs'
    backward_reach = Int.mk_engine_br(ctx, miter)
    for output in Int.get_outputs(miter):
        Int.br_add_target(ctx, backward_reach, output)
    print 'Checking the equivalence now ...'
    res = Int.br_reach_targets(backward_reach)
    return res


def main():
    """Equivalence Checking application"""
    start_time = time.clock()

    parser = argparse.ArgumentParser(description='Executes Equivalence Checking of two circuits')
    parser.add_argument('file1',
                        type=str,
                        help='the first input script')
    parser.add_argument('index1',
                        type=int,
                        help='the index of the circuit in the first input script')
    parser.add_argument('file2',
                        type=str,
                        help='the second input script')
    parser.add_argument('index2',
                        type=int,
                        help='the index of the circuit in the second input script')
    arguments = parser.parse_args()

    file1 = arguments.file1
    name1 = ntpath.basename(file1).split('.')[0]
    index1 = arguments.index1
    file2 = arguments.file2
    name2 = ntpath.basename(file2).split('.')[0]
    index2 = arguments.index2

    utils.check_file_exists(file1)
    utils.check_file_exists(file2)

    ctx = Int.mk_ctx()
    res = equivalence_check(ctx, name1, file1, index1, name2, file2, index2)
    ret = None
    if res == Int.INT_ENGINE_RESULT_UNREACHABLE:
        print 'The circuits are EQUIVALENT'
        ret = 0
    elif res == Int.INT_ENGINE_RESULT_REACHABLE:
        print 'The circuits are NOT EQUIVALENT'
        ret = 1
    else:
        ret = 2

    Int.del_ctx(ctx)

    print '-----------------------------'
    print 'Elapsed time:', time.clock() - start_time

    return ret

if __name__ == "__main__":
    main()