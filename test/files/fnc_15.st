PROGRAM Fnc_15
    VAR
       switch: BOOL;
    END_VAR

    VAR_OUTPUT
        out: BOOL;
    END_VAR

    CASE switch OF
    TRUE:
        switch := FALSE
    FALSE:
        switch := TRUE
    END_CASE;
    out := switch
END_PROGRAM
