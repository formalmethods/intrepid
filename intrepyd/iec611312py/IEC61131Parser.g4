/*
 * Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
 * 
 * This file is distributed under the terms of the 3-clause BSD License.
 * A copy of the license can be found in the root directory or at
 * https://opensource.org/licenses/BSD-3-Clause.
 * 
 * Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
 *   Date: 26/10/2017
 * 
 * A parser for IEC61131-3 ST and IL languages
 */

grammar IEC61131Parser;
import IEC61131Lexer;

/*****************************************************************************************************************
 * POU SECTION
 ****************************************************************************************************************/

pou_decl         : PROGRAM IDENTIFIER variable_blocks? body? END_PROGRAM                      # programDecl
                 | FUNCTION_BLOCK (IDENTIFIER | fb_std_names)
                   variable_blocks? body? END_FUNCTION_BLOCK                                  # fbDecl
                 ;

fb_std_names     : R_TRIG | F_TRIG | TON | TOF | TP | CTU ;

body             : instruction+                                                               # bodyIL
                 | stmt_block                                                                 # bodyST
                 ;                             

/*****************************************************************************************************************
 * VARIABLE DECLARATION SECTION
 ****************************************************************************************************************/

variable_blocks  : variable_block+;

variable_block   : VAR_GLOBAL   attr=(CONSTANT | RETAIN)?   variable_decls END_VAR            # varGlobalBlock
                 | VAR          attr=(CONSTANT | RETAIN)?   variable_decls END_VAR            # varLocalBlock
                 | VAR_INPUT    attr=(RETAIN | NON_RETAIN)? variable_decls END_VAR            # varInputBlock
                 | VAR_OUTPUT   attr=(RETAIN | NON_RETAIN)? variable_decls END_VAR            # varOutputBlock
                 | VAR_IN_OUT   attr=(RETAIN | NON_RETAIN)? variable_decls END_VAR            # varInOutBlock
                 | VAR_EXTERNAL attr=CONSTANT?              variable_decls END_VAR            # varExternalBlock
                 ;

variable_decls   : (variable_decl ';')* ;

variable_decl    : name=variable_name?
                   loc=located_at? ':' dt=data_type ':=' init=variable_init                   # varDeclInit
                 | name=variable_name? loc=located_at? ':' dt=data_type                       # varDeclNoInit
                 | name=variable_name? ':' dt=data_type loc=located_at                        # varDeclRevLoc
                 ;
 
located_at       : AT DIRECTVARIABLE;

variable_init    : signed_int ;

/*****************************************************************************************************************
 * DATATYPE SECTION
 ****************************************************************************************************************/

data_type        : name=( BOOL | BYTE | WORD | DWORD  
                        | INT | SINT | DINT
                        | UINT | USINT | UDINT
                        | REAL | BOOL_EXP )
                   attr=(R_EDGE | F_EDGE)?                                                    # basicDataType
                 | name=TIME                                                                  # timeDataType
                 | name=ARRAY '[' ranfrom=uns_int '..' ranto=uns_int ']' OF dt=data_type      # arrayDataType
                 | name=( SR | RS | R_TRIG | F_TRIG
                        | CTU | CTD | CTUD
                        | TP | TON | TOF )                                                    # stdFbDataType
                 | name=IDENTIFIER                                                            # usrFbDataType
                 ;

/*****************************************************************************************************************
 * IL SECTION
 ****************************************************************************************************************/

instruction      : lab=label ':' instr=il_instruction                                         # instrFull
                 | lab=label ':'                                                              # instrLabel
                 | instr=il_instruction                                                       # instrIlInstr
                 ;

label            : IDENTIFIER ;

il_instruction   : il_instr_op expr=il_expr                                                   # ilInstrUnarySimple
                 | bop=il_expr_bop expr=il_expr                                               # ilInstrUnaryExpr
                 | bop=il_expr_bop '(' expr=il_expr ')'                                       # ilInstrUnaryExpr
                 | il_expr_uop                                                                # ilInstrZeroary
                 | op=( CAL | CALC | CALCN ) IDENTIFIER ( '(' params=il_call_pars ')' )?      # ilInstrCall
                 | op=( JMP | JMPC | JMPCN ) label                                            # ilInstrJump
                 | op=( RET | RETC | RETCN )                                                  # ilInstrReturn
                 ;

il_instr_op      : LD | LDN | ST | STN | 'R' | 'S' ;

il_expr_uop      : NOT | conversion_function | std_func_name ;

il_expr_bop      : AND | OR | XOR | ANDN | ORN
                 | XORN | ADD | SUB | MUL | DIV
                 | MOD | GT | GE | EQ | LT | LE | NE
                 | SHR | SHL
                 ;

il_expr          : '(' simple=il_expr_simple lst=il_instruction_list? ')'                     # ilExprComplex
                 | il_expr_simple                                                             # ilExprSimple
                 ;

il_instruction_list : il_instruction_one+ ;

il_instruction_one : il_instruction ;

il_expr_simple   : constant
                 | variable_name 
                 | array_access 
                 | composite_access 
                 | il_expr_simple '.' uns_int
                 ;

il_call_pars     : il_call_args ;

il_call_args     : il_call_arg ( ',' il_call_arg )* ;

il_call_arg      : param1=variable_name? ':=' param2=il_expr? ;

/*****************************************************************************************************************
 * ST SECTION
 ****************************************************************************************************************/

st_stmt          : assign_stmt ';'
                 | if_stmt ';'
                 | case_stmt ';'
                 | while_stmt ';'
                 | for_stmt ';'
                 | repeat_stmt ';'
                 ;

assign_stmt      : simple_var ':=' expression             # assignVariable
                 | array_access ':=' expression           # assignArrayCell
                 | variable_bit_access ':=' expression    # assignBitAccess
                 | composite_access ':=' expression       # assignCompositeAccess
                 ;

if_stmt          : if_simple_stmt | if_elseif_stmt | if_else_stmt | if_complete_stmt ;

if_simple_stmt   : IF ifexpr=bool_expression THEN ifstmt=stmt_block END_IF ;

if_elseif_stmt   : IF ifexpr=bool_expression THEN ifstmt=stmt_block
                   elsifstmt=elsif_stmt_list
                   END_IF
                 ;

if_else_stmt     : IF ifexpr=bool_expression THEN ifstmt=stmt_block
                   elsestmt=else_stmt 
                   END_IF
                 ;

if_complete_stmt : IF ifexpr=bool_expression THEN ifstmt=stmt_block
                   elsifstmt=elsif_stmt_list
                   elsestmt=else_stmt 
                   END_IF
                 ;

elsif_stmt_list  : elsif_stmt+ ;

elsif_stmt       : ELSIF expr=bool_expression THEN stmtblock=stmt_block ;

else_stmt        : ELSE stmtblock=stmt_block ;

stmt_block       : st_stmt+ ;

case_stmt        : CASE expr=expression OF casesel=case_selections ( ELSE elsestmt=stmt_block )? END_CASE;
case_selections  : case_selection+ ;
case_selection   : case_list ':' stmt_block;
case_list        : case_list_elem ( ',' case_list_elem )*;
case_list_elem   : start=signed_int '..' to=signed_int                                        # caseRange
                 | expression                                                                 # caseExpression
                 ;
iteration_stmt   : for_stmt | while_stmt | repeat_stmt | EXIT | CONTINUE;
for_stmt         : FOR control_variable ':=' for_list DO st_stmt* END_FOR;
control_variable : IDENTIFIER;
for_list         : expression TO expression ( BY expression )?;
while_stmt       : WHILE expr=expression DO stmtblock=stmt_block END_WHILE;
repeat_stmt      : REPEAT st_stmt* UNTIL expression END_REPEAT;

expression       : bool_expression
                 | term_expression
                 ;

bool_expression  : bool_expression op=( AND | OR | XOR ) bool_expression                      # binaryBoolExpression
                 | term_expression op=( '>=' | '<=' | '=' | '<' | '>' | '<>' ) 
                   term_expression                                                            # binaryBoolExpression
                 | NOT bool_expression                                                        # unaryBoolExpression
                 | conversion_function '(' term_expression ')'                                # callBoolExpression
                 | leaf_expression                                                            # leafBoolExpression
                 | '(' subexpr=bool_expression ')'                                            # parBoolExpression
                 ;

term_expression  : term_expression op=( '*' | '/' | MOD ) term_expression                     # binaryTermExpression
                 | term_expression op=( '+' | '-' ) term_expression                           # binaryTermExpression
                 | '-' term_expression                                                        # unaryTermExpression
                 | conversion_function '(' (bool_expression | term_expression) ')'            # callTermExpression
                 | std_func_name '(' (bool_expression | term_expression) ')'                  # callTermExpression
                 | custom_func_name '(' (func_param_init ','?)* ')'                           # customCallExpression
                 | leaf_expression                                                            # leafTermExpression
                 | '(' subexpr=term_expression ')'                                            # parTermExpression
                 ;

func_param_init : variable_name ':=' (variable_name | constant)
                ;
        
leaf_expression  : simple_var
                 | array_access
                 | composite_access
                 | constant
                 ;

/*****************************************************************************************************************
 * NUMBER SECTION
 ****************************************************************************************************************/
                    
constant         : numeric_literal | time_literal | bool_literal;
numeric_literal  : int_literal | real_literal;
int_literal      : ( ( INT | SINT | DINT ) '#' )?
                   ( signed_int | BINARY_INT | OCTAL_INT | HEX_INT );
uns_int          : DIGITS ( '_' ? DIGITS )*;
signed_int       : op=( '+' | '-' )? uns_int;
real_literal     : ( REAL | LREAL '#' )? signed_int '.' uns_int ( 'E' signed_int )?;
bool_literal     : ( BOOL '#' )? ( FALSE | TRUE );
time_literal     : TIME_MS | TIME_S ;

/*****************************************************************************************************************
 * MISC SECTION
 ****************************************************************************************************************/

variable_name       : IDENTIFIER;

custom_func_name    : IDENTIFIER;

simple_var          : variable_name;

array_access        : variable_name '[' term_expression ']' ;

composite_access    : ((variable_name | array_access) '.')+ (variable_name | array_access) ;

variable_bit_access : variable_name '.' uns_int ;

conversion_function : UINT_TO_WORD | UINT_TO_BOOL | UINT_TO_USINT
                    | UINT_TO_INT | UINT_TO_REAL | DINT_TO_UDINT | DINT_TO_UINT
                    | INT_TO_REAL | INT_TO_UINT | INT_TO_USINT | INT_TO_BOOL
                    | INT_TO_WORD | REAL_TO_INT | REAL_TO_UINT | BOOL_TO_INT
                    | WORD_TO_UINT | WORD_TO_BYTE | WORD_TO_INT
                    | USINT_TO_UINT | USINT_TO_BYTE | BYTE_TO_WORD
                    | BYTE_TO_UINT | BYTE_TO_USINT | UDINT_TO_DINT | UINT_TO_DINT
                    | USINT_TO_DINT | DINT_TO_USINT | USINT_TO_UDINT | UDINT_TO_USINT
                    ;

std_func_name    : TRUNC | ABS | SQRT | LN | LOG | EXP
                 | SIN | COS | TAN | ASIN | ACOS | ATAN | ATAN2
                 | ADD | SUB | MUL | DIV | MOD | EXPT | MOVE
                 | SHL | SHR | ROL | ROR
                 | AND | OR | XOR | NOT
                 | SEL | MAX | MIN | LIMIT | MUX
                 | GT | GE | EQ | LE | LT | NE
                 | LEN | LEFT | RIGHT | MID | CONCAT 
                 | INSERT | DELETE | REPLACE | FIND
                 ;
