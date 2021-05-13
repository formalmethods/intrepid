"""
This module implements infrastructure to store expressions
"""

from intrepyd.visitable import Visitable

class ExpressionBase(Visitable):
    """
    Base class for expressions
    """
    def __init__(self):
        self._datatype = None

    @property
    def datatype(self):
        """
        Return the datatype
        """
        return self._datatype

    @datatype.setter
    def datatype(self, x):
        """
        Sets the datatype
        """
        self._datatype = x

class VariableOcc(ExpressionBase):
    """
    Stores a variable occurrence
    """
    def __init__(self, var):
        ExpressionBase.__init__(self)
        self._var = var

    @property
    def var(self):
        """
        Getter
        """
        return self._var

class ConstantOcc(ExpressionBase):
    """
    Stores a constant occurrence
    """
    def __init__(self, cst):
        ExpressionBase.__init__(self)
        self._cst = cst

    @property
    def cst(self):
        """
        Getter
        """
        return self._cst

class Expression(ExpressionBase):
    """
    Base class for expressions
    """
    def __init__(self, operator, arguments):
        ExpressionBase.__init__(self)
        self._operator = operator
        self._arguments = arguments

    @property
    def operator(self):
        """
        Returns operator
        """
        return self._operator

    @property
    def arguments(self):
        """
        Returns arguments
        """
        return self._arguments

class Range(ExpressionBase):
    """
    A range
    """
    def __init__(self, first, last):
        ExpressionBase.__init__(self)
        if first > last:
            raise RuntimeError('From is greater than to in range expression')
        self._first = first
        self._last = last

class Ite(ExpressionBase):
    """
    Term If-then-else. This construct does not exist in ST language. It is used
    as intermediate step before translating into intrepyd
    """
    def __init__(self, condition, then_term, else_term):
        ExpressionBase.__init__(self)
        self._condition = condition
        self._then_term = then_term
        self._else_term = else_term

    @property
    def condition(self):
        """
        Return condition term
        """
        return self._condition

    @property
    def then_term(self):
        """
        Return then term
        """
        return self._then_term

    @property
    def else_term(self):
        """
        Return else term
        """
        return self._else_term

class FunctionOcc(ExpressionBase):
    """
    A function call occurrence
    """
    def __init__(self, name, param_inits):
        ExpressionBase.__init__(self)
        self._name = name
        self._param_inits = param_inits

    @property
    def name(self):
        """
        Return name
        """
        return self._name

    @property
    def param_inits(self):
        """
        Return param inits
        """
        return self._param_inits

class ParamInit(ExpressionBase):
    """
    Holds a parameter initialization for function calls
    """
    def __init__(self, lhs, rhs):
        ExpressionBase.__init__(self)
        self._lhs = lhs
        self._rhs = rhs

    @property
    def lhs(self):
        """
        Returns the lhs
        """
        return self._lhs

    @property
    def rhs(self):
        """
        Returns the rhs
        """
        return self._rhs

TRUE = ConstantOcc('TRUE')
FALSE = ConstantOcc('FALSE')
