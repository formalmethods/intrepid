import intrepid as ip
import sudoku
import time

if __name__ == "__main__":
    startTime = time.time()
    ctx = ip.mk_ctx()
    inst = sudoku.SimulinkCircuit(ctx, 'sudoku')
    inst.mk_circuit()
    prsTime = time.time() - startTime
    negProp = inst.proof_objectives['sudoku/Proof Objective']
    bmc = ip.mk_engine_bmc(ctx)
    ip.bmc_add_target(ctx, bmc, negProp)
    ip.bmc_add_watch(ctx, bmc, negProp)
    result = ip.bmc_reach_targets(bmc)
    if result == ip.INT_ENGINE_RESULT_REACHABLE:
        print 'There is a solution:'
        cex = ip.bmc_get_counterexample(ctx, bmc, negProp)
        cexDict = ip.utils.counterexample_get_as_dictionary(ctx, cex, inst.inputs, {})
        cell = 1
        table = ''
        for _, value in cexDict.iteritems():
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
