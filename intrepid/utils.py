"""
Utilities that makes the C API more pythonic
"""

import api

def get_inputs(circ):
    """
    Generator for the list of inputs in the circuit

    get_inputs(circ) -> [Int_net, Int_net, ...]

    Parameters
    ----------
    circ: Int_circuit
    """
    i = 0
    size = api.get_inputs_size(circ)
    while i < size:
        yield api.get_input(circ, i)
        i += 1

def get_outputs(circ):
    """
    Generator for the list of outputs in the circuit

    get_outputs(circ) -> [Int_net, Int_net, ...]

    Parameters
    ----------
    circ: Int_circuit
    """
    i = 0
    size = api.get_outputs_size(circ)
    while i < size:
        yield api.get_output(circ, i)
        i += 1
