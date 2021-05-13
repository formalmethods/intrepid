Module intrepyd.atg.mcdc
========================
This module implements a toolbox for Automated Test Generation

Functions
---------

    
`compute_hash(test)`
:   Computes a unique hash for a test

    
`compute_mcdc(context, class_, decisions, max_depth)`
:   Computes MC/DC tests in form of a table.
    
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

    
`compute_mcdc_tables(context, inst_a, inst_b, decision2traces, trace2condition, decisions)`
:   Computes MC/DC tables out of counterexamples.

    
`compute_mcdc_targets(context, inst_a, inst_b, decision, conditions)`
:   Computes the MC/DC reachability target for the
    two copies of the circuit.
    
    Args:
        context: the intrepyd context to use
        inst_a: an instance of the circuit
        inst_b: an instance of the circuit
        decision: the name of a decision
        conditions: the list of names of the conditions
    
    Returns:
        a map from targets to conditions for which target is an independence pair

    
`compute_pretty_tables(decision2table)`
:   Postprocess raw MC/DC tables to get something presentation ready.

    
`get_tables_as_dataframe(decision2table)`
:   Postprocess table to turn into a dataframe

    
`solve_mcdc_targets(context, decision2testobjectives, decisions, max_depth)`
:   Solves the MC/DC targets, maximizing the number of solved
    test objectives per each call.