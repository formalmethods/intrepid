import intrepid as Int

def getInputs(circ):
    i = 0
    size = Int.get_inputs_size(circ);
    while i < size:
        yield Int.get_input(circ, i)
	i += 1

def getOutputs(circ):
    i = 0
    size = Int.get_outputs_size(circ);
    while i < size:
        yield Int.get_output(circ, i)
	i += 1
