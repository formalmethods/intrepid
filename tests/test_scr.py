import intrepyd as ip
import intrepyd.scr
import intrepyd.api
import unittest

class TestScr(unittest.TestCase):

    def setUp(self):
        self.ctx = ip.api.mk_ctx()

    # def tearDown(self):
    #     ip.api.del_ctx(self.ctx)

    def isReachableAtDepth(self, target, depth):
        bmc = ip.api.mk_engine_bmc(self.ctx)
        ip.api.bmc_add_target(self.ctx, bmc, target)
        ip.api.set_bmc_current_depth(bmc, depth)
        result = ip.api.bmc_reach_targets(bmc)
        return ip.api.INT_ENGINE_RESULT_REACHABLE == result

    def makeModeOff(self):
        return ip.api.mk_number(self.ctx, '0', ip.api.mk_int8_type(self.ctx))

    def makeModeGreen(self):
        return ip.api.mk_number(self.ctx, '1', ip.api.mk_int8_type(self.ctx))

    def makeModeYellow(self):
        return ip.api.mk_number(self.ctx, '2', ip.api.mk_int8_type(self.ctx))

    def makeModeRed(self):
        return ip.api.mk_number(self.ctx, '3', ip.api.mk_int8_type(self.ctx))

    def makeModes(self):
        # This order must match the one defined in traffic_light.ord
        return [self.makeModeOff(),\
                self.makeModeGreen(),\
                self.makeModeYellow(),\
                self.makeModeRed()]

    def test_traffic_light_00(self):
        """
        Just outputs the parser table for manual inspection
        """

        modes = self.makeModes()

        pastInputs = [ip.api.mk_input(self.ctx, 'PastOnTurnOff', ip.api.mk_boolean_type(self.ctx)),\
                      ip.api.mk_input(self.ctx, 'PastOnGreen', ip.api.mk_boolean_type(self.ctx)),\
                      ip.api.mk_input(self.ctx, 'PastOnYellow', ip.api.mk_boolean_type(self.ctx)),\
                      ip.api.mk_input(self.ctx, 'PastOnRed', ip.api.mk_boolean_type(self.ctx)),\
                      ip.api.mk_input(self.ctx, 'PastDayTime', ip.api.mk_boolean_type(self.ctx))]

        inputs = [ip.api.mk_input(self.ctx, 'OnTurnOff', ip.api.mk_boolean_type(self.ctx)),\
                  ip.api.mk_input(self.ctx, 'OnGreen', ip.api.mk_boolean_type(self.ctx)),\
                  ip.api.mk_input(self.ctx, 'OnYellow', ip.api.mk_boolean_type(self.ctx)),\
                  ip.api.mk_input(self.ctx, 'OnRed', ip.api.mk_boolean_type(self.ctx)),\
                  ip.api.mk_input(self.ctx, 'DayTime', ip.api.mk_boolean_type(self.ctx))]

        pastMode = ip.api.mk_input(self.ctx, 'PastMode', ip.api.mk_int8_type(self.ctx))
        currentMode = ip.scr.mk_scr(self.ctx, 'tests/files/traffic_light',
                                    inputs, pastInputs, modes, pastMode) 
        ip.api.apitrace_dump_to_file('trace.cpp')

    def test_traffic_light_01(self):
        """
        past(Daylight) = true
        past(Mode) = Green          _
        past(OnYellow) = false       | Raising edge
        OnYellow = true             _| on OnYellow
        expect: Mode = Yellow
        """

        modes = self.makeModes()

        pastInputs = [ip.api.mk_false(self.ctx),\
                      ip.api.mk_false(self.ctx),\
                      ip.api.mk_false(self.ctx),\
                      ip.api.mk_false(self.ctx),\
                      ip.api.mk_true(self.ctx)]

        inputs = [ip.api.mk_false(self.ctx),\
                  ip.api.mk_false(self.ctx),\
                  ip.api.mk_true(self.ctx),\
                  ip.api.mk_false(self.ctx),\
                  ip.api.mk_false(self.ctx)]

        pastMode = self.makeModeGreen()
        currentMode = ip.scr.mk_scr(self.ctx, 'tests/files/traffic_light',
                                    inputs, pastInputs, modes, pastMode) 

        target = ip.api.mk_eq(self.ctx, currentMode, self.makeModeYellow())
        self.assertTrue(self.isReachableAtDepth(target, 0))


    def test_traffic_light_02(self):
        """
        past(Daylight) = true
        past(Mode) = Yellow         _
        past(OnRed) = false          | Raising edge
        OnRed = true                _| on OnRed
        expect: Mode = Red
        """

        modes = self.makeModes()

        pastInputs = [ip.api.mk_false(self.ctx),\
                      ip.api.mk_false(self.ctx),\
                      ip.api.mk_false(self.ctx),\
                      ip.api.mk_false(self.ctx),\
                      ip.api.mk_true(self.ctx)]

        inputs = [ip.api.mk_false(self.ctx),\
                  ip.api.mk_false(self.ctx),\
                  ip.api.mk_false(self.ctx),\
                  ip.api.mk_true(self.ctx),\
                  ip.api.mk_false(self.ctx)]

        pastMode = self.makeModeYellow()
        currentMode = ip.scr.mk_scr(self.ctx, 'tests/files/traffic_light',
                                    inputs, pastInputs, modes, pastMode) 

        target = ip.api.mk_eq(self.ctx, currentMode, self.makeModeRed())
        self.assertTrue(self.isReachableAtDepth(target, 0))


    def test_traffic_light_03(self):
        """
        past(Daylight) = true
        past(Mode) = Red            _
        past(OnGreen) = false        | Raising edge
        OnRed = true                _| on OnGreen
        expect: Mode = Green
        """

        modes = self.makeModes()

        pastInputs = [ip.api.mk_false(self.ctx),\
                      ip.api.mk_false(self.ctx),\
                      ip.api.mk_false(self.ctx),\
                      ip.api.mk_false(self.ctx),\
                      ip.api.mk_true(self.ctx)]

        inputs = [ip.api.mk_false(self.ctx),\
                  ip.api.mk_true(self.ctx),\
                  ip.api.mk_false(self.ctx),\
                  ip.api.mk_false(self.ctx),\
                  ip.api.mk_false(self.ctx)]

        pastMode = self.makeModeRed()
        currentMode = ip.scr.mk_scr(self.ctx, 'tests/files/traffic_light',
                                    inputs, pastInputs, modes, pastMode) 

        target = ip.api.mk_eq(self.ctx, currentMode, self.makeModeGreen())
        self.assertTrue(self.isReachableAtDepth(target, 0))


    def test_traffic_light_04(self):
        """
        past(Daylight) = false
        past(Mode) = Yellow         _
        past(OnTurnOff) = false      | Raising edge
        OnTurnOff = true            _| on OnTurnOff
        expect: Mode = TurnOff
        """

        modes = self.makeModes()

        pastInputs = [ip.api.mk_false(self.ctx),\
                      ip.api.mk_false(self.ctx),\
                      ip.api.mk_false(self.ctx),\
                      ip.api.mk_false(self.ctx),\
                      ip.api.mk_false(self.ctx)]

        inputs = [ip.api.mk_true(self.ctx),\
                  ip.api.mk_false(self.ctx),\
                  ip.api.mk_false(self.ctx),\
                  ip.api.mk_false(self.ctx),\
                  ip.api.mk_false(self.ctx)]

        pastMode = self.makeModeYellow()
        currentMode = ip.scr.mk_scr(self.ctx, 'tests/files/traffic_light',
                                    inputs, pastInputs, modes, pastMode) 

        target = ip.api.mk_eq(self.ctx, currentMode, self.makeModeOff())
        self.assertTrue(self.isReachableAtDepth(target, 0))


    def test_traffic_light_05(self):
        """
        past(Daylight) = false
        past(Mode) = Off            _
        past(OnYellow) = false       | Raising edge
        OnYellow = true             _| on OnYellow
        expect: Mode = Yellow
        """

        modes = self.makeModes()

        pastInputs = [ip.api.mk_false(self.ctx),\
                      ip.api.mk_false(self.ctx),\
                      ip.api.mk_false(self.ctx),\
                      ip.api.mk_false(self.ctx),\
                      ip.api.mk_false(self.ctx)]

        inputs = [ip.api.mk_false(self.ctx),\
                  ip.api.mk_false(self.ctx),\
                  ip.api.mk_true(self.ctx),\
                  ip.api.mk_false(self.ctx),\
                  ip.api.mk_false(self.ctx)]

        pastMode = self.makeModeOff()
        currentMode = ip.scr.mk_scr(self.ctx, 'tests/files/traffic_light',
                                    inputs, pastInputs, modes, pastMode) 

        target = ip.api.mk_eq(self.ctx, currentMode, self.makeModeYellow())
        self.assertTrue(self.isReachableAtDepth(target, 0))

if __name__ == '__main__':
    unittest.main()
