import unittest
import intrepid as ip
import intrepid.scr

class TestScr(unittest.TestCase):

    def setUp(self):
        self.ctx = ip.mk_ctx()

    def tearDown(self):
        ip.del_ctx(self.ctx)

    def isReachableAtDepth(self, target, depth):
        bmc = ip.mk_engine_bmc(self.ctx)
        ip.bmc_add_target(self.ctx, bmc, target)
        ip.set_bmc_current_depth(bmc, depth)
        result = ip.bmc_reach_targets(bmc)
        return ip.INT_ENGINE_RESULT_REACHABLE == result

    def makeModeGreen(self):
        return ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))

    def makeModeYellow(self):
        return ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))

    def makeModeRed(self):
        return ip.mk_number(self.ctx, '2', ip.mk_int8_type(self.ctx))

    def makeModeOff(self):
        return ip.mk_number(self.ctx, '3', ip.mk_int8_type(self.ctx))

    def makeModes(self):
        # This order must match the one defined in traffic_light.ord
        return [self.makeModeGreen(),\
                self.makeModeYellow(),\
                self.makeModeRed(),\
                self.makeModeOff()]

    def test_traffic_light(self):
        """
        Just outputs the parser table for manual inspection
        """

        modes = self.makeModes()

        pastInputs = [ip.mk_input(self.ctx, 'PastOnGreen', ip.mk_boolean_type(self.ctx)),\
                      ip.mk_input(self.ctx, 'PastOnYellow', ip.mk_boolean_type(self.ctx)),\
                      ip.mk_input(self.ctx, 'PastOnRed', ip.mk_boolean_type(self.ctx)),\
                      ip.mk_input(self.ctx, 'PastOnTurnOff', ip.mk_boolean_type(self.ctx)),\
                      ip.mk_input(self.ctx, 'PastDayTime', ip.mk_boolean_type(self.ctx))]

        inputs = [ip.mk_input(self.ctx, 'OnGreen', ip.mk_boolean_type(self.ctx)),\
                  ip.mk_input(self.ctx, 'OnYellow', ip.mk_boolean_type(self.ctx)),\
                  ip.mk_input(self.ctx, 'OnRed', ip.mk_boolean_type(self.ctx)),\
                  ip.mk_input(self.ctx, 'OnTurnOff', ip.mk_boolean_type(self.ctx)),\
                  ip.mk_input(self.ctx, 'DayTime', ip.mk_boolean_type(self.ctx))]

        pastMode = ip.mk_input(self.ctx, 'PastMode', ip.mk_int8_type(self.ctx))
        currentMode = ip.scr.mk_scr(self.ctx, 'test/files/traffic_light',
                                    inputs, pastInputs, modes, pastMode) 

        # Uncomment the next line to display table on screen
        # print ip.utils.to_string(self.ctx, currentMode)

    def test_traffic_light_01(self):
        """
        past(Daylight) = true
        past(Mode) = Green          _
        past(OnYellow) = false       | Raising edge
        OnYellow = true             _| on OnYellow
        expect: Mode = Yellow
        """

        modes = self.makeModes()

        pastInputs = [ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx),\
                      ip.mk_true(self.ctx)]

        inputs = [ip.mk_false(self.ctx),\
                  ip.mk_true(self.ctx),\
                  ip.mk_false(self.ctx),\
                  ip.mk_false(self.ctx),\
                  ip.mk_false(self.ctx)]

        pastMode = self.makeModeGreen()
        currentMode = ip.scr.mk_scr(self.ctx, 'test/files/traffic_light',
                                    inputs, pastInputs, modes, pastMode) 

        target = ip.mk_eq(self.ctx, currentMode, self.makeModeYellow())
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

        pastInputs = [ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx),\
                      ip.mk_true(self.ctx)]

        inputs = [ip.mk_false(self.ctx),\
                  ip.mk_false(self.ctx),\
                  ip.mk_true(self.ctx),\
                  ip.mk_false(self.ctx),\
                  ip.mk_false(self.ctx)]

        pastMode = self.makeModeYellow()
        currentMode = ip.scr.mk_scr(self.ctx, 'test/files/traffic_light',
                                    inputs, pastInputs, modes, pastMode) 

        target = ip.mk_eq(self.ctx, currentMode, self.makeModeRed())
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

        pastInputs = [ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx),\
                      ip.mk_true(self.ctx)]

        inputs = [ip.mk_true(self.ctx),\
                  ip.mk_false(self.ctx),\
                  ip.mk_false(self.ctx),\
                  ip.mk_false(self.ctx),\
                  ip.mk_false(self.ctx)]

        pastMode = self.makeModeRed()
        currentMode = ip.scr.mk_scr(self.ctx, 'test/files/traffic_light',
                                    inputs, pastInputs, modes, pastMode) 

        target = ip.mk_eq(self.ctx, currentMode, self.makeModeGreen())
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

        pastInputs = [ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx)]

        inputs = [ip.mk_false(self.ctx),\
                  ip.mk_false(self.ctx),\
                  ip.mk_false(self.ctx),\
                  ip.mk_true(self.ctx),\
                  ip.mk_false(self.ctx)]

        pastMode = self.makeModeYellow()
        currentMode = ip.scr.mk_scr(self.ctx, 'test/files/traffic_light',
                                    inputs, pastInputs, modes, pastMode) 

        target = ip.mk_eq(self.ctx, currentMode, self.makeModeOff())
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

        pastInputs = [ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx)]

        inputs = [ip.mk_false(self.ctx),\
                  ip.mk_true(self.ctx),\
                  ip.mk_false(self.ctx),\
                  ip.mk_false(self.ctx),\
                  ip.mk_false(self.ctx)]

        pastMode = self.makeModeOff()
        currentMode = ip.scr.mk_scr(self.ctx, 'test/files/traffic_light',
                                    inputs, pastInputs, modes, pastMode) 

        target = ip.mk_eq(self.ctx, currentMode, self.makeModeYellow())
        self.assertTrue(self.isReachableAtDepth(target, 0))

if __name__ == '__main__':
    unittest.main()
