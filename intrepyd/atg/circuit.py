"""
Implementation of Circuit class for ATG
"""
class Circuit:
    """
    Abstract interface for a circuit to use for ATG
    """
    def __init__(self, ctx, name):
        self._ctx = ctx
        self._name = name

    def mk_circuit(self):
        """
        Makes the circuit
        """
        self._ctx.push_namespace(self._name)
        self._mk_circuit_impl()
        self._ctx.pop_namespace()

    def _mk_circuit_impl(self):
        raise NotImplementedError('Should have implemented this')

    def inputs(self):
        """
        Returns the dictionary of inputs
        """
        raise NotImplementedError('Should have implemented this')

    def nets(self):
        """
        Returns the dictionary of nets
        """
        raise NotImplementedError('Should have implemented this')
