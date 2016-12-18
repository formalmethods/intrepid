import intrepid as ip
import intrepid.utils

def compute_mcdc(ctx, class_, decisions):
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

    # Compute MC/DC tables: this is the computationally
    # expensive part that calls model checking routines
    tables = solve_mcdc_targets(ctx, instA, instB, decision2testObjectives)

    return tables

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

def solve_mcdc_targets(ctx, instA, instB, decision2testObjectives):
    bmc = ip.mk_engine_bmc(ctx)

    testObjectives2decision = {}
    totalTargets = 0
    for decision, tos in decision2testObjectives.iteritems():
        for to in tos:
            testObjectives2decision[to] = decision
            ip.bmc_add_target(ctx, bmc, to)
            totalTargets += 1

    ip.set_bmc_optimize(bmc)

    allInputs = {}
    for name, net in instA.inputs.iteritems():
        allInputs['instA/' + name] = net
    for name, net in instB.inputs.iteritems():
        allInputs['instB/' + name] = net
    done = False
    depth = 0
    totalReached = 0
    # Hardcoded
    maxDepth = 10
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
            cex = ip.bmc_get_counterexample(ctx, bmc, testObjs[0])
            cexDict = ip.utils.counterexample_get_as_dictionary(ctx, cex, allInputs, {})
        if totalReached == totalTargets:
            done = True

    return cexDict
