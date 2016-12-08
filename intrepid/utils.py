"""
Utilities that simplify the use of the api
"""

import intrepid as ip
import imp
import collections

def counterexample_get_value_for_net(ctx, cex, net, depth):
    """
    Simplifies the retrieval of a value from the counterexample.
    """
    size = ip.counterexample_prepare_value_for_net(ctx, cex, net, depth)
    value = ''
    for i in range(size):
        value += ip.value_at(i)
    return value

def counterexample_get_as_steps(ctx, cex, net):
    """
    Simplifies the retrieval of the set values per step for a net in a counterexample.
    """
    maxDepth = ip.counterexample_get_max_depth(cex)
    values = []
    for depth in range(0, maxDepth + 1):
        values.append(counterexample_get_value_for_net(ctx, cex, net, depth))
    return values

def to_string(ctx, net):
    """
    Returns the given net as a string, as given from the underlying smt-solver.
    """
    size = ip.prepare_value_for_net(ctx, net)
    value = ''
    for i in range(size):
        value += ip.value_at(i)
    return value

def counterexample_get_as_dictionary(ctx, cex, inputs, watches):
    """
    Returns the counterexample as a dictionary, whose keys
    are the nets, and the values are the list of values,
    one per each time step.

    Parameters
    ----------
    ctx: the intrepid context
    cex: the counterexample
    inputs: a dictionary name -> net for input nets
    watches: a dictionary name -> net for watched nets
    """
    result = collections.OrderedDict()
    for name, net in inputs.iteritems():
        steps = counterexample_get_as_steps(ctx, cex, net)
        result[name] = steps
    for name, net in watches.iteritems():
        steps = counterexample_get_as_steps(ctx, cex, net)
        result[name] = steps
    return result

def bmc_reach_at_depth(ctx, bmc, depth):
    """
    Runs bmc to try to reach the targets, at the given depth

    Parameters
    ----------
    ctx: the intrepid context
    bmc: the bmc engine to use
    depth: the depth to use
    """
    ip.set_bmc_current_depth(bmc, depth)
    result = ip.bmc_reach_targets(bmc)
    reached_targets = []
    if ip.INT_ENGINE_RESULT_REACHABLE == result:
        for i in range(ip.bmc_last_reached_targets_number(bmc)):
            reached_targets.append(ip.bmc_last_reached_target(bmc, i))
    return reached_targets