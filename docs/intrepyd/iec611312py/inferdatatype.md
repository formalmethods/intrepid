Module intrepyd.iec611312py.inferdatatype
=========================================
This module implements type inference for expressions

Functions
---------

    
`getConversionOperatorInputType(operator)`
:   

    
`getConversionOperatorOutputType(operator)`
:   

Classes
-------

`InferDatatypeBottomUp()`
:   Visitor for inferring expressions datatype

    ### Ancestors (in MRO)

    * intrepyd.iec611312py.visitor.Visitor

    ### Methods

    `process_statements(self, statements)`
    :

`InferDatatypeTopDown()`
:   Visitor for inferring expressions datatype

    ### Ancestors (in MRO)

    * intrepyd.iec611312py.visitor.Visitor

    ### Methods

    `process_statements(self, statements)`
    :