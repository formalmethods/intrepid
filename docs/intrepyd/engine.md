Module intrepyd.engine
======================
This module implements the verification engines

Classes
-------

`BackwardReach(ctx)`
:   A Backward Reachability Model Checking algorithm

    ### Ancestors (in MRO)

    * intrepyd.engine.Engine

`Bmc(ctx)`
:   A Bounded Model Checking engine

    ### Ancestors (in MRO)

    * intrepyd.engine.Engine

    ### Descendants

    * intrepyd.engine.OptimizingBmc

    ### Methods

    `set_allow_targets_at_any_depth(self)`
    :   Looks for counterexamples at any depth, not just the current

    `set_current_depth(self, depth)`
    :   Sets the current depth to use for BMC

    `set_use_attack_path_axioms(self, source, target)`
    :   Tells bmc to apply internally axioms for source and target of an attack

    `set_use_induction(self)`
    :   Turn on induction

`Engine(ctx)`
:   Abstract intreface for an Engine

    ### Descendants

    * intrepyd.engine.BackwardReach
    * intrepyd.engine.Bmc

    ### Methods

    `add_target(self, net)`
    :   Adds a target to be solved

    `add_watch(self, net)`
    :   Track the value of net in future traces

    `can_optimize(self)`
    :   Tells if the engine can prove targets to be unreachable

    `can_prove(self)`
    :   Tells if the engine can prove targets to be unreachable

    `can_reach(self)`
    :   Tells if the engine can reach targets

    `get_last_reached_targets(self)`
    :   Returns the list of targets that has been reached last

    `get_last_trace(self)`
    :   Returns the last produced trace

    `reach_targets(self)`
    :   Tries to reach any of the previously added targets

    `remove_last_reached_targets(self)`
    :   Removes all the reached targets from the last call from the engine

`EngineResult(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   Results from engine's reachability calls

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `REACHABLE`
    :

    `UNKNOWN`
    :

    `UNREACHABLE`
    :

`OptimizingBmc(ctx)`
:   An Optimizing Bounded Model Checking engine

    ### Ancestors (in MRO)

    * intrepyd.engine.Bmc
    * intrepyd.engine.Engine