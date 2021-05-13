Module intrepyd.circuit
=======================
This module implements a class Circuit used by translators

Classes
-------

`Circuit(context, name)`
:   Abstract interface for a circuit.

    ### Methods

    `mk_circuit(self, put_namespace=False)`
    :   Makes the circuit, including inputs and outputs.
        Optionally, it inserts a namespace.
        
        Args:
            put_namespace (bool=False): whether to set a namespace

    `mk_naked_circuit(self, inputs, namespace=False)`
    :   Makes the naked circuit, using the provided inputs.
        It fills out the dictionaries with the created nets.
        Optionally, it inserts a namespace.
        
        Args:
            inputs (Dict): the inputs to use
            namespace (bool=False): whether to set a namespace
        
        Returns:
            (Dict) the ordered dictionary of the outputs