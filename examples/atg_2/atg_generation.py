import intrepid as ip
import intrepid.atg
import intrepid.circuit
import intrepid.utils
import collections
import pprint
import pandas as pd
import circuit

if __name__ == "__main__":
    ctx = ip.mk_ctx()
    decisions = { 'circuit/Out' : ['In1', 'In2', 'In3', 'In4', 'In5', 'In6'] }
    tables = ip.atg.compute_mcdc(ctx, circuit.SimulinkCircuit, decisions, maxDepth=10)
    decision2dataframe = ip.atg.get_tables_as_dataframe(tables)
    print '\nGenerated tests:'
    print decision2dataframe['circuit/Out']
    ip.del_ctx(ctx)