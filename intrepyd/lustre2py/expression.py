"""
This module implements infrastructure to store Lustre expressions
"""

from intrepyd.visitable import Visitable

class Expression(Visitable):
    """
    Abstract class for expressions
    """
    def __init__(self, kind):
        self._kind = kind

    @property
    def kind(self):
        """
        Getter
        """
        return self._kind

    INITCURR = 'INITCURR'
    LITERAL = 'LITERAL'
    ZEROARY = 'ZEROARY'
    UNARY = 'UNARY'
    BINARY = 'BINARY'
    CALL = 'CALL'
    TUPLE = 'TUPLE'
    ITE = 'ITE'

    INT = 'int'
    REAL = 'real'
    BOOL = 'bool'

class CallExpression(Expression):
    """
    Class for node calls
    """
    def __init__(self, cid, params):
        Expression.__init__(self, Expression.CALL)
        self._cid = cid
        self._params = params

    @property
    def cid(self):
        """
        Getter
        """
        return self._cid

    @property
    def params(self):
        """
        Getter
        """
        return self._params


class InitCurrExpression(Expression):
    """
    Class for init curr
    """
    def __init__(self, init, curr):
        Expression.__init__(self, Expression.INITCURR)
        self._init = init
        self._curr = curr

    @property
    def init(self):
        """
        Getter
        """
        return self._init

    @property
    def curr(self):
        """
        Getter
        """
        return self._curr

class LiteralExpression(Expression):
    """
    Class for numeric or boolean literals
    """
    def __init__(self, value, datatype):
        Expression.__init__(self, Expression.LITERAL)
        self._value = value
        self._datatype = datatype

    @property
    def value(self):
        """
        Getter
        """
        return self._value

    @property
    def datatype(self):
        """
        Getter
        """
        return self._datatype

class ZeroaryExpression(Expression):
    """
    Class for zero-arity functions
    """
    def __init__(self, name):
        Expression.__init__(self, Expression.ZEROARY)
        self._name = name

    @property
    def name(self):
        """
        Getter
        """
        return self._name

class UnaryExpression(Expression):
    """
    Class for unary functions
    """
    def __init__(self, operator, operand):
        Expression.__init__(self, Expression.UNARY)
        self._operator = operator
        self._operand = operand

    @property
    def operator(self):
        """
        Getter
        """
        return self._operator

    @property
    def operand(self):
        """
        Getter
        """
        return self._operand

class BinaryExpression(Expression):
    """
    Class for binary functions
    """
    def __init__(self, operator, left, right):
        Expression.__init__(self, Expression.BINARY)
        self._operator = operator
        self._left = left
        self._right = right

    @property
    def operator(self):
        """
        Getter
        """
        return self._operator


    @property
    def left(self):
        """
        Getter
        """
        return self._left

    @property
    def right(self):
        """
        Getter
        """
        return self._right

class ITEExpression(Expression):
    """
    Class for if then elses
    """
    def __init__(self, if_, then_, else_):
        Expression.__init__(self, Expression.ITE)
        self._if_ = if_
        self._then_ = then_
        self._else_ = else_

    @property
    def if_(self):
        """
        Getter
        """
        return self._if_

    @property
    def then_(self):
        """
        Getter
        """
        return self._then_

    @property
    def else_(self):
        """
        Getter
        """
        return self._else_


class TupleExpression(Expression):
    """
    Class for tuples
    """
    def __init__(self, expressions):
        Expression.__init__(self, Expression.TUPLE)
        self._expressions = expressions

    @property
    def expressions(self):
        """
        Getter
        """
        return self._expressions
