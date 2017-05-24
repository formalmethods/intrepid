"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017

This module implements creation of pseudo-boolean functions for nets
"""

import intrepyd as ip
import intrepyd.api

def mk_at_most_one(ctx, nets):
    """
    Computes "at most one net is true"

    Args:
        ctx: the context to use
        nets: the nets to use
    """
    atMostOne = ip.api.mk_true(ctx)
    numNets = len(nets)
    for i in range(numNets - 1):
        for j in range(i + 1, numNets):
            conj = ip.api.mk_or(ctx, ip.api.mk_not(ctx, nets[i]), ip.api.mk_not(ctx, nets[j]))
            atMostOne = ip.api.mk_and(ctx, atMostOne, conj)
    return atMostOne

def mk_at_least_one(ctx, nets):
    """
    Computes "at least one net is true"

    Args:
        ctx: the context to use
        nets: the nets to use
    """
    atLeastOne = ip.api.mk_false(ctx)
    numNets = len(nets)
    for i in range(numNets):
        atLeastOne = ip.api.mk_or(ctx, atLeastOne, nets[i])
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
    ip.api.push_namespace(ctx, name)
    result = _mk_exactly_one_cv(ctx, nets)
    ip.api.pop_namespace(ctx)
    return result

def _mk_exactly_one_cv(ctx, nets, k=3, depth=0, nGroup=0):
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
            cv = _mk_exactly_one_cv(ctx, group, k, depth + 1, nGroup)
            commanderVariables.append(cv)
            i += k
            nGroup += 1
        netsToProcess = commanderVariables
    else:
        netsToProcess = nets

    # Encoding happens here
    numNets = len(netsToProcess)
    cv = ip.api.mk_input(ctx, "__cv_" + str(depth) + "_" + str(nGroup), ip.api.mk_boolean_type(ctx))
    exactlyOne = ip.api.mk_true(ctx)
    # Type 1 clauses
    atMostOneTrue = mk_at_most_one(ctx, netsToProcess)
    exactlyOne = ip.api.mk_and(ctx, exactlyOne, atMostOneTrue)
    # Type 2 clauses
    cvTrueThenAtLeastOneTrue = ip.api.mk_not(ctx, cv)
    for i in range(numNets):
        cvTrueThenAtLeastOneTrue = ip.api.mk_or(ctx, cvTrueThenAtLeastOneTrue, netsToProcess[i])
    exactlyOne = ip.api.mk_and(ctx, exactlyOne, cvTrueThenAtLeastOneTrue)
    # Type 3 clauses
    cvFalseThenAllFalse = ip.api.mk_true(ctx)
    for i in range(numNets):
        conj = ip.api.mk_or(ctx, cv, ip.api.mk_not(ctx, netsToProcess[i]))
        cvFalseThenAllFalse = ip.api.mk_and(ctx, cvFalseThenAllFalse, conj)
    exactlyOne = ip.api.mk_and(ctx, exactlyOne, cvFalseThenAllFalse)
    # Type 4 clauses
    if depth == 0:
        atMostOneTrue = mk_at_most_one(ctx, netsToProcess)
        atLeastOneTrue = mk_at_least_one(ctx, netsToProcess)
        exactlyOne = ip.api.mk_and(ctx, exactlyOne, atMostOneTrue)
        exactlyOne = ip.api.mk_and(ctx, exactlyOne, atLeastOneTrue)
    return exactlyOne