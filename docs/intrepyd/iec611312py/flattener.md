Module intrepyd.iec611312py.flattener
=====================================
This module implements a flattener for ST terms

Functions
---------

    
`build_ite(varOcc, conditions, rewritten_stmt_blocks)`
:   

    
`collect_lhss(blocks)`
:   

    
`find_rhs_for(varOcc, block)`
:   

Classes
-------

`Flattener()`
:   Flattens statements

    ### Methods

    `flatten_case(self, instruction)`
    :

    `flatten_if_then_else(self, instruction)`
    :

    `flatten_instruction(self, instruction)`
    :

    `flatten_stmt_block(self, block)`
    :

    `flatten_stmt_block_impl(self, block)`
    :