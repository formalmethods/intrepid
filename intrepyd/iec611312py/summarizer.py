"""
Copyright (C) 2018 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/12/2018

This module implements a summarizer for ST assignments
"""

from intrepyd.iec611312py.expression import Expression, VariableOcc, ConstantOcc, Ite
from intrepyd.iec611312py.statement import Assignment
from intrepyd.iec611312py.variable import Variable
from collections import OrderedDict
from intrepyd.iec611312py.stmtprinter import termAsString

class Summarizer(object):
    def __init__(self):
        self._count = 0
        self._assignments = []

    @property
    def assignments(self):
        return self._assignments

    def getTmpVarFromVar(self, var):
        self._count += 1
        return VariableOcc(Variable(var.name + '___' + str(self._count), var.datatype, Variable.TEMP))

    def summarizeStmtBlock(block, assignments):
        summary = OrderedDict()
        for assignment in block:
            if not isinstance(assignment, Assignment):
                raise RuntimeError('A non-assignment instruction was detected ' + str(type(assignment)))
            newRhs = substitute(assignment.rhs, summary, assignments)
            print 'Summarized %d / %d' % (len(summary) + 1, len(block))
            summary[assignment.lhs.var] = newRhs
        return [Assignment(VariableOcc(lhs), rhs) for lhs, rhs in summary.iteritems()]

    def substituteInTerm(var, expression, term, assignments):
        result = None
        if isinstance(term, Expression):
            new_arguments = []
            for argument in term.arguments:
                new_arguments.append(substituteInTerm(var, expression, argument))
            result = Expression(term.operator, new_arguments)
        elif isinstance(term, Ite):
            i = substituteInTerm(var, expression, term.condition)
            t = substituteInTerm(var, expression, term.then_term)
            e = substituteInTerm(var, expression, term.else_term)
            result = Ite(i, t, e)
        elif isinstance(term, ConstantOcc):
            result = term
        elif isinstance(term, VariableOcc):
            if var == term.var:
                result = getTmpVarFromVar(var)
                self._assignments.append(Assignment(result, expression))
            else:
                result = term
        else:
            raise NotImplementedError('Term not handled %s' % type(term))
        return result

    def substitute(rhs, summary, assignments):
        result = rhs
        for key, value in summary.iteritems():
            result = substituteInTerm(key, value, result, assignments)
        return result
