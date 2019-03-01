
# Project 3 lambda expressions

class Expr:
    pass

class IdExpr(Expr):
    '''Represents identifiers'''
    def __init__(self, id):
        self.id = id
        self.ref = None

    def __str__(self):
        return self.id

# represents variable declaration
class VarDecl(Expr):
    def __init__(self, id):
        self.id = id
    def __str__(self):
        return self.id

# represents lambda abstractions
class AbsExpr(Expr):
    def __init__(self, var, e1):
        self. var = VarDecl(var) if type(var) is str else var
        self.expr = e1

    def __str__(self):
        return f"\\{self.var}.{self.expr}"

# represents application
class AppExpr(Expr):
  	def __init__(self, lhs, rhs):
  		self.lhs = lhs
  		self.rhs = rhs

  	def __str__(self):
  		return f"({self.lhs} {self.rhs})"

# check if expr
def is_reducible(e):
    return not type(e) is IdExpr or type(e) is AbsExpr

# resolve recursively
def resolve(e, s = []):
    if type(e) is AppExpr:
        resolve(e.lhs, s)
        resolve(e.rhs, s)
        return

    if type(e) is AbsExpr:
        resolve(e.expr, s + e.var)
        return

    if type(e) is IdExpr:
        for var in s[::-1]:
            if e.id == var.id: 
                e.ref = var 
                return

    assert False

# substitute
def subst(e, s):
    if type(e) is IdExpr:
        return s[e.ref] if e.ref in s else e

    if type(e) is AbsExpr:
        return AbsExpr(e.var, subst(e.expr, s))

    if type(e) is AppExpr:
        return AppExpr(subst(e.lhs, s), subst(e.rhs), s)

    assert(False)

# step application
def step_app(e):
    if is_reducible(e.lhs):
        return AppExpr(step(e.lhs), e.rhs)

    if is_reducible(e.rhs):
        return AppExpr(e.lhs, step(e.rhs))

    s = {e.lhs.var: e.rhs}

    return subst(e.lhs.expr, s)

def step(e):
    if type(e) is AppExpr:
        return step_app(e)

    assert False

