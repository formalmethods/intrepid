FUNCTION_BLOCK Fnc_5
VAR_INPUT
    input1: SINT;
    input2: SINT;
    input3: SINT;
END_VAR
VAR_OUTPUT
    output1: BOOL;
END_VAR
VAR
    local1: SINT;
END_VAR
VAR_TEMP
END_VAR
IF input1 + input2 <= input3 THEN
    local1 := input1;
ELSEIF local1 = 0 THEN
    local1 := 1;
ELSE
    local1 := 0;
END_IF;
output1 := local1 = 0
END_FUNCTION_BLOCK
VAR_GLOBAL CONSTANT
END_VAR
VAR_GLOBAL
END_VAR
