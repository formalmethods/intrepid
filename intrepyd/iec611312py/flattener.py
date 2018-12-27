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

def flattenStmtBlock(block):
    rewritten_stmt_block = []
    for instr in block:
        rewritten_stmt_block.append(flattenInstruction(instr))
    return rewritten_stmt_block

def flattenCase(instruction):
    if not isinstance(instruction, Case):
        raise RuntimeError('Instruction is not of type Case')
    raise NotImplementedError

def collectLhss(blocks):
    seen = set()
    for block in blocks:
        for instruction in block:
            if not isinstance(instruction, Assignment):
                raise RuntimeError('Expected Assignment, got ' + type(instruction))
            seen.add(instruction.lhs)
    return seen

def flattenIfThenElse(instruction):
    if not isinstance(instruction, IfThenElse):
        raise RuntimeError('Instruction is not of type IfThenElse')
    conditions = instruction.conditions
    rewritten_stmt_blocks = []
    for block in instruction.stmt_blocks:
        rewritten_stmt_blocks.append(flattenStmtBlock(block))
    lhs_set = collectLhss(rewritten_stmt_blocks)

def flattenInstruction(instruction):
    if isinstance(instruction, Assignment):
        return instruction
    elif isinstance(instruction, Case):
        return flattenCase(instruction)
    elif isinstance(instruction, IfThenElse):
        return flattenIfThenElse(instruction)
    raise RuntimeError('Unexpected instruction type ' + type(instruction))

