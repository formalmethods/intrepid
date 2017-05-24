"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017

This module implements the simulator
"""

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
        """
        Executes a simulation using the values in trace, up to the specified depth
        """
        ip.api.simulator_simulate(self.simulator, trace.rawtrace, depth)
