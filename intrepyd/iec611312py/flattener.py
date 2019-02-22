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
from intrepyd.iec611312py.summarizer import Summarizer
from intrepyd.iec611312py.expression import VariableOcc, TRUE

class Flattener(object):
    def __init__(self):
        self._summarizer = Summarizer()

    def flattenStmtBlock(self, block):
        rewritten_stmt_block = self.flattenStmtBlockImpl(block)
        normal_assignments = self._summarizer.summarizeStmtBlock(rewritten_stmt_block)
        extra_assignments = self._summarizer._assignments
        return extra_assignments + normal_assignments

    def flattenStmtBlockImpl(self, block):
        rewritten_stmt_block = []
        for instr in block:
            flattened_instruction = self.flattenInstruction(instr)
            for flat_instr in flattened_instruction:
                rewritten_stmt_block.append(flat_instr)
        return self._summarizer.summarizeStmtBlock(rewritten_stmt_block)

    def flattenCase(self, instruction):
        if not isinstance(instruction, Case):
            raise RuntimeError('Instruction is not of type Case')
        expression = instruction.expression
        rewritten_stmt_blocks = []
        for block in instruction.stmt_blocks:
            rewritten_stmt_blocks.append(self.flattenStmtBlockImpl(block))
        lhss = collectLhss(rewritten_stmt_blocks)
        ites = []
        conditions = []
        for selection in instruction.selections:
            if len(selection) == 1:
                conditions.append(Expression('=', [expression, selection[0]]))
            else:
                cond_or = [Expression('=', [expression, sel]) for sel in selection]
                conditions.append(Expression('OR', cond_or))
        for lhs in lhss:
            lhsOcc = VariableOcc(lhs)
            ites.append(Assignment(lhsOcc, buildIte(lhsOcc, conditions, rewritten_stmt_blocks)))
        return ites   

    def flattenIfThenElse(self, instruction):
        if not isinstance(instruction, IfThenElse):
            raise RuntimeError('Instruction is not of type IfThenElse')
        conditions = instruction.conditions
        rewritten_stmt_blocks = []
        for block in instruction.stmt_blocks:
            rewritten_stmt_blocks.append(self.flattenStmtBlockImpl(block))
        lhss = collectLhss(rewritten_stmt_blocks)
        ites = []
        for lhs in lhss:
            lhsOcc = VariableOcc(lhs)
            ites.append(Assignment(lhsOcc, buildIte(lhsOcc, conditions, rewritten_stmt_blocks)))
        return ites   

    def flattenInstruction(self, instruction):
        if isinstance(instruction, Assignment):
            return [instruction]
        elif isinstance(instruction, Case):
            return self.flattenCase(instruction)
        elif isinstance(instruction, IfThenElse):
            return self.flattenIfThenElse(instruction)
        raise RuntimeError('Unexpected instruction type ' + str(type(instruction)))

def buildIte(varOcc, conditions, rewritten_stmt_blocks):
    result = varOcc
    length = len(conditions)
    for i in range(length - 1, -1, -1):
        rhs = findRhsFor(varOcc, rewritten_stmt_blocks[i])
        if conditions[i] == TRUE:
            result = rhs
        else:
            result = Ite(conditions[i], rhs, result)
    return result

def findRhsFor(varOcc, block):
    for assignment in block:
        if varOcc.var == assignment.lhs.var:
            return assignment.rhs
    return varOcc

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
