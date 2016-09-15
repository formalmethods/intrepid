PROGRAM Fnc_16
    VAR
       switch: BOOL;
    END_VAR

    VAR_OUTPUT
        out: BOOL;
    END_VAR

    CASE switch OF
    TRUE:
        switch := FALSE
    ELSE
        switch := TRUE
    END_CASE;
    out := switch
END_PROGRAM
