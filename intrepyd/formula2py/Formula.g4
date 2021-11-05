grammar Formula;

formula: expr EOF;

expr: op=('not' | 'NOT') expr           # notExpr
	| op=('pre' | 'PRE') expr           # preExpr
    | expr (('and' | 'AND') expr)+      # andExpr
    | expr (('or' | 'OR') expr)+        # orExpr
	| '(' expr ')'                      # parExpr
	| ID                                # parID
    ;

ID: [a-zA-Z_][a-zA-Z_0-9]*;

WS: [ \t\n\r\f]+ -> skip;

ERROR: .;
