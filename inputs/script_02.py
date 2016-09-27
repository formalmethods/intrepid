import intrepid as Int

def get_number_of_circuits():
    return 1;

def get_circuit(ctx, i):
    if i < 0 or i >= get_number_of_circuits():
        raise Int.IntrepidException('Circuit index out of bounds')
    circ = Int.mk_circuit(ctx, "ComplexAnd")
    tb = Int.mk_boolean_type(ctx)
    input1 = Int.mk_input(ctx, circ, "In1", tb)
    input2 = Int.mk_input(ctx, circ, "In2", tb)
    not_input1 = Int.mk_not(ctx, input1)
    not_input2 = Int.mk_not(ctx, input2)
    not_output = Int.mk_or(ctx, not_input1, not_input2)
    output = Int.mk_not(ctx, not_output)
    Int.mk_output(ctx, circ, "Out1", output)
    return circ

def get_name():
    return 'Complex And Script'


