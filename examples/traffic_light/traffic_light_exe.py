import intrepyd as ip
from intrepyd.engine import EngineResult

# Importing translated module
import traffic_light

def doMain():
    ctx = ip.Context()
    myTrafficLight = traffic_light.SimulinkCircuit(ctx, 'MyTrafficLight')
    myTrafficLight.mk_circuit()
    lightOut = myTrafficLight.outputs['traffic_light/out']
    targetGreen = ctx.mk_eq(lightOut, myTrafficLight.nets['traffic_light/Green'], 'Green')
    targetYellow = ctx.mk_eq(lightOut, myTrafficLight.nets['traffic_light/Yellow'], 'Yellow')
    targetRed = ctx.mk_eq(lightOut, myTrafficLight.nets['traffic_light/Red'], 'Red')
    targetOff = ctx.mk_eq(lightOut, myTrafficLight.nets['traffic_light/Off'], 'Off')
    bmc = ctx.mk_bmc()
    bmc.add_target(targetGreen)
    bmc.add_target(targetYellow)
    bmc.add_target(targetRed)
    bmc.add_target(targetOff)
    for depth in range(4):
        bmc.set_current_depth(depth)
        res = bmc.reach_targets()
        if res == EngineResult.REACHABLE:
            reachedTargets = bmc.get_last_reached_targets()
            print 'Targets reached at depth', depth, ':'
            for target in reachedTargets:
                print '-->', ctx.net2name[target], '<--'
            trace = bmc.get_last_trace()
            traceDf = trace.get_as_dataframe(ctx.net2name)
            print traceDf
            # ip.plots.plot_counterexample_dictionary(cexDict)
        else:
            print 'No target reacheable at depth:', depth
        print

if __name__ == "__main__":
    doMain()
