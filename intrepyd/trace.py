"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017

This module implements the class for traces
"""

import pandas as pd
import intrepyd as ip

class Trace(object):
    """
    A trace generated from an Engine, or manually built for use in simulation
    """
    def __init__(self, ctx, rawtrace=None):
        self.ctx = ctx
        self.rawtrace = None
        if rawtrace is None:
            rawtrace = ip.api.mk_trace(self.ctx)
        self.rawtrace = rawtrace

    @staticmethod
    def get_numeric_value(value):
        """
        Coverts a string value (including true, false) into a corresponding float or integer.
        """
        if '.' in value:
            return float(value)
        elif value == '?':
            return '?'
        elif value == 'T':
            return 1
        elif value == 'F':
            return 0
        return int(value)

    def get_max_depth(self):
        """
        Returns the max depth of the trace
        """
        return ip.api.trace_get_max_depth(self.rawtrace)

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
        """
        Sets a value for a net at a certain depth
        """
        if value == 'true':
            value = 'T'
        elif value == 'false':
            value = 'F'
        ip.api.trace_set_value(self.ctx, self.rawtrace, net, depth, value)

    def get_as_net_dictionary(self, net2name=None):
        """
        Return the trace as a dictionary

        net -> [value@0, value@1, ...]
        """
        watched_nets = [ip.api.trace_get_watched_net(self.rawtrace, i)\
                       for i in range(ip.api.trace_get_watched_nets_number(self.rawtrace))]
        if net2name is None:
            return {net : list(self._get_as_steps(net)) for net in watched_nets}
        else:
            return {net2name[net] : list(self._get_as_steps(net)) for net in watched_nets}

    def get_as_depth_dictionary(self):
        """
        Return the trace as a dictionary

        depth -> [valuenet1@depth, valuenet2@depth, ...]
        """
        return {depth : list(self._get_values_at_depth(depth))\
                for depth in range(ip.api.trace_get_max_depth(self.rawtrace))}

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

    def set_from_dataframe(self, dataframe, inputname2net):
        """
        Return a trace from a pandas dataframe. Only input values
        are considered in filling up the trace
        """
        max_depth = 0
        row = 0
        for name in dataframe.index:
            if name in inputname2net:
                net = inputname2net[name]
                depth = 0
                for value in dataframe.values[row]:
                    self.set_value(net, depth, str(value))
                    if depth > max_depth:
                        max_depth = depth
                    depth += 1
            row += 1
        return max_depth

    def _get_as_steps(self, net):
        """
        Simplifies the retrieval of the set values per step for a net in a trace.
        """
        max_depth = ip.api.trace_get_max_depth(self.rawtrace)
        return (self.get_value(net, depth) for depth in range(0, max_depth + 1))

    def _get_values_at_depth(self, depth):
        """
        Simplifies the retrieval of the set values per step for a net in a trace.
        """
        watched_nets = [ip.api.trace_get_watched_net(self.rawtrace, i)\
                       for i in range(ip.api.trace_get_watched_nets_number(self.rawtrace))]
        return (self.get_value(net, depth) for net in watched_nets)
