"""
This module implements a class Circuit used by translators
"""

class Circuit:
    """
    Abstract interface for a circuit.
    """

    def __init__(self, context, name):
        self.context = context
        self.name = name
        self.nets = {}
        self.inputs = {}
        self.outputs = {}
        self.targets = {}

    def mk_circuit(self, put_namespace=False):
        """
        Makes the circuit, including inputs and outputs.
        Optionally, it inserts a namespace.

        Args:
            put_namespace (bool=False): whether to set a namespace
        """
        if put_namespace:
            self.context.push_namespace(self.name)
        self._mk_inputs()
        self.outputs = self._mk_naked_circuit_impl(self.inputs)
        self._mk_outputs()
        if put_namespace:
            self.context.pop_namespace()

    def mk_naked_circuit(self, inputs, namespace=False):
        """
        Makes the naked circuit, using the provided inputs.
        It fills out the dictionaries with the created nets.
        Optionally, it inserts a namespace.

        Args:
            inputs (Dict): the inputs to use
            namespace (bool=False): whether to set a namespace

        Returns:
            (Dict) the ordered dictionary of the outputs
        """
        if namespace:
            self.context.push_namespace(self.name)
        outputs = self._mk_naked_circuit_impl(inputs)
        if namespace:
            self.context.pop_namespace()
        return outputs

    def _mk_outputs(self):
        """
        Makes the outputs contained in the already filled-out
        self.outputs.
        """
        for _, (_, net) in enumerate(self.outputs.items()):
            self.context.mk_output(net)

    def _mk_inputs(self):
        """
        Makes the inputs nets, and it fills the self.inputs
        dictionary with the inputs nets.
        """
        raise NotImplementedError('Should have implemented this')

    def _mk_naked_circuit_impl(self, inputs):
        """
        Makes the naked circuit.

        Args:
            inputs (Dict): the inputs to use

        Returns:
            (Dict) the outputs
        """
        raise NotImplementedError('Should have implemented this')
