"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017

This module implements infrastructure to store instructions
"""

import intrepyd as ip
import intrepyd.api

def mk_counter(context, name, type, limit, init=None, increment=None, enable=None, reset=None):
    """
    Counts from init to limit by increment. When limit
    is reached, limit is outputted. An enable signal may
    also be specified.

    Args:
        context: the context to use
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
        init = context.mk_number("0", type)
    if increment == None:
        increment = context.mk_number("1", type)
    if enable == None:
        enable = context.mk_true()
    if reset == None:
        reset = context.mk_false()

    counter = context.mk_latch(name, type)
    notQ = context.mk_lt(counter, limit)
    next = context.mk_ite(reset,\
                          init,\
                          context.mk_ite(context.mk_and(enable, notQ),\
                                         context.mk_add(counter, increment),\
                                         counter))
    context.set_latch_init_next(counter, init, next)
    Q = context.mk_not(notQ, name + '.Q')
    return counter, Q