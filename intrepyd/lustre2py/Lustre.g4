grammar Lustre;

program: (datatypedef | constant | node)* EOF;

datatypedef: 'datatype' ID '=' topLevelType ';';

constant: 'const' ID (':' datatype)? '=' expr ';';

node:
  'node' ID '(' inp=varDeclList? ')'
  'returns' '(' outp=varDeclList? ')' ';'
  ('var' local=varDeclList ';')?
  'let' instrlst=instrList? 'tel' ';'?
;

instrList: instr+ ;

instr: equation
     | prop 
     | assertion 
     | main 
     | realizabilityInputs 
     | ivc
     ;

varDeclList: varDeclGroup (';' varDeclGroup)*;

varDeclGroup: eID (',' eID)* ':' datatype;

topLevelType: datatype                                           # plainType
    | 'struct' '{' (ID ':' datatype) (';' ID ':' datatype)* '}'  # recordType
    | 'enum' '{' ID (',' ID)* '}'                                # enumType
    ;

datatype: 'int'                                                  # primitiveType
    | 'subrange' '[' bound ',' bound ']' 'of' 'int'              # subrangeType
    | 'bool'                                                     # primitiveType
    | 'real'                                                     # primitiveType
    | datatype '[' INT ']'                                       # arrayType
    | ID                                                         # userType
    ;

bound: '-'? INT;

prop: '--%PROPERTY' expr ';';

realizabilityInputs: '--%REALIZABLE' (ID (',' ID)*)? ';';

ivc: '--%IVC' (ID (',' ID)*)? ';';

main: '--%MAIN' ';'?;

assertion: 'assert' expr ';';

equation: (pos1=lhs | '(' pos2=lhs? ')') '=' pos3=expr ';';

lhs: eID (',' eID)*;

expr: ID                                                         # idExpr
    | '-'? INT                                                   # intExpr
    | REAL                                                       # realExpr
    | BOOL                                                       # boolExpr
    | op=('real' | 'floor') '(' expr ')'                         # castExpr
    | ID '(' (expr (',' expr)*)? ')'                             # nodeCallExpr
    | 'condact' '(' expr (',' expr)+ ')'                         # condactExpr
    | expr '.' ID                                                # recordAccessExpr
    | expr '{' ID ':=' expr '}'                                  # recordUpdateExpr
    | expr '[' expr ']'                                          # arrayAccessExpr
    | expr '[' expr ':=' expr ']'                                # arrayUpdateExpr
    | 'pre' expr                                                 # preExpr
    | 'not' expr                                                 # notExpr
    | '-' expr                                                   # negateExpr
    | expr op=('*' | '/' | 'div' | 'mod') expr                   # binaryExpr
    | expr op=('+' | '-') expr                                   # binaryExpr
    | expr op=('<' | '<=' | '>' | '>=' | '=' | '<>') expr        # binaryExpr
    | expr op='and' expr                                         # binaryExpr
    | expr op=('or' | 'xor') expr                                # binaryExpr
    | <assoc=right> expr op='=>' expr                            # binaryExpr
    | <assoc=right> expr op='->' expr                            # initCurrExpr
    | 'if' expr 'then' expr 'else' expr                          # ifThenElseExpr
    | ID '{' ID '=' expr (';' ID '=' expr)* '}'                  # recordExpr
    | '[' expr (',' expr)* ']'                                   # arrayExpr
    | '(' expr (',' expr)* ')'                                   # tupleExpr
    ;

// eID used internally. Users should only use ID.
eID: ID                                                          # baseEID
   | eID '[' INT ']'                                             # arrayEID
   | eID '.' ID                                                  # recordEID
   ;

REAL: INT '.' INT;

BOOL: 'true' | 'false';
INT: [0-9]+;

// ~ is used internally. Users should not use it.
ID: [a-zA-Z_~][a-zA-Z_0-9~]*;

WS: [ \t\n\r\f]+ -> skip;

SL_COMMENT: '--' (~[%\n\r] ~[\n\r]* | /* empty */) ('\r'? '\n')? -> skip;
ML_COMMENT: '(*' .*? '*)' -> skip;
C_COMMENT: '/*' .*? '*/' -> skip;

ERROR: .;
