import intrepyd as ip
import intrepyd.components
import intrepyd.utils

ctx = ip.mk_ctx()
int8type = ip.mk_int8_type(ctx)
ten = ip.mk_number(ctx, "10", int8type)
counter, Q = ip.components.mk_counter(ctx, "counter", type=int8type, limit=ten)
simulator = ip.mk_simulator(ctx)
ip.simulator_add_watch(ctx, simulator, counter)
ip.simulator_add_watch(ctx, simulator, Q)
cex = ip.simulator_default_simulate(simulator, 12)
cexDict = ip.utils.counterexample_get_as_dictionary(ctx, cex, {}, { 'counter' : counter, 'Q' : Q })
df = ip.utils.counterexample_get_as_dataframe(cexDict)
print df
ip.del_ctx(ctx)
