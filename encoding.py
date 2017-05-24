# Translated from ../kind2-benchmarks/simulation/ums.lus using lustre2py on 2017-05-24

import intrepyd

LATCH2PRE = {}
LATCHEQUIV = []

def Sofar(ctx, __first_tick, X):
    __bt = ctx.mk_boolean_type()
    __it = ctx.mk_int32_type()
    __rt = ctx.mk_real_type()
    pre_Sofar = ctx.mk_latch("pre_Sofar", __bt)
    __l2 = ctx.mk_and(X, pre_Sofar)
    __l1 = ctx.mk_ite(__first_tick, X, __l2)
    Sofar = __l1
    if Sofar in LATCH2PRE:
        LATCHEQUIV.append((LATCH2PRE[Sofar], pre_Sofar))
    LATCH2PRE[Sofar] = pre_Sofar
    ctx.set_latch_init_next(pre_Sofar, ctx.mk_false(), Sofar)
    return Sofar

def edge(ctx, __first_tick, X):
    __bt = ctx.mk_boolean_type()
    __it = ctx.mk_int32_type()
    __rt = ctx.mk_real_type()
    pre_X = ctx.mk_latch("pre_X", __bt)
    __l5 = ctx.mk_not(pre_X)
    __l4 = ctx.mk_and(X, __l5)
    __l3 = ctx.mk_ite(__first_tick, X, __l4)
    Y = __l3
    if X in LATCH2PRE:
        LATCHEQUIV.append((LATCH2PRE[X], pre_X))
    LATCH2PRE[X] = pre_X
    ctx.set_latch_init_next(pre_X, ctx.mk_false(), X)
    return Y

def after(ctx, __first_tick, A):
    __bt = ctx.mk_boolean_type()
    __it = ctx.mk_int32_type()
    __rt = ctx.mk_real_type()
    pre_A = ctx.mk_latch("pre_A", __bt)
    pre_afterA = ctx.mk_latch("pre_afterA", __bt)
    __l7 = ctx.mk_or(pre_A, pre_afterA)
    __l6 = ctx.mk_ite(__first_tick, ctx.mk_false(), __l7)
    afterA = __l6
    if A in LATCH2PRE:
        LATCHEQUIV.append((LATCH2PRE[A], pre_A))
    LATCH2PRE[A] = pre_A
    ctx.set_latch_init_next(pre_A, ctx.mk_false(), A)
    if afterA in LATCH2PRE:
        LATCHEQUIV.append((LATCH2PRE[afterA], pre_afterA))
    LATCH2PRE[afterA] = pre_afterA
    ctx.set_latch_init_next(pre_afterA, ctx.mk_false(), afterA)
    return afterA

def always_since(ctx, __first_tick, B, A):
    __bt = ctx.mk_boolean_type()
    __it = ctx.mk_int32_type()
    __rt = ctx.mk_real_type()
    ctx.push_namespace("after.1")
    __l10 = after(ctx, __first_tick, A)
    ctx.pop_namespace()
    pre_alwaysBsinceA = ctx.mk_latch("pre_alwaysBsinceA", __bt)
    __l11 = ctx.mk_and(B, pre_alwaysBsinceA)
    __l9 = ctx.mk_ite(__l10, __l11, ctx.mk_true())
    __l8 = ctx.mk_ite(A, B, __l9)
    alwaysBsinceA = __l8
    if alwaysBsinceA in LATCH2PRE:
        LATCHEQUIV.append((LATCH2PRE[alwaysBsinceA], pre_alwaysBsinceA))
    LATCH2PRE[alwaysBsinceA] = pre_alwaysBsinceA
    ctx.set_latch_init_next(pre_alwaysBsinceA, ctx.mk_false(), alwaysBsinceA)
    return alwaysBsinceA

def once_since(ctx, __first_tick, C, A):
    __bt = ctx.mk_boolean_type()
    __it = ctx.mk_int32_type()
    __rt = ctx.mk_real_type()
    ctx.push_namespace("after.2")
    __l14 = after(ctx, __first_tick, A)
    ctx.pop_namespace()
    pre_onceCsinceA = ctx.mk_latch("pre_onceCsinceA", __bt)
    __l15 = ctx.mk_or(C, pre_onceCsinceA)
    __l13 = ctx.mk_ite(__l14, __l15, ctx.mk_true())
    __l12 = ctx.mk_ite(A, C, __l13)
    onceCsinceA = __l12
    if onceCsinceA in LATCH2PRE:
        LATCHEQUIV.append((LATCH2PRE[onceCsinceA], pre_onceCsinceA))
    LATCH2PRE[onceCsinceA] = pre_onceCsinceA
    ctx.set_latch_init_next(pre_onceCsinceA, ctx.mk_false(), onceCsinceA)
    return onceCsinceA

def implies(ctx, __first_tick, A, B):
    __bt = ctx.mk_boolean_type()
    __it = ctx.mk_int32_type()
    __rt = ctx.mk_real_type()
    __l17 = ctx.mk_not(A)
    __l16 = ctx.mk_or(__l17, B)
    AimpliesB = __l16
    return AimpliesB

def always_from_to(ctx, __first_tick, B, A, C):
    __bt = ctx.mk_boolean_type()
    __it = ctx.mk_int32_type()
    __rt = ctx.mk_real_type()
    ctx.push_namespace("after.4")
    __l19 = after(ctx, __first_tick, A)
    ctx.pop_namespace()
    ctx.push_namespace("always_since.5")
    __l21 = always_since(ctx, __first_tick, B, A)
    ctx.pop_namespace()
    ctx.push_namespace("once_since.6")
    __l22 = once_since(ctx, __first_tick, C, A)
    ctx.pop_namespace()
    __l20 = ctx.mk_or(__l21, __l22)
    ctx.push_namespace("implies.3")
    __l18 = implies(ctx, __first_tick, __l19, __l20)
    ctx.pop_namespace()
    X = __l18
    return X

def UMS(ctx, __first_tick, on_A, on_B, on_C, ack_AB, ack_BC):
    __bt = ctx.mk_boolean_type()
    __it = ctx.mk_int32_type()
    __rt = ctx.mk_real_type()
    __l24 = ctx.mk_or(on_A, on_B)
    __l23 = ctx.mk_or(__l24, on_C)
    __l25 = ctx.mk_not(__l23)
    empty_section = __l25
    __l26 = ctx.mk_and(empty_section, ack_AB)
    grant_access = __l26
    __l28 = ctx.mk_or(on_A, on_C)
    __l29 = ctx.mk_not(__l28)
    __l27 = ctx.mk_and(on_B, __l29)
    only_on_B = __l27
    __l30 = ctx.mk_and(only_on_B, ack_BC)
    grant_exit = __l30
    __l32 = ctx.mk_not(ack_AB)
    __l31 = ctx.mk_and(__l32, empty_section)
    do_AB = __l31
    __l34 = ctx.mk_not(ack_BC)
    __l33 = ctx.mk_and(__l34, only_on_B)
    do_BC = __l33
    return grant_access, grant_exit, do_AB, do_BC

def top(ctx, __first_tick, on_A, on_B, on_C, ack_AB, ack_BC):
    __bt = ctx.mk_boolean_type()
    __it = ctx.mk_int32_type()
    __rt = ctx.mk_real_type()
    __l36 = ctx.mk_or(on_A, on_B)
    __l35 = ctx.mk_or(__l36, on_C)
    __l37 = ctx.mk_not(__l35)
    empty_section = __l37
    __l39 = ctx.mk_or(on_A, on_C)
    __l40 = ctx.mk_not(__l39)
    __l38 = ctx.mk_and(on_B, __l40)
    only_on_B = __l38
    ctx.push_namespace("UMS.7")
    __l41 = UMS(ctx, __first_tick, on_A, on_B, on_C, ack_AB, ack_BC)
    ctx.pop_namespace()
    grant_access, grant_exit, do_AB, do_BC = __l41
    __l50 = ctx.mk_and(ack_AB, ack_BC)
    __l51 = ctx.mk_not(__l50)
    ctx.push_namespace("always_from_to.9")
    __l52 = always_from_to(ctx, __first_tick, ack_AB, ack_AB, do_BC)
    ctx.pop_namespace()
    __l49 = ctx.mk_and(__l51, __l52)
    ctx.push_namespace("always_from_to.10")
    __l53 = always_from_to(ctx, __first_tick, ack_BC, ack_BC, do_AB)
    ctx.pop_namespace()
    __l48 = ctx.mk_and(__l49, __l53)
    __l54 = ctx.mk_ite(__first_tick, empty_section, ctx.mk_true())
    __l47 = ctx.mk_and(__l48, __l54)
    __l58 = ctx.mk_not(empty_section)
    ctx.push_namespace("edge.12")
    __l57 = edge(ctx, __first_tick, __l58)
    ctx.pop_namespace()
    pre_grant_access = ctx.mk_latch("pre_grant_access", __bt)
    ctx.push_namespace("implies.11")
    __l56 = implies(ctx, __first_tick, __l57, pre_grant_access)
    ctx.pop_namespace()
    __l55 = ctx.mk_ite(__first_tick, ctx.mk_true(), __l56)
    __l46 = ctx.mk_and(__l47, __l55)
    ctx.push_namespace("edge.14")
    __l61 = edge(ctx, __first_tick, on_C)
    ctx.pop_namespace()
    pre_grant_exit = ctx.mk_latch("pre_grant_exit", __bt)
    ctx.push_namespace("implies.13")
    __l60 = implies(ctx, __first_tick, __l61, pre_grant_exit)
    ctx.pop_namespace()
    __l59 = ctx.mk_ite(__first_tick, ctx.mk_true(), __l60)
    __l45 = ctx.mk_and(__l46, __l59)
    __l64 = ctx.mk_not(on_A)
    ctx.push_namespace("edge.16")
    __l63 = edge(ctx, __first_tick, __l64)
    ctx.pop_namespace()
    ctx.push_namespace("implies.15")
    __l62 = implies(ctx, __first_tick, __l63, on_B)
    ctx.pop_namespace()
    __l44 = ctx.mk_and(__l45, __l62)
    __l67 = ctx.mk_not(on_B)
    ctx.push_namespace("edge.18")
    __l66 = edge(ctx, __first_tick, __l67)
    ctx.pop_namespace()
    __l68 = ctx.mk_or(on_A, on_C)
    ctx.push_namespace("implies.17")
    __l65 = implies(ctx, __first_tick, __l66, __l68)
    ctx.pop_namespace()
    __l43 = ctx.mk_and(__l44, __l65)
    ctx.push_namespace("Sofar.8")
    __l42 = Sofar(ctx, __first_tick, __l43)
    ctx.pop_namespace()
    env = __l42
    ctx.push_namespace("implies.19")
    __l69 = implies(ctx, __first_tick, grant_access, empty_section)
    ctx.pop_namespace()
    no_collision = __l69
    __l70 = ctx.mk_and(do_AB, do_BC)
    __l71 = ctx.mk_not(__l70)
    exclusive_req = __l71
    ctx.push_namespace("always_from_to.20")
    __l72 = always_from_to(ctx, __first_tick, ack_AB, grant_access, only_on_B)
    ctx.pop_namespace()
    no_derail_AB = __l72
    ctx.push_namespace("always_from_to.21")
    __l73 = always_from_to(ctx, __first_tick, ack_BC, grant_exit, empty_section)
    ctx.pop_namespace()
    no_derail_BC = __l73
    __l77 = ctx.mk_and(no_collision, exclusive_req)
    __l76 = ctx.mk_and(__l77, no_derail_AB)
    __l75 = ctx.mk_and(__l76, no_derail_BC)
    __l74 = ctx.mk_implies(env, __l75)
    OK = __l74
    if grant_access in LATCH2PRE:
        LATCHEQUIV.append((LATCH2PRE[grant_access], pre_grant_access))
    LATCH2PRE[grant_access] = pre_grant_access
    ctx.set_latch_init_next(pre_grant_access, ctx.mk_false(), grant_access)
    if grant_exit in LATCH2PRE:
        LATCHEQUIV.append((LATCH2PRE[grant_exit], pre_grant_exit))
    LATCH2PRE[grant_exit] = pre_grant_exit
    ctx.set_latch_init_next(pre_grant_exit, ctx.mk_false(), grant_exit)
    return OK

def lustre2py_main():
    ctx = intrepyd.Context()
    __bt = ctx.mk_boolean_type()
    __it = ctx.mk_int32_type()
    __rt = ctx.mk_real_type()
    __first_tick = ctx.mk_latch("__first_tick", ctx.mk_boolean_type())
    ctx.set_latch_init_next(__first_tick, ctx.mk_true(), ctx.mk_false())
    i0 = ctx.mk_input("i0", __bt)
    i1 = ctx.mk_input("i1", __bt)
    i2 = ctx.mk_input("i2", __bt)
    i3 = ctx.mk_input("i3", __bt)
    i4 = ctx.mk_input("i4", __bt)
    prop = top(ctx, __first_tick, i0, i1, i2, i3, i4)
    return ctx

if __name__ == "__main__":
    ctx = lustre2py_main()

