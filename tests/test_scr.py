"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017
"""
import unittest
from intrepyd.engine import EngineResult
import intrepyd as ip
import intrepyd.scr
import traffic_light
import A7E_requirements
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

    def test_scr_02(self):
        ctx = ip.Context()
        myA7E = A7E_requirements.SimulinkCircuit(ctx, 'A7E_requirements')
        myA7E.mk_circuit()
        navigationUpdateMode = myA7E.nets['A7E_requirements/NU/Mode']
        weaponDeliveryMode = myA7E.nets['A7E_requirements/WD/Mode']
        aflyUpdate = myA7E.nets['A7E_requirements/NU/AflyUpd']
        boc = myA7E.nets['A7E_requirements/WD/BOC']
        sboc = myA7E.nets['A7E_requirements/WD/SBOC']
        navAfly = ctx.mk_neq(navigationUpdateMode, aflyUpdate)
        wpnBoc = ctx.mk_eq(weaponDeliveryMode, boc)
        wpnSboc = ctx.mk_eq(weaponDeliveryMode, sboc)
        target1 = ctx.mk_and(navAfly, wpnBoc)
        target2 = ctx.mk_and(navAfly, wpnSboc)
        target = ctx.mk_or(target1, target2)
        wdm = myA7E.nets['A7E_requirements/WD/Mode']
        num = myA7E.nets['A7E_requirements/NU/Mode']
        br = ctx.mk_backward_reach()
        br.add_target(target)
        result = br.reach_targets()
        self.assertEquals(EngineResult.UNREACHABLE, result)

if __name__ == '__main__':
    unittest.main()
