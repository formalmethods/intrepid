import intrepyd as ip
from intrepyd.engine import EngineResult
import A7E_requirements
import time
import sys

# Property 3:
#
# If the system is in WpnDel modes BOC or SBOC,
# then NavUpd is in AflyUpd
#
#
# In formula:
#
# F := (WpnDel=BOC \/ WpnDel=SBOC) -> NavUpd=AflyUpd
#
# 
# Reachability query: !F
#
# !F                                                                    <->
# (WpnDel=BOC \/ WpnDel=SBOC) /\ NavUpd!=AflyUpd                        <->
# (WpnDel=BOC /\ NavUpd!=AflyUpd) \/ (WpnDel=SBOC /\ NavUpd!=AflyUpd)
def mk_negation_of_property_3(ctx, inst):
    navigationUpdateMode = inst.nets['A7E_requirements/NU/Mode']
    weaponDeliveryMode = inst.nets['A7E_requirements/WD/Mode']
    aflyUpdate = inst.nets['A7E_requirements/NU/AflyUpd']
    boc = inst.nets['A7E_requirements/WD/BOC']
    sboc = inst.nets['A7E_requirements/WD/SBOC']
    navAfly = ctx.mk_neq(navigationUpdateMode, aflyUpdate)
    wpnBoc = ctx.mk_eq(weaponDeliveryMode, boc)
    wpnSboc = ctx.mk_eq(weaponDeliveryMode, sboc)
    # NavUpd!=AflyUpd /\ WpnDel=BOC (1)
    target1 = ctx.mk_and(navAfly, wpnBoc)
    # NavUpd!=AflyUpd /\ WpnDel=SBOC (2)
    target2 = ctx.mk_and(navAfly, wpnSboc)
    # (1) \/ (2)
    target = ctx.mk_or(target1, target2)
    return target

# Converse of Property 3:
#
# If the system is in NavUpd mode AflyUpd,
# then WpnDel is in either BOC or SBOC
#
#
# In formula:
#
# CF := (WpnDel=BOC \/ WpnDel=SBOC) <- NavUpd=AflyUpd
#
# 
# Reachability query: !CF
#
# !CF                                              <->
# !(WpnDel=BOC \/ WpnDel=SBOC) /\ NavUpd=AflyUpd   <->
# WpnDel!=BOC /\ WpnDel!=SBOC /\ NavUpd=AflyUpd
def mk_negation_of_converse_of_property_3(ctx, inst):
    navigationUpdateMode = inst.nets['A7E_requirements/NU/Mode']
    weaponDeliveryMode = inst.nets['A7E_requirements/WD/Mode']
    aflyUpdate = inst.nets['A7E_requirements/NU/AflyUpd']
    boc = inst.nets['A7E_requirements/WD/BOC']
    sboc = inst.nets['A7E_requirements/WD/SBOC']
    navAfly = ctx.mk_eq(navigationUpdateMode, aflyUpdate)
    wpnBoc = ctx.mk_neq(weaponDeliveryMode, boc)
    wpnSboc = ctx.mk_neq(weaponDeliveryMode, sboc)
    # NavUpd=AflyUpd /\ WpnDel!=BOC (1)
    tmp = ctx.mk_and(navAfly, wpnBoc)
    # (1) /\ WpnDel=SBOC
    target = ctx.mk_and(tmp, wpnSboc)
    return target

if __name__ == "__main__":
    startTime = time.time()
    ctx = ip.Context()
    inst = A7E_requirements.SimulinkCircuit(ctx, 'A7E')
    inst.mk_circuit()
    wdm = inst.nets['A7E_requirements/WD/Mode']
    num = inst.nets['A7E_requirements/NU/Mode']
    prsTime = time.time() - startTime
    negProp3 = mk_negation_of_property_3(ctx, inst) 
    convnegProg3 = mk_negation_of_converse_of_property_3(ctx, inst)

    br = ctx.mk_backward_reach()
    br.add_target(negProp3)
    br.add_target(convnegProg3)
    result = br.reach_targets()
    print "Unreachable?", result == EngineResult.UNREACHABLE

    endTime = time.time() - startTime
    print 'Parse time:', prsTime
    print 'Total time:', endTime
