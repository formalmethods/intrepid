Module intrepyd.atg.circuit
===========================
Implementation of Circuit class for ATG

Classes
-------

`Circuit(ctx, name)`
:   Abstract interface for a circuit to use for ATG

    ### Descendants

    * intrepyd.tests.test_atg.CircAnd
    * intrepyd.tests.test_atg.CircFmics2021

    ### Methods

    `inputs(self)`
    :   Returns the dictionary of inputs

    `mk_circuit(self)`
    :   Makes the circuit

    `nets(self)`
    :   Returns the dictionary of nets