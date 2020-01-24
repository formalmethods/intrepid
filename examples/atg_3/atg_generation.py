import intrepyd as ip
import intrepyd.atg
import intrepyd.atg.mcdc
import intrepyd.circuit

# The translated circuit
import circuit

if __name__ == "__main__":
    ctx = ip.Context()
    decisions = { 'circuit/Out' : ['In1', 'In2', 'In3', 'In4', 'In5'] }
    tables, _, _ = ip.atg.mcdc.compute_mcdc(ctx, circuit.SimulinkCircuit, decisions, max_depth=10)
    decision2dataframe = ip.atg.mcdc.get_tables_as_dataframe(tables)
    print '\nGenerated tests:'
    print decision2dataframe['circuit/Out']
