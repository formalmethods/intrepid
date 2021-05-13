Module intrepyd.components.eda
==============================
Implementation of EDA-specific components

Functions
---------

    
`mk_clock(ctx, name)`
:   Creates a clock signal

    
`mk_counter(context, name, typ, limit, init=None, increment=None, enable=None, reset=None)`
:   Counts from init to limit by increment. Returns the
    value of the counter and whether the limit has been
    reached or not. An enable signal and a reset signal
    may also be specified.
    
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
        counter: the current value of the counter
        Q: true iff the counter has reached saturation

Classes
-------

`Delay(ctx, name, t)`
:   Delay (D)
    
    Delays a signal by one full clock cycle
    
    Symbol:
          ____
         |    |
    D ---| D  |--- Q
         |    |
         |>   |
         |____|
    
    Diagram:
        Two latches in series
    
          ____     ____
         |    |   |    |
    D ---| L  |---| L  |--- Q
         |    |   |    |
         |____|   |____|
    
    Args:
        ctx: the context to use
        name: the unique name
        t: the type of the data stored

    ### Methods

    `set_init_next(self, init, d)`
    :   Sets the initial value of the latch
        
        Args:
            init: the "fill" value for the first cycle
            D: the input signal

`FlipFlopD(ctx, name, t, c)`
:   Flip Flop D (FFD)
    
    Args:
        ctx: the context to use
        name: the unique name
        t: the type of the data stored
        C: the clock signal
    
    Returns:
        Q: the value stored in the flip flop
    
    Symbol:
          _____
         |     |
    D ---| FFD |--- Q
         |     |
    C ---|>    |
         |_____|
    
    Diagram:
        It consists of a master DL and a slave LD. The
        diagram shows the raising-edge version (notice
        the negated clock in the master latchD)
    
                        +---------------------+
                        |   ____              |
           _____        |  |    |             |
          |     |       +--| L  |---+   __    |
    D ----| LD  |---+      |    |   |  |  \   |
          |     |   |      |____|   +--| 0 |  |
    C -+-o|     |   |                  |   |--+-- Q
       |  |_____|   +------------------| 1 |
       |                               |__/
       |                                 |
       +---------------------------------+
    
    Args:
        ctx: the context to use
        name: the unique name
        t: the type of the data stored
        C: the clock signal

    ### Methods

    `set_init_next(self, init, d)`
    :   Sets the initial and next value
        
        Args:
            init: the initial value
            D: the flip flop input signal

`FlipFlopDE(ctx, name, t, c)`
:   Flip Flop D with Enable (FFDE)
    
    Symbol:
          _____
         |     |
    D ---| FFD |--- Q
    E ---|     |
    C ---|>    |
         |_____|
    
    Diagram:
    
    It consists of a FFD wrapped by a mux
    
       +--------------------+
       |   __               |
       |  |  \     _____    |
       +--| 0 |   |     |   |
          |   |---| FFD |---+--- Q
     D ---| 1 |   |     |
          |__/  +-|>    |
            |   | |_____|
     E -----+   |
                |
     C ---------+
    
    Args:
        ctx: the context to use
        name: the unique name
        t: the type of the data stored
        C: the clock signal

    ### Methods

    `set_init_next(self, init, d, e)`
    :   Sets the initial and next value
        
        Args:
            init: the initial value
            D: the flip flop input signal
            E: the flip flop enable signal

`LatchD(ctx, name, t)`
:   LatchD (LD)
    
    A latch with enable
    
    Symbol:
          ____
         |    |
    D ---| LD |--- Q
         |    |
    E ---|    |
         |____|
    
    Diagram:
        A latch wrapped around a mux
    
        +--------------------+
        |   __               |
        |  |  \      ____    |
        +--| 0 |    |    |   |
           |   |----| L  |---+--- Q
      D ---| 1 |    |    |
           |__/     |____|
             |
             |
      E -----+
    
    Args:
        ctx: the context to use
        name: the unique name
        t: the type of the data stored

    ### Methods

    `set_init_next(self, init, d, e)`
    :   Sets the initial value of the latch
        
        Args:
            init: the initial value
            D: the input signal
            E: the enable signal