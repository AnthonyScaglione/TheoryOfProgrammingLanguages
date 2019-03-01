# import sys

# Expression Language (EL)

class Expr:

    # e ::= true
    #   false
    #   not e1
    #   e1 and e2
    #   e1 or e2

    #v ::= true
    #      false

    # e::= x
    #      x.e1
    #      e1 e2

    pass

# Boolean implementation for project 1

# Base boolean values
class BoolExpr(Expr):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return "true" if self.value else "false"

# not e
class NotExpr(Expr):
    # Represents strings in the form 'not e'
    def __init__(self, e):
        self.expr = e

    def __str__(self):
        return f"(not {self.expr})"

# e1 and e2
class AndExpr(Expr):
    def __init__(self, e1, e2):
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return f"({self.lhs} and {self.rhs})"

# e1 or e2
class OrExpr(Expr):
    def __init__(self, e1, e2):
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return f"({self.lhs} or {self.rhs})"

# return value recursively
def value(e):    
    if type(e) is BoolExpr:
        return e.val

    if type(e) is NotExpr:
        return not value(e.expr)

    if type(e) is AndExpr:
        return value(e.lhs) and value(e.rhs)
    
    if type(e) is OrExpr:
        return value(e.lhs) or value(e.rhs)

    assert False

# find size of tree
def size(e):
    if type(e) is BoolExpr:
        return 1

    if type(e) is NotExpr:
        return 1 + size(e.expr)

    if type(e) is AndExpr or type(e) is OrExpr:
        return 1 + size(e.lhs) + size(e.rhs)

    assert False

# find height of the tree
def height(e):

    if e is None:
        return 0

    if type(e) is BoolExpr:
        return 1

    if type(e) is NotExpr:
        return 1 + height(e.expr)

    if type(e) is AndExpr or type(e) is OrExpr:
        return 1 + max(height(e.lhs), height(e.rhs))

# test if two expressions are the same
def same(e1, e2):
    if type(e1) is not type(e2):
        return False

    if type(e1) is BoolExpr:
        return e1.value == e2.value

    if type(e1) is NotExpr:
        return same(e1.expr, e2.expr)

    if type(e1) is AndExpr:
        return same(e1.lhs, e2.lhs) and same(e1.rhs, e2.rhs)

    if type(e1) is OrExpr:
        return same(e1.lhs, e2.rhs) and same(e1.rhs, e2.rhs)

# step
def step(e):
    if(is_reducible(e)):
        if type(e) is BoolExpr:
            return e.val

        if type(e) is NotExpr:
            return step_not(e)

        if type(e) is AndExpr:
            return step_and(e)

        if type(e) is OrExpr:
            return step_or(e)

# step not expression
def step_not(e):
    if is_value(e):
        return BoolExpr(not e.val)
    else:
        return NotExpr(step(e.expr))

# step and expression
def step_and(e):

    if is_value(e.lhs) and is_value(e.rhs):
        return BoolExpr(e.lhs.val and e.rhs.val)

    if is_reducible(e.lhs):
        return AndExpr(step(e.lhs), e.rhs)

    if is_reducible(e.rhs):
        return AndExpr(e.lhs, step(e.rhs))

    assert False

# step or expression
def step_or(e):

    if is_value(e.lhs) and is_value(e.rhs):
        return BoolExpr(e.lhs.val or e.rhs.val)

    if is_reducible(e.lhs):
        return OrExpr(step(e.lhs), e.rhs)

    if is_reducible(e.rhs):
        return OrExpr(e.lhs, step(e.rhs))

    assert False

# reduce fully
def reduce(e):
    while(is_reducible(e)):
        e = step(e)

    return e

# check if val
def is_value(e):
    return type(e) is BoolExpr

#check if expr
def is_reducible(e):
    return not is_value(e)

