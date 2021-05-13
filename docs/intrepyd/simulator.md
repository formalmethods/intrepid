Module intrepyd.simulator
=========================
The Simulator

Classes
-------

`Simulator(ctx)`
:   Simulates the circuit in the context by using the input values provided
    in the trace. If a value is not present at a time step, the default
    value for the type is taken

    ### Methods

    `add_watch(self, net)`
    :   Tells the simulator about a net whose value will be reported in the simulated trace

    `simulate(self, trace, depth)`
    :   Executes a simulation using the values in trace, up to the specified depth