import intrepid as ip
import intrepid.scr
import intrepid.utils

inputs = {}
proof_objectives = {}
outputs = []

def mk_naked_circuit(ctx, n1, n2, n3, n4, n5):
    # OnOff -> n1
    # OnGreen -> n2
    # OnYellow -> n3
    # OnRed -> n4
    # Daytime -> n5
    n6 = ip.mk_latch(ctx, 'traffic_light/Past(OnOff)', ip.mk_boolean_type(ctx))
    n7 = ip.mk_latch(ctx, 'traffic_light/Past(OnRed)', ip.mk_boolean_type(ctx))
    n8 = ip.mk_latch(ctx, 'traffic_light/Past(OnYellow)', ip.mk_boolean_type(ctx))
    n9 = ip.mk_latch(ctx, 'traffic_light/Past(OnGreen)', ip.mk_boolean_type(ctx))
    n10 = ip.mk_latch(ctx, 'traffic_light/Past(Daytime)', ip.mk_boolean_type(ctx))
    n11 = ip.mk_latch(ctx, 'traffic_light/Init', ip.mk_boolean_type(ctx))
    n12 = ip.mk_latch(ctx, 'traffic_light/Past(Mode)', ip.mk_int8_type(ctx))
    # traffic_light/false
    n13 = ip.mk_false(ctx)
    # traffic_light/Off
    n14 = ip.mk_number(ctx, '0', ip.mk_int8_type(ctx))
    # Bus Creator
    n15 = [n1, n2, n3, n4, n5]
    # Bus Creator1
    n16 = [n6, n9, n8, n7, n10]
    # traffic_light/Green
    n17 = ip.mk_number(ctx, '1', ip.mk_int8_type(ctx))
    # traffic_light/Yellow
    n18 = ip.mk_number(ctx, '2', ip.mk_int8_type(ctx))
    # traffic_light/Red
    n19 = ip.mk_number(ctx, '3', ip.mk_int8_type(ctx))
    # Bus Creator2
    n20 = [n14, n17, n18, n19]
    n21_1 = ip.scr.mk_scr(ctx, 'traffic_light', n15, n16, n20, n12)
    # traffic_light/Mode
    n22 = ip.mk_ite(ctx, n11, n14, n21_1)
    in6 = ip.mk_true(ctx)
    ip.set_latch_init_next(ctx, n6, in6, n1)
    in7 = ip.mk_true(ctx)
    ip.set_latch_init_next(ctx, n7, in7, n4)
    in8 = ip.mk_true(ctx)
    ip.set_latch_init_next(ctx, n8, in8, n3)
    in9 = ip.mk_true(ctx)
    ip.set_latch_init_next(ctx, n9, in9, n2)
    in10 = ip.mk_true(ctx)
    ip.set_latch_init_next(ctx, n10, in10, n5)
    in11 = ip.mk_true(ctx)
    ip.set_latch_init_next(ctx, n11, in11, n13)
    in12 = ip.mk_number(ctx, '1', ip.mk_int8_type(ctx))
    ip.set_latch_init_next(ctx, n12, in12, n22)
    # n22 -> out
    return n22

def mk_circuit(ctx):
    # traffic_light/OnOff -> n1
    n1 = ip.mk_input(ctx, 'OnOff', ip.mk_boolean_type(ctx))
    inputs['OnOff'] = n1
    # traffic_light/OnGreen -> n2
    n2 = ip.mk_input(ctx, 'OnGreen', ip.mk_boolean_type(ctx))
    inputs['OnGreen'] = n2
    # traffic_light/OnYellow -> n3
    n3 = ip.mk_input(ctx, 'OnYellow', ip.mk_boolean_type(ctx))
    inputs['OnYellow'] = n3
    # traffic_light/OnRed -> n4
    n4 = ip.mk_input(ctx, 'OnRed', ip.mk_boolean_type(ctx))
    inputs['OnRed'] = n4
    # traffic_light/Daytime -> n5
    n5 = ip.mk_input(ctx, 'Daytime', ip.mk_boolean_type(ctx))
    inputs['Daytime'] = n5
    n22 = mk_naked_circuit(ctx, n1, n2, n3, n4, n5)
    # n22 -> traffic_light/out
    ip.mk_output(ctx, n22)
    outputs.append(n22)