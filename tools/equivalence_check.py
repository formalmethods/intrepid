#!/usr/bin/python
"""
Equivalence checking tool
"""

import argparse
import sys
import time
import intrepid as Int

def check_file_exists(filename):
    """Checks is a file exists"""
    try:
        open(filename, 'r')
    except IOError:
        print 'Error: ', filename, 'does not exists'
        sys.exit(1)
    print 'File', filename, 'exists!'


def equivalence_check(ctx, filename1, filename2):
    """Equivalence checking of the two ST files passed as input"""
    print 'Parsing', filename1, '...'
    circuit1 = Int.mk_circuit_from_st_file(ctx, filename1)
    print 'Parsing', filename2, '...'
    circuit2 = Int.mk_circuit_from_st_file(ctx, filename2)
    print 'Constructing the miter ...'
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

    parser = argparse.ArgumentParser(description='Executes Equivalence Checking of two ST files')
    parser.add_argument('file1',
                        type=str,
                        help='the first file')
    parser.add_argument('file2',
                        type=str,
                        help='the second file')
    arguments = parser.parse_args()

    file1 = arguments.file1
    file2 = arguments.file2

    check_file_exists(file1)
    check_file_exists(file2)

    ctx = Int.mk_ctx()
    res = equivalence_check(ctx, file1, file2)
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