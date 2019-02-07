import intrepyd as ip
from intrepyd.engine import EngineResult
from intrepyd.tools import translate_iec61131
import time

def main():
    startTime = time.time()
    # enc = translate_iec61131('tests/openplc/simple2.xml')
    enc = translate_iec61131('tests/openplc/GPCA_SW_Functional_redux.xml')

    # ctx = ip.Context()
    # circ = enc.mk_instance(ctx, 'Simple1')
    # circ.mk_circuit()
    prsTime = time.time() - startTime

    # bmc = ctx.mk_bmc()
    # bmc.add_target(negProp)
    # result = bmc.reach_targets()
    # if result == EngineResult.REACHABLE:
    # elif result == EngineResult.UNREACHABLE:
    # else:
    #     print 'An error occurred'
    # endTime = time.time() - startTime
    print 'Parse time:', prsTime
    # print 'Total time:', endTime

if __name__ == "__main__":
    main()
