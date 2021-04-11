import intrepyd as ip
from intrepyd.engine import EngineResult
import sudoku
import time

if __name__ == "__main__":
    startTime = time.time()
    ctx = ip.Context()
    inst = sudoku.SimulinkCircuit(ctx, 'sudoku')
    inst.mk_circuit()
    prsTime = time.time() - startTime
    negProp = inst.targets['sudoku/Proof Objective']
    bmc = ctx.mk_bmc()
    bmc.add_target(negProp)
    result = bmc.reach_targets()
    if result == EngineResult.REACHABLE:
        print 'There is a solution:'
        trace = bmc.get_last_trace()
        traceDict = trace.get_as_net_dictionary()
        cell = 1
        table = ''
        for _, value in traceDict.items():
            table += value[0] + ' '
            if cell % 9 == 0 and cell != 81:
                table += '\n'
            cell += 1
        print table
    elif result == ip.INT_ENGINE_RESULT_UNREACHABLE:
        print 'There is no possible solution'
    else:
        print 'An error occurred'
    endTime = time.time() - startTime
    print 'Parse time:', prsTime
    print 'Total time:', endTime
