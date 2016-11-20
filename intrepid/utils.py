"""
Utilities that simplify the use of the api
"""

import intrepid as ip

def counterexample_get_value_for_net(ctx, cex, net, depth):
    """
    Simplifies the retrieval of a value from the counterexample
    """
    size = ip.counterexample_prepare_value_for_net(ctx, cex, net, depth)
    value = ''
    for i in range(size):
        value += ip.value_at(i)
    return value

def counterexample_get_as_steps(ctx, cex, net):
    """
    Simplifies the retrieval of the set values per step for a net in a counterexample
    """
    maxDepth = ip.counterexample_get_max_depth(cex)
    values = []
    for depth in range(0, maxDepth + 1):
        values.append(counterexample_get_value_for_net(ctx, cex, net, depth))
    return values

def to_string(ctx, net):
    """
    Returns the given net as a string, as given from the underlying smt-solver
    """
    size = ip.prepare_value_for_net(ctx, net)
    value = ''
    for i in range(size):
        value += ip.value_at(i)
    return value