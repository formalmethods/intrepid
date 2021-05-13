Module intrepyd.pseudoboolean
=============================
Routines for pseudo-boolean functions

Functions
---------

    
`mk_at_least_one(ctx, nets)`
:   Computes "at least one net is true"
    
    Args:
        ctx: the context to use
        nets: the nets to use

    
`mk_at_most_one(ctx, nets)`
:   Computes "at most one net is true"
    
    Args:
        ctx: the context to use
        nets: the nets to use

    
`mk_exactly_one(ctx, nets, name)`
:   Computes the pseudo-boolean constraint "exactly one is true".
    Uses the "commander variable" encoding described in
    "Efficient CNF Encoding for Selecting 1 from N Objects"
    by Will Klieber and Gihwon Kwon.
    
    Args:
        ctx: the context to use
        nets: the list of (Boolean) nets
    
    Returns:
        a net expressing the constraint "exactly one is true"