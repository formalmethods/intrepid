import intrepyd as ip
from intrepyd.engine import EngineResult
from intrepyd.tools import translate_iec61131
import time
import sys

def mk_properties(ctx, inputs, outputs):
    highestLevelAlarm = outputs['Highest_Level_Alarm']
    systemOn = inputs['System_On']
    reservoirEmpty = inputs['Reservoir_Empty']
    inTherapy = inputs['In_Therapy']
    systemOn = inputs['System_On']
    one = ctx.mk_number("1", ctx.mk_uint8_type())
    two = ctx.mk_number("2", ctx.mk_uint8_type())
    thr = ctx.mk_number("3", ctx.mk_uint8_type())
    fou = ctx.mk_number("4", ctx.mk_uint8_type())
    eqOne = ctx.mk_eq(highestLevelAlarm, one)
    eqTwo = ctx.mk_eq(highestLevelAlarm, two)
    eqThr = ctx.mk_eq(highestLevelAlarm, thr)
    eqFou = ctx.mk_eq(highestLevelAlarm, fou)
    alarmRange = ctx.mk_or(eqOne,
                        ctx.mk_or(eqTwo,
                            ctx.mk_or(eqThr, eqFou)))
    and1 = ctx.mk_and(systemOn, reservoirEmpty)
    and2 = ctx.mk_and(and1, inTherapy)
    not1 = ctx.mk_not(and2)
    emptyReservoirImpliesAlarmL4 = ctx.mk_or(eqFou, not1)
    volumeInfused = inputs['Volume_Infused']
    vtbiHigh = inputs['VTBI_High']
    geq1 = ctx.mk_geq(highestLevelAlarm, thr)
    gt1 = ctx.mk_gt(volumeInfused, vtbiHigh)
    and3 = ctx.mk_and(inTherapy, gt1)
    and4 = ctx.mk_and(systemOn, and3)
    not2 = ctx.mk_not(and4)
    volumeInfusedGreaterThanVTBIHighCausesGreaterL3Alarm = ctx.mk_or(not2, geq1)
    airInLine = inputs['Air_In_Line']
    and5 = ctx.mk_and(systemOn, airInLine)
    not3 = ctx.mk_not(and5)
    airInLineImpliesGreaterL3Alarm = ctx.mk_or(geq1, not3)
    occlusion = inputs['Occlusion']
    and6 = ctx.mk_and(systemOn, occlusion) 
    not4 = ctx.mk_not(and6)
    occlusionImpliesGreaterL3Alarm = ctx.mk_or(and6, not4)
    doorOpen = inputs['Door_Open']
    and7 = ctx.mk_and(systemOn, doorOpen) 
    not5 = ctx.mk_not(and6)
    doorOpenImpliesGreaterL3Alarm = ctx.mk_or(and7, not5)
    return [alarmRange,
            emptyReservoirImpliesAlarmL4,
            volumeInfusedGreaterThanVTBIHighCausesGreaterL3Alarm,
            airInLineImpliesGreaterL3Alarm,
            occlusionImpliesGreaterL3Alarm,
            doorOpenImpliesGreaterL3Alarm]

def main():
    startTime = time.time()
    # enc = translate_iec61131('tests/openplc/GPCA_Config.xml')
    enc = translate_iec61131('tests/openplc/GPCA_Alarm.xml')

    ctx = ip.Context()
    circ = enc.mk_instance(ctx, 'GPCA 1')
    circ.mk_circuit()

    prsTime = time.time() - startTime

    properties = mk_properties(ctx, circ.inputs, circ.outputs)
    negProp0 = ctx.mk_not(properties[2])

    bmc = ctx.mk_bmc()
    bmc.add_target(negProp0)
    bmc.set_current_depth(0)
    result = bmc.reach_targets()
    if result == EngineResult.REACHABLE:
        print 'UNSAFE'
        trace = bmc.get_last_trace()
        trace = trace.get_as_dataframe(ctx.net2name)
        print trace
    elif result == EngineResult.UNREACHABLE:
        print 'SAFE'
    else:
        print 'An error occurred'
    endTime = time.time() - startTime
    print 'Parse time:', prsTime
    print 'Total time:', endTime

if __name__ == "__main__":
    main()
