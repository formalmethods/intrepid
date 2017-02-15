import intrepyd as ip
import intrepyd.atg
import intrepyd.circuit

# The translated circuit
import circuit

if __name__ == "__main__":
    ctx = ip.Context()
    decisions = { 'circuit/Out' : ['In1', 'In2', 'In3', 'In4', 'In5'] }
    tables, _ = ip.atg.compute_mcdc(ctx, circuit.SimulinkCircuit, decisions, maxDepth=10)
    decision2dataframe = ip.atg.get_tables_as_dataframe(tables)
    print '\nGenerated tests:'
    print decision2dataframe['circuit/Out']
