"""
This module implements the main parsing routine of Lustre files
"""

from intrepyd.lustre2py.LustreVisitor import LustreVisitor
from intrepyd.lustre2py.node import Node
from intrepyd.lustre2py.expression import LiteralExpression, ZeroaryExpression,\
                                          UnaryExpression, BinaryExpression, InitCurrExpression,\
                                          ITEExpression, Expression, CallExpression,\
                                          TupleExpression
from intrepyd.lustre2py.variable import VarDeclGroup
from intrepyd.lustre2py.instruction import Equation
from intrepyd.lustre2py.datatype import Primitive

class ASTBuilder(LustreVisitor):
    """
    Vistor that builds the internal AST for the
    Lustre program
    """
    def __init__(self):
        self._nodes = []
        self._current_node = None

    @property
    def nodes(self):
        """
        Getter
        """
        return self._nodes

    def visitNode(self, ctx):
        new_node = Node(ctx.getChild(1).getText())
        self._current_node = new_node
        if not ctx.inp is None:
            lst = ctx.inp.accept(self)
            for decl in lst:
                new_node.add_input_decl(decl)
        if not ctx.outp is None:
            lst = ctx.outp.accept(self)
            for decl in lst:
                new_node.add_output_decl(decl)
        if not ctx.local is None:
            lst = ctx.local.accept(self)
            for decl in lst:
                new_node.add_local_decl(decl)
        if not ctx.instrlst is None:
            ctx.instrlst.accept(self)
        self._nodes.append(new_node)
        self._current_node = None

    def visitVarDeclList(self, ctx):
        return [ctx.getChild(i).accept(self) for i in range(0, ctx.getChildCount(), 2)]

    def visitVarDeclGroup(self, ctx):
        var_list = [ctx.getChild(i).accept(self) for i in range(0, ctx.getChildCount() - 2, 2)]
        datatype = ctx.getChild(ctx.getChildCount() - 1).accept(self)
        return VarDeclGroup(var_list, datatype)

    def visitInitCurrExpr(self, ctx):
        init = ctx.getChild(0).accept(self)
        curr = ctx.getChild(2).accept(self)
        return InitCurrExpression(init, curr)

    def visitNotExpr(self, ctx):
        arg = ctx.getChild(1).accept(self)
        return UnaryExpression('not', arg)

    def visitNegateExpr(self, ctx):
        arg = ctx.getChild(1).accept(self)
        return UnaryExpression('-', arg)

    def visitPreExpr(self, ctx):
        arg = ctx.getChild(1).accept(self)
        return UnaryExpression('pre', arg)

    def visitBinaryExpr(self, ctx):
        left = ctx.getChild(0).accept(self)
        right = ctx.getChild(2).accept(self)
        return BinaryExpression(ctx.op.text, left, right)

    def visitIfThenElseExpr(self, ctx):
        if_ = ctx.getChild(1).accept(self)
        then_ = ctx.getChild(3).accept(self)
        else_ = ctx.getChild(5).accept(self)
        return ITEExpression(if_, then_, else_)

    def visitIdExpr(self, ctx):
        return ZeroaryExpression(ctx.getText())

    def visitIntExpr(self, ctx):
        return LiteralExpression(ctx.getText(), Expression.INT)

    def visitRealExpr(self, ctx):
        return LiteralExpression(ctx.getText(), Expression.REAL)

    def visitBoolExpr(self, ctx):
        return LiteralExpression(ctx.getText(), Expression.BOOL)

    def visitTupleExpr(self, ctx):
        expressions = [ctx.getChild(i).accept(self)\
                        for i in range(1, ctx.getChildCount() - 1, 2)]
        return TupleExpression(expressions)

    def visitEquation(self, ctx):
        lhs = None
        if not ctx.pos1 is None:
            lhs = ctx.pos1.accept(self)
        if not ctx.pos2 is None:
            lhs = ctx.pos2.accept(self)
        expr = ctx.pos3.accept(self)
        self._current_node.add_equation(Equation(lhs, expr))

    def visitLhs(self, ctx):
        return [ctx.getChild(i).accept(self) for i in range(0, ctx.getChildCount(), 2)]

    def visitNodeCallExpr(self, ctx):
        cid = ctx.getChild(0).getText()
        params = [ctx.getChild(i).accept(self)\
                        for i in range(2, ctx.getChildCount() - 1, 2)]
        return CallExpression(cid, params)

    def visitProp(self, ctx):
        self._current_node.add_property(ctx.getChild(1).accept(self))

    def visitMain(self, ctx):
        self._current_node.main = True

    def visitBaseEID(self, ctx):
        return ctx.getText()

    def visitArrayEID(self, ctx):
        raise NotImplementedError

    def visitRecordEID(self, ctx):
        raise NotImplementedError

    def visitAssertion(self, ctx):
        raise NotImplementedError

    def visitIvc(self, ctx):
        raise NotImplementedError

    def visitRealizabilityInputs(self, ctx):
        raise NotImplementedError

    def visitCondactExpr(self, ctx):
        raise NotImplementedError

    def visitCastExpr(self, ctx):
        raise NotImplementedError

    def visitRecordExpr(self, ctx):
        raise NotImplementedError

    def visitArrayExpr(self, ctx):
        raise NotImplementedError

    def visitArrayAccessExpr(self, ctx):
        raise NotImplementedError

    def visitRecordAccessExpr(self, ctx):
        raise NotImplementedError

    def visitPrimitiveType(self, ctx):
        return Primitive(ctx.getChild(0).getText())

    def visitSubrangeType(self, ctx):
        raise NotImplementedError

    def visitArrayType(self, ctx):
        raise NotImplementedError

    def visitUserType(self, ctx):
        raise NotImplementedError

    def visitRecordType(self, ctx):
        raise NotImplementedError

    def visitEnumType(self, ctx):
        raise NotImplementedError
