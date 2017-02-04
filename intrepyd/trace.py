import intrepyd as ip
import intrepyd.api
import pandas as pd

class Trace(object):
    """
    A trace generated from an Engine, or manually built for use in simulation
    """
    def __init__(self, ctx, rawtrace=None):
        self.ctx = ctx
        self.rawtrace = None
        if rawtrace == None:
            rawtrace = ip.api.mk_trace(self.ctx)
        self.rawtrace = rawtrace

    @staticmethod
    def get_numeric_value(self, value):
        """
        Coverts a string value (including true, false) into a corresponding float or integer.
        """
        if '.' in value:
            return float(value)
        elif value == '?':
            return '?'
        elif value == 'true':
            return 1
        elif value == 'false':
            return 0
        return int(value)

    def get_value(self, net, depth):
        """
        Retrieval of a value from the trace for a net at a depth
        """
        size = ip.api.trace_prepare_value_for_net(self.ctx, self.rawtrace, net, depth)
        value = ''
        for i in range(size):
            value += ip.api.value_at(i)
        return value

    def set_value(self, net, depth, value):
        ip.api.trace_set_value(self.ctx, self.rawtrace, net, depth, value)

    def get_as_net_dictionary(self, net2name=None):
        """
        Return the trace as a dictionary
        
        net -> [value@0, value@1, ...]
        """
        watchedNets = [ip.api.trace_get_watched_net(self.rawtrace, i)\
                       for i in range(ip.api.trace_get_watched_nets_number(self.rawtrace))]
        if net2name == None:
            return {net : list(self._get_as_steps(net)) for net in watchedNets}
        else:
            return {net2name[net] : list(self._get_as_steps(net)) for net in watchedNets}

    def get_as_depth_dictionary(self):
        """
        Return the trace as a dictionary
        
        depth -> [valuenet1@depth, valuenet2@depth, ...]
        """
        return {depth : list(self._get_values_at_depth(net, depth))\
                for depth in ip.api.trace_get_max_depth(self.trace)}

    def get_as_dataframe(self, net2name):
        """
        Return the trace as a pandas dataframe

                  0       1       2    ...
        name1  value@0 value@1 value@2 ...
        name2  value@0 value@1 value@2 ...
        ...
        """
        matrix = []
        indexes = []
        for net, values in self.get_as_net_dictionary().iteritems():
            indexes.append(net2name[net])
            matrix.append(values)
        return pd.DataFrame(matrix, index=indexes)

    def _get_as_steps(self, net):
        """
        Simplifies the retrieval of the set values per step for a net in a trace.
        """
        maxDepth = ip.api.trace_get_max_depth(self.rawtrace)
        return (self.get_value(net, depth) for depth in range(0, maxDepth + 1))

    def _get_values_at_depth(self, depth):
        """
        Simplifies the retrieval of the set values per step for a net in a trace.
        """
        watchedNets = [ip.api.trace_get_watched_net(self.rawtrace, i)\
                       for i in range(ip.api.trace_get_watched_nets_number(self.rawtrace))]
        return (self._get_value_for_net(net, depth) for net in watchedNets)
