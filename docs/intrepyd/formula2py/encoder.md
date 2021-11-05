Module intrepyd.formula2py.encoder
==================================
Parses a formula

Functions
---------

    
`compute_pre_depth(formula)`
:   Computes the depth of nesting of pres in the formula

    
`encode_formula(ctx, input_string)`
:   Encodes the formula passed as input into the context
    The context must contain the symbols mentioned in the
    input string

    
`parse_string(input_string)`
:   Parse the provided string and create it in the provided
    intrepyd context. Returns the produced net or aborts with
    an error