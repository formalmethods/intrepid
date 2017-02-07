import intrepyd as ip
from intrepyd.engine import EngineResult
import pandas as pd
import collections as cl

def compute_mcdc(context, class_, decisions, maxDepth):
    """
    Computes MC/DC tests in form of a table.

    Args:
        context: the intrepyd context to use
        class_ (class): a python class that defines the circuit
        decisions (Dictionary): each key of the dictionary is the
                    name of a decision, and the values are the
                    corresponding conditions

                { netName           : [netName, ...] }
                  ^                    ^
                  the decision         the list of conditions

    Returns:
        (Dictionary) the MC/DC tables, one per each decision
    """

    # Fetches and duplicates the circuit
    instA = class_(context, 'InstA')
    instB = class_(context, 'InstB')
    instA.mk_circuit(True)
    instB.mk_circuit(True)

    # Flattens inputs and outputs into nets, for simplicity
    instA.nets.update(instA.inputs)
    instB.nets.update(instB.inputs)

    # Creates test objectives
    decision2testObjectives = { decision :\
            compute_mcdc_targets(context, instA, instB, decision, conditions)\
            for decision, conditions in decisions.iteritems() }

    # Compute MC/DC traces: this is the computationally
    # expensive part that calls model checking routines
    decision2traces, decision2unreachable = solve_mcdc_targets(context, decision2testObjectives, maxDepth)

    # Compute MC/DC tables from traces
    decision2table = compute_mcdc_tables(context, instA, instB, decision2traces, decisions)

    # Compute pretty tables
    decision2prettyTable = compute_pretty_tables(decision2table)

    return decision2prettyTable

def compute_mcdc_targets(context, instA, instB, decision, conditions):
    """
    Computes the MC/DC reachability target for the
    two copies of the circuit.

    Args:
        context: the intrepid context to use
        instA: an instance of the circuit
        instB: an instance of the circuit
        decision: the name of a decision
        conditions: the list of names of the conditions

    Returns:
        the list of targets, whose reachability implies the existence of an MC/DC test
    """
    decisionA = instA.nets[decision]
    decisionB = instB.nets[decision]
    decisionA_diff_decisionB = context.mk_neq(decisionA, decisionB)

    conditionA_neq_conditionB = []
    conditionsA = []
    conditionsB = []
    for condition in conditions:
        cA = instA.nets[condition]
        conditionsA.append(cA)
        cB = instB.nets[condition]
        conditionsB.append(cB)
        conditionA_neq_conditionB.append(context.mk_neq(cA, cB))

    targets = []
    for i in range(len(conditions)):
        # Building test objective for the i-th condition
        cA = conditionsA[i]
        cB = conditionsB[i]
        # i-th condition must differ in A and B
        conj1 = conditionA_neq_conditionB[i]
        # test objective must differ in A and B
        conj2 = decisionA_diff_decisionB
        # decisionA[not(cA)/cA] != decisionA
        not_cA = context.mk_not(cA)
        decisionA_not_cA = context.mk_substitute(decisionA, not_cA, cA)
        conj3 = context.mk_neq(decisionA_not_cA, decisionA)
        # decisionB[not(cB)/cB] != decisionB
        not_cB = context.mk_not(cB)
        decisionB_not_cB = context.mk_substitute(decisionB, not_cB, cB)
        conj4 = context.mk_neq(decisionB_not_cB, decisionB)
        # Creates final conjunction
        tmp1 = context.mk_and(conj1, conj2)
        tmp2 = context.mk_and(tmp1, conj3)
        target = context.mk_and(tmp2, conj4)
        targets.append(target)

    return targets

def solve_mcdc_targets(context, decision2testObjectives, maxDepth):
    """
    Solves the MC/DC targets, maximizing the number of solved
    test objectives per each call.
    """
    # Bmc engine will be used to compute counterexamples
    bmc = context.mk_optimizing_bmc()

    testObjectives2decision = {}
    decision2traces = {}
    decision2unreachable = {}
    targets = []
    for decision, tos in decision2testObjectives.iteritems():
        decision2traces[decision] = []
        decision2unreachable[decision] = []
        for to in tos:
            testObjectives2decision[to] = decision
            targets.append(to)

    totalTargets = len(targets)

    # Compute unreachable targets first
    totalUnreached = 0
    totalReached = 0
    for target in targets:
        br = context.mk_backward_reach()
        br.add_target(target)
        result = br.reach_targets()
        if result == EngineResult.UNREACHABLE:
            decision = testObjectives2decision[target]
            decision2unreachable[decision].append(target)
            totalUnreached += 1
        elif result == EngineResult.REACHABLE:
            bmc.add_target(target)
            totalReached += 1

    print 'There are', totalTargets, 'test objectives:'
    print '-', totalUnreached, 'unreachable test objectives'
    print '-', totalReached, 'reachable test objectives'

    if totalUnreached == totalTargets:
        return decision2traces, decision2unreachable

    # Compute counterexamples for reachable targets
    done = False
    depth = 0
    bmcTotalReached = 0
    while not done:
        bmc.set_current_depth(depth)
        result = bmc.reach_targets()
        if result != EngineResult.REACHABLE:
            if depth == maxDepth:
                done = True
            depth += 1
            continue
        reached = bmc.get_last_reached_targets()
        trace = bmc.get_last_trace()
        for reachedTarget in reached:
            decision = testObjectives2decision[reachedTarget]
            decision2traces[decision].append(trace)
            bmcTotalReached += 1
        bmc.remove_last_reached_targets()
        if bmcTotalReached == totalReached:
            done = True

    totalUndecided = totalReached - bmcTotalReached
    if totalUndecided != 0:
        print 'There are', totalUndecided, 'undecided test objectives within depth', maxDepth

    return decision2traces, decision2unreachable

def compute_mcdc_tables(context, instA, instB, decision2traces, decisions):
    """
    Computes MC/DC tables out of counterexamples.
    """
    decision2table = {}
    for decision, traces in decision2traces.iteritems():
        instAtestNets = instA.inputs.values() + [instA.nets[decision]]
        instBtestNets = instB.inputs.values() + [instB.nets[decision]]
        header = [cond for cond in decisions[decision]]
        header.append(decision)
        decision2table[decision] = [header]
        for trace in traces:
            simulator = context.mk_simulator()
            simulator.add_watch(instA.nets[decision])
            simulator.add_watch(instB.nets[decision])
            simulator.simulate(trace, trace.get_max_depth())
            fullTestA = trace.get_as_net_dictionary()
            fullTestB = trace.get_as_net_dictionary()
            testA = [v[0] for k, v in fullTestA.iteritems() if k in instAtestNets]
            testB = [v[0] for k, v in fullTestB.iteritems() if k in instBtestNets]
            decision2table[decision].append((testA, testB))
    return decision2table

def compute_pretty_tables(decision2table):
    """
    Postprocess raw MC/DC tables to get something presentation ready.
    """
    decision2prettyTable = {}
    first = True
    for decision, table in decision2table.iteritems():
        prettyTable = []
        for row in table:
            if first:
                first = False
                prettyTable.append(row)
            else:
                prettyTable.append(row[0])
                prettyTable.append(row[1])
        decision2prettyTable[decision] = prettyTable
    return decision2prettyTable

def get_tables_as_dataframe(decision2table):
    result = {}
    for decision, table in decision2table.iteritems():
        if len(table) == 1:
            continue
        df = pd.DataFrame(table[1:], columns=table[0])
        df = df.drop_duplicates()
        result[decision] = df
    return result
