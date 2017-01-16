"""
Utilities that simplify the use of the api
"""

import intrepid as ip
import imp
import collections
import pandas as pd

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
    Returns the counterexample as an ordered dictionary, whose keys
    are the nets, and the values are the list of values,
    one per each time step.

    Args:
        ctx: the intrepid context
        cex: the counterexample
        inputs: a dictionary name -> net for input nets
        watches: a dictionary name -> net for watched nets

    Returns:
        a dictionary name -> [value at step 0, ..., value at step n]
    """
    result = collections.OrderedDict()
    for name, net in inputs.iteritems():
        steps = counterexample_get_as_steps(ctx, cex, net)
        result[name] = steps
    for name, net in watches.iteritems():
        steps = counterexample_get_as_steps(ctx, cex, net)
        result[name] = steps
    return result

def counterexample_get_as_dataframe(cexDict):
    """
    Returns the counterexample as a pandas dataframe

          step0 ... stepn
    name0
    ...
    namem

    Args:
        cexDict: the counterexample as a dictionary

    Returns:
        the cex in a pandas dataframe
    """
    matrix = []
    indexes = []
    for name, values in cexDict.iteritems():
        indexes.append(name)
        matrix.append(values)
    df = pd.DataFrame(matrix, index=indexes)
    return df

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

def mk_at_most_one(ctx, nets):
    """
    Computes "at most one net is true"

    Args:
        ctx: the context to use
        nets: the nets to use
    """
    atMostOne = ip.mk_true(ctx)
    numNets = len(nets)
    for i in range(numNets - 1):
        for j in range(i + 1, numNets):
            conj = ip.mk_or(ctx, ip.mk_not(ctx, nets[i]), ip.mk_not(ctx, nets[j]))
            atMostOne = ip.mk_and(ctx, atMostOne, conj)
    return atMostOne

def mk_at_least_one(ctx, nets):
    """
    Computes "at least one net is true"

    Args:
        ctx: the context to use
        nets: the nets to use
    """
    atLeastOne = ip.mk_false(ctx)
    numNets = len(nets)
    for i in range(numNets):
        atLeastOne = ip.mk_or(ctx, atLeastOne, nets[i])
    return atLeastOne

def mk_exactly_one(ctx, nets, name):
    """
    Computes the pseudo-boolean constraint "exactly one is true".
    Uses the "commander variable" encoding described in
    "Efficient CNF Encoding for Selecting 1 from N Objects"
    by Will Klieber and Gihwon Kwon.

    Args:
        ctx: the context to use
        nets: the list of (Boolean) nets

    Returns:
        a net expressing the constraint "exactly one is true"
    """
    ip.push_namespace(ctx, name)
    result = mk_exactly_one_cv(ctx, nets)
    ip.pop_namespace(ctx)
    return result

def mk_exactly_one_cv(ctx, nets, k=3, depth=0, nGroup=0):
    numNets = len(nets)
    netsToProcess = []
    if numNets > k:
        # Recursively compute commander variables
        i = 0
        commanderVariables = []
        nGroup = 0
        while True:
            if i > numNets:
                break
            group = []
            for j in range(i, min(i + k, numNets)):
                group.append(nets[j])
            cv = mk_exactly_one_cv(ctx, group, k, depth + 1, nGroup)
            commanderVariables.append(cv)
            i += k
            nGroup += 1
        netsToProcess = commanderVariables
    else:
        netsToProcess = nets

    # Encoding happens here
    numNets = len(netsToProcess)
    cv = ip.mk_input(ctx, "cv_" + str(depth) + "_" + str(nGroup), ip.mk_boolean_type(ctx))
    exactlyOne = ip.mk_true(ctx)
    # Type 1 clauses
    atMostOneTrue = mk_at_most_one(ctx, netsToProcess)
    exactlyOne = ip.mk_and(ctx, exactlyOne, atMostOneTrue)
    # Type 2 clauses
    cvTrueThenAtLeastOneTrue = ip.mk_not(ctx, cv)
    for i in range(numNets):
        cvTrueThenAtLeastOneTrue = ip.mk_or(ctx, cvTrueThenAtLeastOneTrue, netsToProcess[i])
    exactlyOne = ip.mk_and(ctx, exactlyOne, cvTrueThenAtLeastOneTrue)
    # Type 3 clauses
    cvFalseThenAllFalse = ip.mk_true(ctx)
    for i in range(numNets):
        conj = ip.mk_or(ctx, cv, ip.mk_not(ctx, netsToProcess[i]))
        cvFalseThenAllFalse = ip.mk_and(ctx, cvFalseThenAllFalse, conj)
    exactlyOne = ip.mk_and(ctx, exactlyOne, cvFalseThenAllFalse)
    # Type 4 clauses
    if depth == 0:
        atMostOneTrue = mk_at_most_one(ctx, netsToProcess)
        atLeastOneTrue = mk_at_least_one(ctx, netsToProcess)
        exactlyOne = ip.mk_and(ctx, exactlyOne, atMostOneTrue)
        exactlyOne = ip.mk_and(ctx, exactlyOne, atLeastOneTrue)
    return exactlyOne