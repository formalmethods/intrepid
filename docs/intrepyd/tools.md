Module intrepyd.tools
=====================
Provides some tools that could be used almost out of the box

Functions
---------

    
`simulate(ctx, infile, depth, outputs)`
:   Simulates the design using default values for inputs or by taking
    input values from an existing simulation file

    
`translate_iec61131(infilename, outmodule='encoding')`
:   Translates a ST iec61131 file into intrepyd syntax

    
`translate_lustre(infilename, topnode, realtype, outmodule='encoding')`
:   Translates a lustre file into intrepyd syntax