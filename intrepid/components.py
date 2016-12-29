import intrepid as ip

def mk_counter(ctx, name, type, init, increment, limit, enable):
    """
    Counts from init to limit by increment. When limit
    is reached, limit is outputted. An enable signal may
    also be specified.
    """
    counter = ip.mk_latch(ctx, name, type)
    zero = ip.mk_number(ctx, "0", type)
    enable = enable and ip.mk_lt(ctx, counter, limit)
    next = ip.mk_ite(ctx, enable, ip.mk_add(ctx, counter, increment), counter)
    ip.set_latch_init_next(ctx, counter, init, next)
    return counter