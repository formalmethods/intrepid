import intrepyd as ip
import intrepyd.components
import intrepyd.trace

if __name__ == "__main__":
    ctx = ip.Context()
    int8type = ctx.mk_int8_type()
    ten = ctx.mk_number("10", int8type)
    counter, Q = ip.components.mk_counter(ctx, "counter", type=int8type, limit=ten)
    simulator = ctx.mk_simulator()
    tr = ctx.mk_trace()
    simulator.add_watch(counter)
    simulator.add_watch(Q)
    simulator.simulate(tr, 12)
    df = tr.get_as_dataframe(ctx.net2name)
    print df
