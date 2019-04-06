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
    zer = ctx.mk_number("0", ctx.mk_uint8_type())
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
                                     ctx.mk_or(eqThr, eqFou)), 'alarm_range')
    and1 = ctx.mk_and(systemOn, reservoirEmpty)
    and2 = ctx.mk_and(and1, inTherapy)
    not1 = ctx.mk_not(and2)
    emptyReservoirImpliesAlarmL4 = ctx.mk_or(eqFou, not1, 'empty_reservoir_implies_alarm_L4')
    volumeInfused = inputs['Volume_Infused']
    vtbiHigh = inputs['VTBI_High']
    geq1 = ctx.mk_geq(highestLevelAlarm, thr)
    gt1 = ctx.mk_gt(volumeInfused, vtbiHigh)
    and3 = ctx.mk_and(inTherapy, gt1)
    and4 = ctx.mk_and(systemOn, and3)
    not2 = ctx.mk_not(and4)
    volumeInfusedGreaterThanVTBIHighCausesGreaterL3Alarm = ctx.mk_or(not2, geq1, 'volume_infused_greater_than_VTBIHigh_causes_greater_L3_alarm')
    airInLine = inputs['Air_In_Line']
    and5 = ctx.mk_and(systemOn, airInLine)
    not3 = ctx.mk_not(and5)
    airInLineImpliesGreaterL3Alarm = ctx.mk_or(geq1, not3, 'air_in_line_implies_greater_L3_alerm')
    occlusion = inputs['Occlusion']
    and6 = ctx.mk_and(systemOn, occlusion)
    not4 = ctx.mk_not(and6)
    geq2 = ctx.mk_geq(highestLevelAlarm, thr)
    occlusionImpliesGreaterL3Alarm = ctx.mk_or(geq2, not4, 'occlusion_implies_greater_L3_alarm')
    doorOpen = inputs['Door_Open']
    and7 = ctx.mk_and(systemOn, doorOpen)
    not5 = ctx.mk_not(and6)
    doorOpenImpliesGreaterL3Alarm = ctx.mk_or(and7, not5, 'door_open_implies_greater_L3_alarm')
    disableAudio = inputs['Disable_Audio']
    audioNotificationCommand = outputs['Audio_Notification_Command']
    isAudioDisabled = outputs['Is_Audio_Disabled']
    eq2 = ctx.mk_eq(audioNotificationCommand, zer)
    eq1 = ctx.mk_eq(disableAudio, isAudioDisabled)
    and8 = ctx.mk_and(eq1, eq2)
    gt2 = ctx.mk_gt(disableAudio, zer)
    and9 = ctx.mk_and(systemOn, gt2)
    not6 = ctx.mk_not(and9)
    noAudioIfAudioDisabled = ctx.mk_or(not6, and8, 'no_audio_if_audio_disabled')
    audioLevel = inputs['Audio_Level']
    eq3 = ctx.mk_eq(audioNotificationCommand, audioLevel)
    eq4 = ctx.mk_eq(isAudioDisabled, zer)
    and10 = ctx.mk_and(eq3, eq4)
    latch1 = ctx.mk_latch('pre_Highest_Level_Alarm', ctx.mk_int8_type())
    ctx.set_latch_init_next(latch1, zer, highestLevelAlarm)
    geq2 = ctx.mk_geq(latch1, thr)
    eq3 = ctx.mk_eq(disableAudio, zer)
    and11 = ctx.mk_and(eq3, geq2)
    and12 = ctx.mk_and(and11, systemOn)
    not7 = ctx.mk_not(and12)
    alarmGteL3CausesAudioOutputEqAudioLevel = ctx.mk_or(not7, and10, 'alarm_gte_L3_causes_audio_output_eq_audio_level')
    return [alarmRange,
            emptyReservoirImpliesAlarmL4,
            volumeInfusedGreaterThanVTBIHighCausesGreaterL3Alarm,
            airInLineImpliesGreaterL3Alarm,
            occlusionImpliesGreaterL3Alarm,
            doorOpenImpliesGreaterL3Alarm,
            noAudioIfAudioDisabled,
            alarmGteL3CausesAudioOutputEqAudioLevel]


def main():
    startTime = time.time()
    enc = translate_iec61131('tests/openplc/GPCA_Alarm.xml')

    ctx = ip.Context()
    circ = enc.mk_instance(ctx, 'GPCA 1')
    circ.mk_circuit()

    prsTime = time.time() - startTime

    properties = mk_properties(ctx, circ.inputs, circ.outputs)
    bmc = ctx.mk_bmc()
    for prop in properties:
        bmc.add_target(ctx.mk_not(prop, 'prop_' + ctx.net2name[prop]))
    targetsToSolve = len(properties)
    depth = 0
    while depth < 10:
        print 'Current depth: %d' % depth
        print "There are still %d targets to solve" % targetsToSolve
        bmc.set_current_depth(depth)
        result = bmc.reach_targets()
        lastSolvedTargets = 0
        if result == EngineResult.REACHABLE:
            # trace = bmc.get_last_trace()
            # trace = trace.get_as_dataframe(ctx.net2name)
            # print trace
            for t in bmc.get_last_reached_targets():
                print ctx.net2name[t] + ' is UNSAFE'
                lastSolvedTargets += 1
            bmc.remove_last_reached_targets()
        elif result == EngineResult.UNREACHABLE:
            print 'No more properties can be solved at this depth'
        else:
            print 'An error occurred'
        targetsToSolve -= lastSolvedTargets
        if targetsToSolve == 0:
            break
        if lastSolvedTargets == 0:
            depth += 1
    endTime = time.time() - startTime
    print 'Parse time:', prsTime
    print 'Total time:', endTime


if __name__ == "__main__":
    main()
