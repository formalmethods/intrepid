"""
This module implements type inference for expressions
"""

import re
from intrepyd.iec611312py.visitor import Visitor
from intrepyd.iec611312py.datatype import Primitive, Datatype

boolType = Primitive('BOOL')

# Operators for which a type is known
OPSOFKNOWNTYPE = {
    '=' : boolType,
    '<>' : boolType,
    '<' : boolType,
    '>' : boolType,
    '<=' : boolType,
    '>=' : boolType,
    'OR' : boolType,
    'AND' : boolType,
    'XOR' : boolType,
    'NOT' : boolType
}

# Father and children have all the same type
OPSOFSAMETYPEASFATHER = {
    '-', '+', '*', '/'
}

OPSCHILDRENHAVESAMETYPE = OPSOFSAMETYPEASFATHER.copy()
OPSCHILDRENHAVESAMETYPE.update(set(OPSOFKNOWNTYPE.keys()))

def getConversionOperatorOutputType(operator):
    mobj = re.match('(.*)_TO_(.*)', operator)
    if not mobj:
        return None
    return Primitive(mobj.group(2))

def getConversionOperatorInputType(operator):
    mobj = re.match('(.*)_TO_(.*)', operator)
    if not mobj:
        return None
    return Primitive(mobj.group(1))


class InferDatatypeBottomUp(Visitor):
    """
    Visitor for inferring expressions datatype
    """
    def process_statements(self, statements):
        for statement in statements:
            statement.accept(self)

    def _visit_expression(self, expression):
        for arg in expression.arguments:
            arg.accept(self)
        if expression.operator in OPSOFKNOWNTYPE:
            expression.datatype = OPSOFKNOWNTYPE[expression.operator]
        elif expression.operator in OPSOFSAMETYPEASFATHER:
            for arg in expression.arguments:
                if not arg.datatype is None:
                    expression.datatype = arg.datatype
                    return
        else:
            datatype = getConversionOperatorOutputType(expression.operator)
            if not datatype is None:
                expression.datatype = datatype

    def _visit_ite(self, ite):
        ite.then_term.accept(self)
        ite.else_term.accept(self)
        ite.condition.accept(self)
        if not ite.then_term.datatype is None:
            ite.datatype = ite.then_term.datatype
        elif not ite.else_term.datatype is None:
            ite.datatype = ite.else_term.datatype

    def _visit_assignment(self, assignment):
        assignment.lhs.accept(self)
        assignment.rhs.accept(self)

    def _visit_variable_occ(self, variableOcc):
        variableOcc.datatype = variableOcc.var.datatype

    def _visit_constant_occ(self, constantOcc):
        pass

    def _visit_function_occ(self, functionOcc):
        functionOcc.datatype = Datatype.get(functionOcc.name)


class InferDatatypeTopDown(Visitor):
    """
    Visitor for inferring expressions datatype
    """
    def process_statements(self, statements):
        for statement in statements:
            statement.accept(self)

    def _visit_expression(self, expression):
        if not expression.datatype is None:
            if expression.operator in OPSOFSAMETYPEASFATHER:
                for arg in expression.arguments:
                    if arg.datatype is None:
                        arg.datatype = expression.datatype
                    elif arg.datatype != expression.datatype:
                        raise RuntimeError('Expression mismatch datatype: ' + arg.datatype.dtname + ' vs ' + expression.datatype.dtname)
        if expression.operator in OPSCHILDRENHAVESAMETYPE:
            commonType = None
            for arg in expression.arguments:
                if not arg.datatype is None:
                    if commonType is None:
                        commonType = arg.datatype
                    elif commonType != arg.datatype:
                        raise RuntimeError('Expression mismatch datatype')
            if commonType is None:
                raise RuntimeError('Cannot infer arguments datatypes')
            for arg in expression.arguments:
                if arg.datatype is None:
                    arg.datatype = commonType
        else:
            inputType = getConversionOperatorInputType(expression.operator)
            if not inputType is None:
                if expression.arguments[0].datatype is None:
                    expression.arguments[0].datatype = inputType
                elif expression.arguments[0].datatype != inputType:
                    raise RuntimeError('Expression mismatch datatype')
        for arg in expression.arguments:
            arg.accept(self)

    def _visit_ite(self, ite):
        # Shouldn't it be either None or BOOL ?
        if (not ite.condition.datatype is None) and ite.condition.datatype != Primitive('BOOL'):
            ite.condition.datatype = 'BOOL'
        if not ite.datatype is None:
            if ite.then_term.datatype is None:
                ite.then_term.datatype = ite.datatype
            if ite.else_term.datatype is None:
                ite.else_term.datatype = ite.datatype
            if ite.then_term.datatype != ite.datatype or ite.else_term.datatype != ite.datatype:
                raise RuntimeError('Ite datatypes mismatch')
        ite.then_term.accept(self)
        ite.else_term.accept(self)
        ite.condition.accept(self)

    def _visit_assignment(self, assignment):
        if assignment.rhs.datatype is None:
            if assignment.lhs.datatype is None:
                raise RuntimeError('Assignment lhs has no datatype')
            assignment.rhs.datatype = assignment.lhs.datatype
            assignment.rhs.accept(self)
        elif assignment.rhs.datatype != assignment.lhs.datatype:
            raise RuntimeError('Assignment datatypes mismatch: ' +\
                               assignment.lhs.datatype.dtname +\
                               ' vs ' +\
                               assignment.rhs.datatype.dtname)
        else:
            assignment.rhs.accept(self)

    def _visit_variable_occ(self, variableOcc):
        pass

    def _visit_constant_occ(self, constantOcc):
        pass

    def _visit_function_occ(self, functionOcc):
        pass

