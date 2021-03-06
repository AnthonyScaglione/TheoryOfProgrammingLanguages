class Type:
      pass

class BoolType(Type):
    def __str__(self):
        return "Bool"

class IntType(Type):
    def __str__(self):
        return "Int"

boolType = BoolType()
intType = IntType()

class Expr:
    def __init__(self):
        self.type = None

# Boolean Expressions

class BoolExpr(Expr):
    def __init__(self, val):
        Expr.__init__(self)
        self.value = val

    def __str__(self):
        return "true" if self.value else "false"

class AndExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)
    def __str__(self):
        return f"({self.lhs} and {self.rhs})"

class OrExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} or {self.rhs})"

class NotExpr(Expr):
    def __init__(self, e):
        Expr.__init__(self)
        self.expr = expr(e)

    def __str__(self):
        return f"(not {self.expr})"

class IfExpr(Expr):
    def __init__(self, econ, eif, eelse):
        Expr.__init__(self)
        self.cond = expr(econ)
        self.true = expr(eif)
        self.false = expr(eElse)

    def __str__(self):
        return f"(if {self.cond} then {self.true} else {self.false})"

# Integer expressions

class IntExpr(Expr):
    def __init__(self, val):
        Expr.__init__(self)
        self.value = val

    def __str__(self):
        return str(self.value)

class AddExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} + {self.rhs})"

class SubExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} + {self.rhs})"

class MulExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} - {self.rhs})"

class DivExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} / {self.rhs})"

class ModExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} % {self.rhs})"

class NegExpr(Expr):
    def __init__(self, e1):
        Expr.__init__(self)
        self.expr = expr(e1)

    def __str__(self):
        return f"(-{self.expr})"

# Relational expressions

class EqExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} == {self.rhs})"

class NeExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} != {self.rhs})"

class LtExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} < {self.rhs})"

class GtExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} > {self.rhs})"

class LeExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} <= {self.rhs})"

class GeExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} >= {self.rhs})"

def expr(x):
    if type(x) is bool:
        return BoolExpr(x)
    elif type(x) is int:
        return IntExpr(x)
    elif type(x) is str:
        return IdExpr(x)
    return x

from check import check
from evaluate import evaluate
