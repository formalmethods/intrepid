"""
Utilities that simplify the use of the api
"""

import intrepid as Int

def counterexample_get_value_for_net(ctx, cex, net, depth):
    """
    Simplifies the retrieval of the counterexample
    """
    size = Int.counterexample_prepare_value_for_net(ctx, cex, net, depth)
    value = ''
    for i in range(size):
        value += Int.value_at(i)
    return value