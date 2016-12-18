import intrepid as ip
import collections

class Circuit(object):
    """
    Abstract interface for a circuit.
    """

    def __init__(self, ctx, name):
        self.ctx = ctx
        self.name = name
        self.inputs = collections.OrderedDict()
        self.outputs = collections.OrderedDict()
        self.nets = collections.OrderedDict()
        self.proof_objectives = collections.OrderedDict()

    def mk_circuit(self, namespace=False):
        """
        Makes the circuit, including inputs and outputs.
        Optionally, it inserts a namespace.

        Args:
            namespace (bool=False): whether to set a namespace
        """
        if namespace:
            ip.push_namespace(self.ctx, self.name)
        self._mk_inputs()
        self.outputs = self._mk_naked_circuit_impl(self.inputs)
        self._mk_outputs()
        if namespace:
            ip.pop_namespace(self.ctx)

    def mk_naked_circuit(self, inputs, namespace=False):
        """
        Makes the naked circuit, using the provided inputs.
        It fills out the dictionaries with the created nets.
        Optionally, it inserts a namespace.

        Args:
            inputs (OrderedDict): the inputs to use
            namespace (bool=False): whether to set a namespace

        Returns:
            (OrderedDict) the ordered dictionary of the outputs
        """
        if namespace:
            ip.push_namespace(self.ctx, self.name)
        outputs = self._mk_circuit_naked_impl(self, inputs)
        if namespace:
            ip.pop_namespace(self.ctx)
        return outputs

    def _mk_outputs(self):
        """
        Makes the outputs contained in the already filled-out
        self.outputs.
        """
        for i, (name, net) in enumerate(self.outputs.iteritems()):
            ip.mk_output(self.ctx, net)

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
            inputs (OrderedDict): the inputs to use

        Returns:
            (OrderedDict) the outputs
        """
        raise NotImplementedError('Should have implemented this')
