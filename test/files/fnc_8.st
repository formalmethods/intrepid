FUNCTION_BLOCK Fnc_8
VAR_INPUT
    input1: SINT;
    input2: SINT;
    input3: SINT;
END_VAR
VAR_OUTPUT
    output1: BOOL;
END_VAR
VAR
    local2: SINT;
END_VAR
VAR_TEMP
END_VAR
IF input1 + input2 <= input3 THEN
    local2 := input1;
ELSEIF local2 = 0 THEN
    local2 := 1;
ELSE
    local2 := 0;
END_IF;
output1 := local2 = 0
END_FUNCTION_BLOCK
VAR_GLOBAL CONSTANT
END_VAR
VAR_GLOBAL
END_VAR
