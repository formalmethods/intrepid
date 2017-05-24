"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017

This module implements the verification engines
"""

from enum import Enum
import intrepyd as ip

class EngineResult(Enum):
    """
    Results from engine's reachability calls
    """
    REACHABLE = ip.api.INT_ENGINE_RESULT_REACHABLE
    UNREACHABLE = ip.api.INT_ENGINE_RESULT_UNREACHABLE
    UNKNOWN = ip.api.INT_ENGINE_RESULT_UNKNOWN


class Engine(object):
    """
    Abstract intreface for an Engine
    """

    def __init__(self, ctx):
        self.ctx = ctx
        self.last_result = EngineResult.UNKNOWN

    def add_target(self, net):
        """
        Adds a target to be solved
        """
        raise NotImplementedError('Should have implemented this')

    def reach_targets(self):
        """
        Tries to reach any of the previously added targets
        """
        self.last_result = self._api_result_to_engine_result(self._reach_targets_impl())
        return self.last_result

    def get_last_reached_targets(self):
        """
        Returns the list of targets that has been reached last
        """
        if self.last_result != EngineResult.REACHABLE:
            return
        last_reached_targets_no = self._get_last_reached_targets_number_impl()
        return (self._get_last_reached_target_impl(i) for i in range(last_reached_targets_no))

    def get_last_trace(self):
        """
        Returns the last produced trace
        """
        raise NotImplementedError('Should have implemented this')

    def remove_last_reached_targets(self):
        """
        Removes all the reached targets from the last call from the engine
        """
        return self._remove_last_reached_targets_impl()

    def add_watch(self, net):
        """
        Track the value of net in future traces
        """
        raise NotImplementedError('Should have implemented this')

    def can_prove(self):
        """
        Tells if the engine can prove targets to be unreachable
        """
        raise NotImplementedError('Should have implemented this')

    def can_optimize(self):
        """
        Tells if the engine can prove targets to be unreachable
        """
        raise NotImplementedError('Should have implemented this')

    def _api_result_to_engine_result(self, result):
        if result == ip.api.INT_ENGINE_RESULT_REACHABLE:
            return EngineResult.REACHABLE
        elif result == ip.api.INT_ENGINE_RESULT_UNREACHABLE:
            return EngineResult.UNREACHABLE
        return EngineResult.UNKNOWN

    def _reach_targets_impl(self):
        """
        Engine-dependent reachability search for the added targets
        """
        raise NotImplementedError('Should have implemented this')

    def _get_last_reached_targets_number_impl(self):
        """
        Engine-dependent retrieval of last reached targets number
        """
        raise NotImplementedError('Should have implemented this')

    def _get_last_reached_target_impl(self, target):
        """
        Engine-dependent retrieval of last reached targets
        """
        raise NotImplementedError('Should have implemented this')

    def _remove_last_reached_targets_impl(self):
        """
        Engine-dependent removal of last reached targets
        """
        raise NotImplementedError('Should have implemented this')

class Bmc(Engine):
    """
    A Bounded Model Checking engine
    """

    def __init__(self, ctx):
        Engine.__init__(self, ctx)
        self.bmc = ip.api.mk_engine_bmc(self.ctx)

    def add_target(self, net):
        ip.api.bmc_add_target(self.ctx, self.bmc, net)

    def get_last_trace(self):
        if self.last_result != EngineResult.REACHABLE:
            raise Exception('Cannot get a trace as last result was not REACHABLE')
        target = next(self.get_last_reached_targets())
        cex = ip.api.bmc_get_trace(self.ctx, self.bmc, target)
        return ip.trace.Trace(self.ctx, cex)

    def add_watch(self, net):
        ip.api.bmc_add_watch(self.ctx, self.bmc, net)

    def set_current_depth(self, depth):
        """
        Sets the current depth to use for BMC
        """
        ip.api.set_bmc_current_depth(self.bmc, depth)

    def can_prove(self):
        return False

    def can_optimize(self):
        return False

    def _reach_targets_impl(self):
        return ip.api.bmc_reach_targets(self.bmc)

    def _get_last_reached_targets_number_impl(self):
        return ip.api.bmc_last_reached_targets_number(self.bmc)

    def _get_last_reached_target_impl(self, target):
        return ip.api.bmc_last_reached_target(self.bmc, target)

    def _remove_last_reached_targets_impl(self):
        return ip.api.bmc_remove_last_reached_targets(self.bmc)

class OptimizingBmc(Bmc):
    """
    An Optimizing Bounded Model Checking engine
    """

    def __init__(self, ctx):
        Bmc.__init__(self, ctx)
        ip.api.set_bmc_optimize(self.bmc)

    def can_optimize(self):
        return True


class BackwardReach(Engine):
    """
    A Backward Reachability Model Checking algorithm
    """

    def __init__(self, ctx):
        Engine.__init__(self, ctx)
        self.breach = ip.api.mk_engine_br(self.ctx)

    def add_target(self, net):
        ip.api.br_add_target(self.ctx, self.breach, net)

    def get_last_trace(self):
        if self.last_result != EngineResult.REACHABLE:
            raise Exception('Cannot get a trace as last result was not REACHABLE')
        target = next(self.get_last_reached_targets())
        rawtrace = ip.api.br_get_trace(self.ctx, self.breach, target)
        return ip.trace.Trace(self.ctx, rawtrace)

    def add_watch(self, net):
        ip.api.br_add_watch(self.ctx, self.breach, net)

    def can_prove(self):
        return True

    def can_optimize(self):
        return False

    def _reach_targets_impl(self):
        return ip.api.br_reach_targets(self.breach)

    def _get_last_reached_targets_number_impl(self):
        return ip.api.br_last_reached_targets_number(self.breach)

    def _get_last_reached_target_impl(self, target):
        return ip.api.br_last_reached_target(self.breach, target)

    def _remove_last_reached_targets_impl(self):
        return ip.api.br_remove_last_reached_targets(self.breach)
