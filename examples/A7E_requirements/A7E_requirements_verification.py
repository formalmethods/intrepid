import intrepid as ip
import intrepid.utils
import A7E_requirements
import time
import sys

def mk_negation_of_property_3(ctx, inst):
    navigationUpdateMode = inst.nets['A7E_requirements/NU/Mode']
    weaponDeliveryMode = inst.nets['A7E_requirements/WD/Mode']
    aflyUpdate = inst.nets['A7E_requirements/NU/AflyUpd']
    boc = inst.nets['A7E_requirements/WD/BOC']
    sboc = inst.nets['A7E_requirements/WD/SBOC']
    pre = ip.mk_eq(ctx, navigationUpdateMode, aflyUpdate)
    post1 = ip.mk_neq(ctx, weaponDeliveryMode, boc)
    post2 = ip.mk_neq(ctx, weaponDeliveryMode, sboc)
    post = ip.mk_and(ctx, post1, post2)
    # NavUpd=AflyUpd /\ WpnDel!=BOC /\ WpnDel!=SBOC
    target = ip.mk_and(ctx, pre, post)
    return target

if __name__ == "__main__":
    startTime = time.time()
    ctx = ip.mk_ctx()
    inst = A7E_requirements.SimulinkCircuit(ctx, 'A7E')
    inst.mk_circuit()
    wdm = inst.nets['A7E_requirements/WD/Mode']
    num = inst.nets['A7E_requirements/NU/Mode']
    prsTime = time.time() - startTime
    negProp3 = mk_negation_of_property_3(ctx, inst) 

    br = ip.mk_engine_br(ctx)
    ip.br_add_target(ctx, br, negProp3)
    ip.br_add_watch(ctx, br, negProp3)
    result = ip.br_reach_targets(br)
    print "Unreachable: ", result == ip.INT_ENGINE_RESULT_UNREACHABLE

    # bmc = ip.mk_engine_bmc(ctx)
    # wdmfs = inst.nets['A7E_requirements/WDMFS']
    # ow = inst.nets['A7E_requirements/Other_Weapon']
    # wmboc = inst.nets['A7E_requirements/ro19'] 
    # ip.bmc_add_watch(ctx, bmc, wdmfs)
    # ip.bmc_add_watch(ctx, bmc, ow)
    # ip.bmc_add_watch(ctx, bmc, wmboc)
    # ip.bmc_add_target(ctx, bmc, negProp3)
    # for depth in range(0, 50):
    #     print "Trying depth", depth
    #     ip.set_bmc_current_depth(bmc, depth)
    #     result = ip.bmc_reach_targets(bmc)
    #     if result == ip.INT_ENGINE_RESULT_REACHABLE:
    #         print "Reachable"
    #         cex = ip.bmc_get_counterexample(ctx, bmc, negProp3)
    #         cexDict = ip.utils.counterexample_get_as_dictionary(ctx, cex, inst.inputs, { 'NUM' : num,\
    #         										 'WDM' : wdm,\
    #     										 'WDMFS' : wdmfs,\
    #     										 'OthWp' : ow,\
    #     										 'WM=BOC' : wmboc })
    #         cexDf = ip.utils.counterexample_get_as_dataframe(cexDict)
    #         print cexDf
    #         break
    #     sys.stdout.flush()
    # ip.del_ctx(ctx)

    endTime = time.time() - startTime
    print 'Parse time:', prsTime
    print 'Total time:', endTime
