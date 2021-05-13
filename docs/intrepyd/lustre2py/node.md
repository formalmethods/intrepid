Module intrepyd.lustre2py.node
==============================
This module implements infrastructure to store nodes

Classes
-------

`EquationTopology(equations, local_decls)`
:   Utility class for sorting equation dependencies topologically

    ### Methods

    `compute_topological_order(self)`
    :   Compute dependencies between equations w.r.t. use of local variables
        
        0. a = b + c
        1. b = c
        2. c = 5 + d
        
        0 -> [2, 3]
        1 -> [2]
        2 -> []       (d is not a local variable)

`Node(name)`
:   Stores a node

    ### Ancestors (in MRO)

    * intrepyd.visitable.Visitable

    ### Instance variables

    `equations`
    :   Getter

    `input_decls`
    :   Getter

    `local_decls`
    :   Getter

    `main`
    :   Getter

    `name`
    :   Getter

    `output_decls`
    :   Getter

    `properties`
    :   Getter

    ### Methods

    `add_equation(self, equation)`
    :   Adds an equation

    `add_input_decl(self, inputs)`
    :   Add a new input declaration

    `add_local_decl(self, llocals)`
    :   Add a new local declaration

    `add_output_decl(self, outputs)`
    :   Add a new output declaration

    `add_property(self, prop)`
    :   Adds a property declaration

    `push_pre_in_equations(self)`
    :   Rewrites rhs of equations in such a way that 'pre' operators
        are pushed to variables

    `sort_equations(self)`
    :   Sort equations in such a way that local variables are
        defined before their use.