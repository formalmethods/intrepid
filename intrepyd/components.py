import intrepyd as ip

def mk_counter(ctx, name, type, limit, init=None, increment=None, enable=None, reset=None):
    """
    Counts from init to limit by increment. When limit
    is reached, limit is outputted. An enable signal may
    also be specified.

    Args:
        ctx: the context to use
        name: the unique name of this counter
        type: the type of the data stored in the counter
        limit: the limit after which the counter saturates
        init (=0): the initial value of the counter
        increment (=1): the increment value
        enable (=true): the counter is incremented only if enable is true
        reset (=false): resets the counter to the initial value

    Returns:
        the current value of the counter
        true iff the counter has reached saturation
    """
    if init == None:
        init = ip.mk_number(ctx, "0", type)
    if increment == None:
        increment = ip.mk_number(ctx, "1", type)
    if enable == None:
        enable = ip.mk_true(ctx)
    if reset == None:
        reset = ip.mk_false(ctx)

    counter = ip.mk_latch(ctx, name, type)
    notQ = ip.mk_lt(ctx, counter, limit)
    next = ip.mk_ite(ctx, reset,\
                          init,\
                          ip.mk_ite(ctx, ip.mk_and(ctx, enable, notQ),\
                                         ip.mk_add(ctx, counter, increment),\
                                         counter))
    ip.set_latch_init_next(ctx, counter, init, next)
    Q = ip.mk_not(ctx, notQ)
    return counter, Q