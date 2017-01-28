import intrepyd as ip
import collections
import pandas as pd

class Trace(collections.OrderedDict):
    """
    A trace generated from an Engine, or manually built for use in simulation
    """
    def __init__(self, ctx, rawtrace=None):
        self.ctx = ctx
        if rawtrace == None:
            # Creates an empty trace, dictionary is left empty
            rawtrace = ip.mk_trace(self.ctx)
        else:
            watchedNets = [ip.trace_get_watched_net(self.ctx, trace, i)\
                           for i in range(ip.trace_get_watched_nets_number(self.ctx, trace))]
            for net in watchedNets:
                self[net] = self._get_as_steps(ctx, trace, net)
        self.rawtrace = rawtrace

    def __setitem__(self, key, values):
        depth = 0
        for value in values:
            ip.trace_set_value(self.ctx, self.rawtrace, str(value), depth)
            depth += 1
        self.__setitem__(key, value)

    def get_as_dataframe(self, name2net):
        """
        Return the trace as a pretty-printed pandas dataframe
        """
        matrix = []
        indexes = []
        for net, values in iteritems():
            indexes.append(name2net[net])
            matrix.append(values)
        return pd.DataFrame(matrix, index=indexes)

    def _get_value_for_net(self, trace, net, depth):
        """
        Simplifies the retrieval of a value from the trace.
        """
        size = ip.trace_prepare_value_for_net(self.ctx, trace, net, depth)
        value = ''
        for i in range(size):
            value += ip.value_at(i)
        return value

    def _get_as_steps(self, trace, net):
        """
        Simplifies the retrieval of the set values per step for a net in a trace.
        """
        maxDepth = ip.trace_get_max_depth(trace)
        return (self._get_numeric_value(value)\
                for depth in range(0, maxDepth + 1)\
                    for value in self._get_value_for_net(self.ctx, trace, net, depth))

    def _get_numeric_value(self, value):
        """
        Coverts a string value (including true, false) into a corresponding float or integer.
        """
        if '.' in value:
            return float(value)
        elif value == 'true':
            return 1
        elif value == 'false':
            return 0
        return int(value)