"""
The Simulator
"""

from intrepyd.api import mk_simulator, simulator_add_watch, simulator_simulate

class Simulator:
    """
    Simulates the circuit in the context by using the input values provided
    in the trace. If a value is not present at a time step, the default
    value for the type is taken
    """
    def __init__(self, ctx):
        self.ctx = ctx
        self.simulator = mk_simulator(self.ctx)

    def add_watch(self, net):
        """
        Tells the simulator about a net whose value will be reported in the simulated trace
        """
        simulator_add_watch(self.ctx, self.simulator, net)

    def simulate(self, trace, depth):
        """
        Executes a simulation using the values in trace, up to the specified depth
        """
        simulator_simulate(self.simulator, trace.rawtrace, depth)
