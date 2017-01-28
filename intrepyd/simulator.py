import intrepyd as ip
import intrepyd.trace

class Simulator(object):
    """
    A Simulator
    """
    def __init__(self, ctx):
        self.ctx = ctx
        self.simulator = ip.mk_engine_simulator(self.ctx)

    def add_watch(self, net):
        """
        Tells the simulator about a net whose value will be reported in the simulated trace
        """
        ip.simulator_add_watch(self.ctx, self.simulator, net)

    def simulate(self, trace):
        ip.simulator_simulate(self.ctx, self.simulator, trace.rawtrace)