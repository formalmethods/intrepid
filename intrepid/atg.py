import intrepid as ip

def compute_mcdc(class_, decisions):
    """
    Computes MC/DC tests in form of a table.

    Args:
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
    ctx = ip.mk_ctx()

    # Fetches and duplicates the circuit
    instA = class_(ctx, 'InstA')
    instB = class_(ctx, 'InstB')
    instA.mk_circuit(True)
    instB.mk_circuit(True)

    # Creates test objectives
    testObjectives = { decision :\
            [compute_mcdc_targets(ctx, instA, instB, decision, conditions)\
             for decision, conditions in decisions] }

    # Compute MC/DC tables: this is the computationally
    # expensive part that calls model checking routines
    tables = { decision :\
            [compute_mcdc_tables(ctx, instA, instB, decision, testObjs)\
             for decision, testObjs in testObjectives] }

    ip.del_ctx()
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
    toA = instA.nets[testObjective]
    toB = instB.nets[testObjective]
    toA_diff_toB = ip.mk_neq(ctx, toA, toB)

    tcA_neq_tcB = []
    testConditionsA = []
    for testCondition in testConditions:
        tcA = instA.nets[testCondition]
        testConditionsA.append(tcA)
        tcB = instB.nets[testCondition]
        testConditionsB.append(tcB)
        tcA_neq_tcB.append(ip.mk_neq(ctx, tcA, tcB))

    targets = []
    for i in range(len(testConditions)):
        # Building test objective for the i-th condition
        tcA = testConditionsA[i]
        tcB = testConditionsB[i]
        # i-th condition must differ in A and B
        conj1 = tcA_neq_tcB[i]
        # test objective must differ in A and B
        conj2 = toA_diff_toB
        # toA[not tcA/tcA] != toA
        not_tcA = ip.mk_not(ctx, tcA)
        toA_not_tcA = ip.mk_substitution(ctx, not_tcA, tcA, toA)
        conj3 = ip.mk_neq(ctx, toA_not_tcA, toA)
        # toB[not tcB/tcB] != toB
        not_tcB = ip.mk_not(ctx, tcB)
        toB_not_tcB = ip.mk_substitution(ctx, not_tcB, tcB, toB)
        conj4 = ip.mk_neq(ctx, toB_not_tcB, toB)
        # Creates final conjunction
        tmp1 = ip.mk_and(ctx, conj1, conj2)
        tmp2 = ip.mk_and(ctx, tmp1, conj3)
        target = ip.mk_and(ctx, tmp2, conj4)
        targets.append(target)

    return targets
