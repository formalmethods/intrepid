import intrepyd as ip
import unittest

# class TestExactlyOne(unittest.TestCase):

#     def setUp(self):
#         self.ctx = ip.mk_ctx()

#     def tearDown(self):
#         ip.del_ctx(self.ctx)

#     def createAndRunNets(self, n):
#         nets = []
#         for i in range(n):
#             nets.append(ip.mk_input(self.ctx, "n" + str(i), ip.mk_boolean_type(self.ctx)))
#         eo = ip.utils.mk_exactly_one(self.ctx, nets, "eo")
#         bmc = ip.mk_engine_bmc(self.ctx)
#         ip.bmc_add_target(self.ctx, bmc, eo)
#         reachedNets = ip.utils.bmc_reach_at_depth(self.ctx, bmc, 0)
#         self.assertEqual(1, len(reachedNets))

#     def test_exactly_one_01(self):
#         # Corner cases
#         self.createAndRunNets(1)
#         self.createAndRunNets(2)
#         self.createAndRunNets(3)
#         self.createAndRunNets(4)
#         # Some normal cases
#         self.createAndRunNets(10)
#         self.createAndRunNets(11)
#         self.createAndRunNets(12)
#         # A random prime
#         self.createAndRunNets(43)

#     def test_exactly_one_02(self):
#         nets = []
#         i1 = ip.mk_input(self.ctx, "i1", ip.mk_boolean_type(self.ctx))
#         i2 = ip.mk_input(self.ctx, "i2", ip.mk_boolean_type(self.ctx))
#         i3 = ip.mk_input(self.ctx, "i3", ip.mk_boolean_type(self.ctx))
#         nets.append(ip.mk_or(self.ctx, i1, i2))
#         nets.append(ip.mk_or(self.ctx, i1, i3))
#         nets.append(ip.mk_or(self.ctx, i2, i3))
#         eo = ip.utils.mk_exactly_one(self.ctx, nets, "eo")
#         bmc = ip.mk_engine_bmc(self.ctx)
#         ip.bmc_add_target(self.ctx, bmc, eo)
#         reachedNets = ip.utils.bmc_reach_at_depth(self.ctx, bmc, 0)
#         self.assertEqual(0, len(reachedNets))