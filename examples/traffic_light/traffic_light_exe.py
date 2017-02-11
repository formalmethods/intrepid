import intrepyd as ip

# Importing translated module
import traffic_light

def doMain():
    ctx = ip.Context()
    myTrafficLight = traffic_light.SimulinkCircuit(ctx, 'MyTrafficLight')
    myTrafficLight.mk_circuit()
    lightOut = myTrafficLight.outputs['traffic_light/out']
    targetGreen = ip.mk_eq(ctx, lightOut, myTrafficLight.nets['traffic_light/Green'])
    targetYellow = ip.mk_eq(ctx, lightOut, myTrafficLight.nets['traffic_light/Yellow'])
    targetRed = ctx.mk_eq(lightOut, myTrafficLight.nets['traffic_light/Red'])
    targetOff = ctx.mk_eq(lightOut, myTrafficLight.nets['traffic_light/Off'])
    bmc = ctx.mk_bmc()
    bmc.add_target(targetGreen)
    bmc.add_target(targetYellow)
    bmc.add_target(targetRed)
    bmc.add_target(targetOff)
    for depth in range(4):
        bmc.set_current_depth(depth)
        reachedTargets = bmc.reach_targets()
        if len(reachedTargets) > 0:
            print 'Targets reached at depth', depth, ':', len(reachedTargets)
            trace = bmc.get_trace(reachedTargets[0])
            traceDf = trace.get_as_dataframe(ctx.nets2name)
            print traceDf
            # ip.plots.plot_counterexample_dictionary(cexDict)
        else:
            print 'No target reacheable at depth:', depth
        print

if __name__ == "__main__":
    doMain()
