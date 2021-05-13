"""
This module implements a flattener for ST terms
"""

from intrepyd.iec611312py.expression import Expression, Ite
from intrepyd.iec611312py.statement import IfThenElse, Case, Assignment
from intrepyd.iec611312py.summarizer import Summarizer
from intrepyd.iec611312py.expression import VariableOcc, TRUE

class Flattener(object):
    """
    Flattens statements
    """
    def __init__(self):
        self._summarizer = Summarizer()

    def flatten_stmt_block(self, block):
        rewritten_stmt_block = self.flatten_stmt_block_impl(block)
        normal_assignments = self._summarizer.summarize_stmt_block(rewritten_stmt_block)
        extra_assignments = self._summarizer._assignments
        return extra_assignments + normal_assignments

    def flatten_stmt_block_impl(self, block):
        rewritten_stmt_block = []
        for instr in block:
            flattened_instruction = self.flatten_instruction(instr)
            for flat_instr in flattened_instruction:
                rewritten_stmt_block.append(flat_instr)
        return self._summarizer.summarize_stmt_block(rewritten_stmt_block)

    def flatten_case(self, instruction):
        if not isinstance(instruction, Case):
            raise RuntimeError('Instruction is not of type Case')
        expression = instruction.expression
        rewritten_stmt_blocks = []
        for block in instruction.stmt_blocks:
            rewritten_stmt_blocks.append(self.flatten_stmt_block_impl(block))
        lhss = collect_lhss(rewritten_stmt_blocks)
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
            ites.append(Assignment(lhsOcc, build_ite(lhsOcc, conditions, rewritten_stmt_blocks)))
        return ites

    def flatten_if_then_else(self, instruction):
        if not isinstance(instruction, IfThenElse):
            raise RuntimeError('Instruction is not of type IfThenElse')
        conditions = instruction.conditions
        rewritten_stmt_blocks = []
        for block in instruction.stmt_blocks:
            rewritten_stmt_blocks.append(self.flatten_stmt_block_impl(block))
        lhss = collect_lhss(rewritten_stmt_blocks)
        ites = []
        for lhs in lhss:
            lhsOcc = VariableOcc(lhs)
            ites.append(Assignment(lhsOcc, build_ite(lhsOcc, conditions, rewritten_stmt_blocks)))
        return ites

    def flatten_instruction(self, instruction):
        if isinstance(instruction, Assignment):
            return [instruction]
        if isinstance(instruction, Case):
            return self.flatten_case(instruction)
        if isinstance(instruction, IfThenElse):
            return self.flatten_if_then_else(instruction)
        raise RuntimeError('Unexpected instruction type ' + str(type(instruction)))

def build_ite(varOcc, conditions, rewritten_stmt_blocks):
    result = varOcc
    length = len(conditions)
    for i in range(length - 1, -1, -1):
        rhs = find_rhs_for(varOcc, rewritten_stmt_blocks[i])
        if conditions[i] == TRUE:
            result = rhs
        else:
            result = Ite(conditions[i], rhs, result)
    return result

def find_rhs_for(varOcc, block):
    for assignment in block:
        if varOcc.var == assignment.lhs.var:
            return assignment.rhs
    return varOcc

def collect_lhss(blocks):
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
