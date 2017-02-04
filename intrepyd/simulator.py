import intrepyd as ip
import intrepyd.api
import intrepyd.trace

class Simulator(object):
    """
    A Simulator
    """
    def __init__(self, ctx):
        self.ctx = ctx
        self.simulator = ip.api.mk_simulator(self.ctx)

    def add_watch(self, net):
        """
        Tells the simulator about a net whose value will be reported in the simulated trace
        """
        ip.api.simulator_add_watch(self.ctx, self.simulator, net)

    def simulate(self, trace, depth):
        ip.api.simulator_simulate(self.simulator, trace.rawtrace, depth)
