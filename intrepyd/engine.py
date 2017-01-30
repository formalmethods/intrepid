import intrepyd as ip
import intrepyd.api
import intrepyd.trace
from enum import Enum

class EngineResult(Enum):
    """
    Results from engine's reachability calls
    """
    REACHABLE = ip.api.INT_ENGINE_RESULT_REACHABLE
    UNREACHABLE = ip.api.INT_ENGINE_RESULT_UNREACHABLE
    UNKOWN = ip.api.INT_ENGINE_RESULT_UNKNOWN


class Engine(object):
    """
    Abstract intreface for an Engine
    """

    def __init__(self, ctx):
        self.ctx = ctx
        self.lastResult = EngineResult.UNKOWN

    def add_target(self, net):
        """
        Adds a target to be solved
        """
        raise NotImplementedError('Should have implemented this')
        
    def reach_targets(self):
        self.lastResult = self._api_result_to_engine_result(self._reach_targets_impl())
        return self.lastResult

    def get_last_reached_targets(self):
        """
        Returns the list of targets that has been reached last
        """
        if self.lastResult != EngineResult.REACHABLE:
            return
        lastReachedTargetsNo = self._get_last_reached_targets_number_impl()
        return (self._get_last_reached_target_impl(i) for i in range(lastReachedTargetsNo))

    def get_last_trace(self):
        """
        Returns the last produced trace
        """
        raise NotImplementedError('Should have implemented this')

    def remove_last_reached_targets(self):
        """
        Removes all the reached targets from the last call from the engine
        """
        raise NotImplementedError('Should have implemented this')

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
        return EngineResult.UNKOWN
    
    def _reach_targets_impl(self):
        """
        Executes a reachability search for the added targets
        """
        raise NotImplementedError('Should have implemented this')

    def _get_last_reached_targets_number_impl(self):
        raise NotImplementedError('Should have implemented this')

    def _get_last_reached_target_impl(self, target):
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

    def remove_last_reached_targets(self):
        if self.lastResult != EngineResult.REACHABLE:
            return
        ip.api.bmc_remove_last_reached_targets(self.ctx, self.bmc)

    def get_last_trace(self):
        if self.lastResult != EngineResult.REACHABLE:
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
        self.br = ip.api.mk_engine_br(self.ctx)

    def add_target(self, net):
        ip.api.br_add_target(self.ctx, self.br, net)

    def get_last_reached_targets(self):
        if self.lastResult != EngineResult.REACHABLE:
            return
        lastReachedTargetsNo = ip.api.bmc_last_reached_targets_number(self.bmc)
        return (ip.api.bmc_last_reached_target(self.bmc, i) for i in range(lastReachedTargetsNo))
       
    def get_last_reached_targets(self):
        if self.lastResult != EngineResult.REACHABLE:
            return
        lastReachedTargetsNo = ip.api.br_last_reached_targets_number(self.br)
        return (ip.api.br_last_reached_target(self.br, i) for i in range(lastReachedTargetsNo))

    def remove_last_reached_targets(self):
        if self.lastResult != EngineResult.REACHABLE:
            return
        ip.api.br_remove_last_reached_targets(self.ctx, self.br)

    def get_last_trace(self):
        if self.lastResult != EngineResult.REACHABLE:
            raise Exception('Cannot get a trace as last result was not REACHABLE')
        target = next(self.get_last_reached_targets())
        rawtrace = ip.api.br_get_trace(self.ctx, self.br, target)
        return ip.trace.Trace(self.ctx, rawtrace)

    def add_watch(self, net):
        ip.api.br_add_watch(self.ctx, self.br, net)

    def can_prove(self):
        return True

    def can_optimize(self):
        return False

    def _reach_targets_impl(self):
        return ip.api.br_reach_targets(self.br)
       
    def _reach_targets_impl(self):
        return ip.api.br_reach_targets(self.br)

    def _get_last_reached_targets_number_impl(self):
        return ip.api.br_last_reached_targets_number(self.br)

    def _get_last_reached_target_impl(self, target):
        return ip.api.br_last_reached_target(self.br, target)