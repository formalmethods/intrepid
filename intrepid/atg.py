import intrepid as ip
import intrepid.utils
import pandas as pd

def compute_mcdc(ctx, class_, decisions, maxDepth):
    """
    Computes MC/DC tests in form of a table.

    Args:
        ctx: the intrepid context to use
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
    instA = class_(ctx, 'InstA')
    instB = class_(ctx, 'InstB')
    instA.mk_circuit(True)
    instB.mk_circuit(True)

    # Creates test objectives
    decision2testObjectives = { decision :\
            compute_mcdc_targets(ctx, instA, instB, decision, conditions)\
            for decision, conditions in decisions.iteritems() }

    # Compute MC/DC cexes: this is the computationally
    # expensive part that calls model checking routines
    decision2cexes = solve_mcdc_targets(ctx, decision2testObjectives, maxDepth)

    # Compute MC/DC tables from cexes
    decision2table = compute_mcdc_tables(ctx, instA, instB, decision2cexes)

    # Compute pretty tables
    decision2prettyTable = compute_pretty_tables(decision2table)

    return decision2prettyTable

def compute_mcdc_targets(ctx, instA, instB, decision, conditions):
    """
    Computes the MC/DC reachability target for the
    two copies of the circuit.

    Args:
        ctx (Int_ctx): the intrepid context to use
        instA (circuit.Circuit): an instance of the circuit
        instB (circuit.Circuit): an instance of the circuit
        decision (str): the name of a decision
        conditions ([str, ...]): the list of names of the conditions

    Returns:
        ([Int_net, Int_net, ...]) the list of targets, whose reachability
                    implies the existence of an MC/DC test
    """
    decisionA = instA.nets[decision]
    decisionB = instB.nets[decision]
    decisionA_diff_decisionB = ip.mk_neq(ctx, decisionA, decisionB)

    conditionA_neq_conditionB = []
    conditionsA = []
    conditionsB = []
    for condition in conditions:
        cA = instA.nets[condition]
        conditionsA.append(cA)
        cB = instB.nets[condition]
        conditionsB.append(cB)
        conditionA_neq_conditionB.append(ip.mk_neq(ctx, cA, cB))

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
        not_cA = ip.mk_not(ctx, cA)
        decisionA_not_cA = ip.mk_substitute(ctx, decisionA, not_cA, cA)
        conj3 = ip.mk_neq(ctx, decisionA_not_cA, decisionA)
        # decisionB[not(cB)/cB] != decisionB
        not_cB = ip.mk_not(ctx, cB)
        decisionB_not_cB = ip.mk_substitute(ctx, decisionB, not_cB, cB)
        conj4 = ip.mk_neq(ctx, decisionB_not_cB, decisionB)
        # Creates final conjunction
        tmp1 = ip.mk_and(ctx, conj1, conj2)
        tmp2 = ip.mk_and(ctx, tmp1, conj3)
        target = ip.mk_and(ctx, tmp2, conj4)
        targets.append(target)

    return targets

def solve_mcdc_targets(ctx, decision2testObjectives, maxDepth):
    """
    Solves the MC/DC targets, maximizing the number of solved
    test objectives per each call.
    """
    bmc = ip.mk_engine_bmc(ctx)

    testObjectives2decision = {}
    decision2cexes = {}
    totalTargets = 0
    for decision, tos in decision2testObjectives.iteritems():
        decision2cexes[decision] = []
        for to in tos:
            testObjectives2decision[to] = decision
            ip.bmc_add_target(ctx, bmc, to)
            totalTargets += 1

    ip.set_bmc_optimize(bmc)

    done = False
    depth = 0
    totalReached = 0
    while not done:
        ip.set_bmc_current_depth(bmc, depth)
        result = ip.bmc_reach_targets(bmc)
        if result != ip.INT_ENGINE_RESULT_REACHABLE:
            if depth == maxDepth:
                done = True
            depth += 1
            continue
        reached = ip.bmc_last_reached_targets_number(bmc)
        if reached > 0:
            totalReached += reached
            cex = None
            for i in range(reached):
                reachedTarget = ip.bmc_last_reached_target(bmc, i)
                if i == 0:
                    cex = ip.bmc_get_counterexample(ctx, bmc, reachedTarget)
                decision = testObjectives2decision[reachedTarget]
                decision2cexes[decision].append(cex)
            ip.bmc_remove_last_reached_targets(bmc)
        if totalReached == totalTargets:
            done = True

    return decision2cexes

def compute_mcdc_tables(ctx, instA, instB, decision2cexes):
    """
    Computes MC/DC tables out of counterexamples.
    """
    decision2table = {}
    for decision, cexes in decision2cexes.iteritems():
        decision2table[decision] = []
        for cex in cexes:
            test1 = ip.utils.counterexample_get_as_dictionary(ctx, cex, instA.inputs, { decision : instA.nets[decision] })
            test2 = ip.utils.counterexample_get_as_dictionary(ctx, cex, instB.inputs, { decision : instB.nets[decision] })
            decision2table[decision].append(test1)
            decision2table[decision].append(test2)
    return decision2table

def compute_pretty_tables(decision2table):
    """
    Postprocess raw MC/DC tables to get something presentation ready.
    """
    decision2prettyTable = {}
    for decision, table in decision2table.iteritems():
        prettyTable = []
        header = []
        for inputValue in table:
            for input, value in inputValue.iteritems():
               header.append(input)
            break
        prettyTable.append(header)
        for inputValue in table:
            row = []
            for _, value in inputValue.iteritems():
                row.append(value[0])
            prettyTable.append(row)
        decision2prettyTable[decision] = prettyTable
    return decision2prettyTable

def get_tables_as_dataframe(decision2table):
    result = {}
    for decision, table in decision2table.iteritems():
        df = pd.DataFrame(table[1:], columns=table[0])
        df = df.drop_duplicates()
        result[decision] = df
    return result
