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

def to_string(ctx, net):
    """
    Returns the given net as a string, as given from the underlying smt-solver
    """
    size = ip.prepare_value_for_net(ctx, net)
    value = ''
    for i in range(size):
        value += ip.value_at(i)
    return value