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
    br = ip.mk_engine_br(ctx)
    ip.br_add_target(ctx, br, negProp)
    ip.br_add_watch(ctx, br, negProp)
    result = ip.br_reach_targets(br)
    print "Result:", result == ip.INT_ENGINE_RESULT_REACHABLE
    endTime = time.time() - startTime
    print 'Parse time:', prsTime
    print 'Total time:', endTime
