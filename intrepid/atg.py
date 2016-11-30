import intrepid as ip

def compute_mcdc(class_, testDescription):
    """
    Computes MC/DC tests in form of a table

    Args:
        class_ (class): a python class that defines the circuit
        testDescription (Dictionary): a description of the test, each
                                      key of the dictionary is the name
                                      of a test objective, and the values
                                      are the corresponding conditions that
                                      are to be used to compute the tests

                { netName           : [netName, ...] }
                  ^                    ^
                  a test objective     a list of test conditions
    """
    ctx = ip.mk_ctx()

    inst_a = class_(ctx, 'InstA')
    inst_b = class_(ctx, 'InstB')

    inst_a.mk_circuit(True)
    inst_b.mk_circuit(True)



    ip.del_ctx()
