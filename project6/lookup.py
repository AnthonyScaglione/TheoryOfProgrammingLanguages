from lang import *

def lookup(id, stk):
    for scope in reversed(stk):
        if id in scope:
            return scope[id]
    return None

def typeRes(ts, stk):
    for s in ts:
        resolve(s, stk)

def type_resolve(t : Expr, stk : list = []):
    if type(t) is BoolType:
        return t
    if type(t) is IntType:
        return t

def resolve(e, stk = []):
    if type(e) is BoolExpr:
        return e

    if type(e) is AndExpr:
        resolve(e.lhs, stk)
        resolve(e.rhs, stk)
        return e

    if type(e) is OrExpr:
        resolve(e.lhs, stk)
        resolve(e.rhs, stk)
        return e

    if type(e) is NotExpr:
        resolve(e.expr, stk)
        return e

    if type(e) is IfExpr:
        resolve(e.cond, stk)
        resolve(e.true, stk)
        resolve(e.false, stk)
        return e

    if type(e) is IdExpr:
        decl = lookup(e.id, stk)
        if not decl:
            raise Exception("name lookup error")
        e.ref = decl
        return e

    if type(e) is AbsExpr:
        resolve(e.expr, stk + [{e.var.id : e.var}])
        return e

    if type(e) is BoolType:
        return e

    if type(e) is IntType:
        return e

    if type(e) is TupleType:
        type_resolve(e.vals, stk)
        return e

    if type(e) is StructType:
        resolve(e.name)
        resolve(e.contents)
        return e
