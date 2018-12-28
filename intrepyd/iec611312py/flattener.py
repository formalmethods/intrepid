"""
Copyright (C) 2018 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 24/12/2018

This module implements a flattener for ST terms
"""

from intrepyd.iec611312py.expression import Expression, Ite
from intrepyd.iec611312py.statement import IfThenElse, Case, Assignment
from intrepyd.iec611312py.summarizer import summarizeStmtBlock
from intrepyd.iec611312py.expression import VariableOcc, TRUE
from intrepyd.iec611312py.stmtprinter import StmtPrinter

def flattenStmtBlock(block):
    rewritten_stmt_block = []
    for instr in block:
        flattened_instruction = flattenInstruction(instr)
        for flat_instr in flattened_instruction:
            rewritten_stmt_block.append(flat_instr)

    # printer = StmtPrinter()
    # printer.processStatements(rewritten_stmt_block)
    # print 'RSB:', printer.result

    return summarizeStmtBlock(rewritten_stmt_block)

def flattenCase(instruction):
    if not isinstance(instruction, Case):
        raise RuntimeError('Instruction is not of type Case')
    raise NotImplementedError

def collectLhss(blocks):
    seen = set()
    lhss = []
    for block in blocks:
        for instruction in block:
            if not isinstance(instruction, Assignment):
                raise RuntimeError('Expected Assignment, got ' + str(type(instruction)))
            if not instruction.lhs.var in seen:
                seen.add(instruction.lhs.var)
                lhss.append(instruction.lhs.var)
    return lhss

def flattenIfThenElse(instruction):
    if not isinstance(instruction, IfThenElse):
        raise RuntimeError('Instruction is not of type IfThenElse')
    conditions = instruction.conditions
    rewritten_stmt_blocks = []
    for block in instruction.stmt_blocks:
        rewritten_stmt_blocks.append(flattenStmtBlock(block))
    lhss = collectLhss(rewritten_stmt_blocks)
    ites = []
    for lhs in lhss:
        lhsOcc = VariableOcc(lhs)
        ites.append(Assignment(lhsOcc, buildIte(lhsOcc, conditions, rewritten_stmt_blocks)))
    return ites   

def buildIte(varOcc, conditions, rewritten_stmt_blocks):
    # print 'BUILDING ITE'
    # for rsb in rewritten_stmt_blocks:
    #     printer = StmtPrinter()
    #     printer.processStatements(rsb)
    #     print 'RSB:', printer.result
    result = varOcc
    length = len(conditions)
    # print 'LENGTH:', length
    for i in range(length - 1, -1, -1):
        rhs = findRhsFor(varOcc, rewritten_stmt_blocks[i])
        if conditions[i] == TRUE:
            result = rhs
        else:
            result = Ite(conditions[i], rhs, result)
        # printer = StmtPrinter()
        # printer.processStatements([result])
        # print 'CURRENT ITE:', printer.result
    return result

def findRhsFor(varOcc, block):
    for assignment in block:
        if varOcc.var == assignment.lhs.var:
            return assignment.rhs
    return varOcc

def flattenInstruction(instruction):
    if isinstance(instruction, Assignment):
        return [instruction]
    elif isinstance(instruction, Case):
        return flattenCase(instruction)
    elif isinstance(instruction, IfThenElse):
        return flattenIfThenElse(instruction)
    raise RuntimeError('Unexpected instruction type ' + str(type(instruction)))
