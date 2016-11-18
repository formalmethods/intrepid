import unittest
import intrepid as ip
import intrepid.scr

class TestScr(unittest.TestCase):

    def setUp(self):
        self.ctx = ip.mk_ctx()

    def tearDown(self):
        ip.del_ctx(self.ctx)

    def makeModeGreen(self, ctx):
        return ip.mk_number(self.ctx, '0', ip.mk_int8_type(ctx))

    def makeModeYellow(self, ctx):
        return ip.mk_number(self.ctx, '1', ip.mk_int8_type(ctx))

    def makeModeRed(self, ctx):
        return ip.mk_number(self.ctx, '2', ip.mk_int8_type(ctx))

    def makeModeOff(self, ctx):
        return ip.mk_number(self.ctx, '3', ip.mk_int8_type(ctx))


    def makeModes(self, ctx):
        return [self.makeModeOff(ctx), self.makeModeGreen(ctx),\
                self.makeModeYellow(ctx), self.makeModeRed(ctx)]

    def test_traffic_light(self):

        inputs = [ip.mk_false(self.ctx),\
                  ip.mk_true(self.ctx),\
                  ip.mk_false(self.ctx),\
                  ip.mk_false(self.ctx),\
                  ip.mk_true(self.ctx)]

        pastInputs = [ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx),\
                      ip.mk_false(self.ctx),\
                      ip.mk_true(self.ctx)]

        modes = self.makeModes(self.ctx)
        pastMode = self.makeModeGreen(self.ctx)

        # past(Mode) = Green          _
        # past(OnYellow) = false       | Raising edge
        # OnYellow = true             _| on OnYellow
        # expect: Mode = Yellow

        currentMode = ip.scr.mk_scr(self.ctx, 'test/files/traffic_light',
                                    inputs, pastInputs, modes, pastMode) 

        target = ip.mk_eq(self.ctx, currentMode, self.makeModeYellow(self.ctx))
        #target = ip.mk_eq(self.ctx, currentMode, self.makeModeGreen(self.ctx))
        #target = ip.mk_eq(self.ctx, currentMode, self.makeModeRed(self.ctx))
        #target = ip.mk_eq(self.ctx, currentMode, self.makeModeOff(self.ctx))
        bmc = ip.mk_engine_bmc(self.ctx)
        ip.bmc_add_target(self.ctx, bmc, target)
        ip.set_bmc_current_depth(bmc, 0)
        result = ip.bmc_reach_targets(bmc)
        self.assertEquals(ip.INT_ENGINE_RESULT_REACHABLE, result)


if __name__ == '__main__':
    unittest.main()
