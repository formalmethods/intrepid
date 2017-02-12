import unittest
from intrepyd.engine import EngineResult
import intrepyd as ip
import intrepyd.scr
import traffic_light
import os

class TestScr(unittest.TestCase):
    
    def test_scr_01(self):
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
        bmc.set_current_depth(4)
        res = bmc.reach_targets()
        self.assertEquals(res, EngineResult.REACHABLE)
        reachedTargets = list(bmc.get_last_reached_targets())
        self.assertEquals(1, len(reachedTargets))

if __name__ == '__main__':
    unittest.main()
