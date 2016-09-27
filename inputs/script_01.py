import intrepid as Int

def get_number_of_circuits():
    return 1;

def get_circuit(ctx, i):
    if i < 0 or i >= get_number_of_circuits():
        raise Int.IntrepidException('Circuit index out of bounds')
    circ = Int.mk_circuit(ctx, "SimpleAnd")
    tb = Int.mk_boolean_type(ctx)
    input1 = Int.mk_input(ctx, circ, "In1", tb)
    input2 = Int.mk_input(ctx, circ, "In2", tb)
    output = Int.mk_and(ctx, input1, input2)
    Int.mk_output(ctx, circ, "Out1", output)
    return circ

def get_name():
    return 'Simple And Script'


