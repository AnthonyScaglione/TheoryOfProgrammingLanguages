from lang import *

boolType = BoolType()
intType = IntType()

def check(e):
    return do_check(e) if not e.type else e.type

def do_check(e):
    if type(e) is BoolExpr:
        return check_bool(e)
    if type(e) is IntExpr:
        return check_int(e)
    if type(e) is AndExpr:
        return check_and(e)
    if type(e) is OrExpr:
        return check_or(e)
    if type(e) is NotExpr:
        return check_not(e)
    if type(e) is IfExpr:
        return check_if(e)
    if type(e) is AddExpr:
        return check_add(e)
    if type(e) is SubExpr:
        return check_sub(e)
    if type(e) is MulExpr:
        return check_mul(e)
    if type(e) is DivExpr:
        return check_div(e)
    if type(e) is ModExpr:
        return check_mod(e)
    if type(e) is NegExpr:
        return check_neg(e)
    if type(e) is EqExpr:
        return check_eq(e)
    if type(e) is NeExpr:
        return check_ne(e)
    if type(e) is LtExpr:
        return check_lt(e)
    if type(e) is GtExpr:
        return check_gt(e)
    if type(e) is LeExpr:
        return check_le(e)
    if type(e) is GeExpr:
        return check_ge(e)
    if type(e) is TupleExpr:
        return check_tuple(e)
    if type(e) is RecordExpr:
        return check_record(e)
    if type(e) is VariantExpr:
        return check_variant(e)
    assert False

def is_bool(x):
    return x == boolType if isinstance(x, Type) else is_bool(check(x))

def is_int(x):
    return x == intType if isinstance(x, Type) else is_int(check(x))

def is_same_type(t1, t2):
    if type(t1) is not type(t2):
        return False
    elif type(t1) is BoolType:
        return True
    elif type(t1) is IntType:
        return True

def has_same_type(e1, e2):
    return is_same_type(check(e1), check(e2))

def check_bool(e):
    return boolType

def check_int(e):
    return intType

# Checking boolean operations

def check_booltype(e, sym):
    if is_bool(e.lhs) and is_bool(e.rhs):
        return boolType
    raise Excepttion(f"invalid operands to '{sym}'")

def check_and(e):
    return check_booltype(e, "and")

def check_or(e):
    return check_booltype(e, "or")

def check_not(e):
    if is_bool(e.expr):
        return boolType
    raise Exception("invalid operands to 'not'")

def check_if(e):
    if type(check(e.eif)) is type(check(e.eelse)):
        return boolType
    raise Exception("invalid operands to 'if'")

# checking numerical operators

def check_inttype(e, sym):
    if is_int(e.lhs) and is_int(e.rhs):
        return intType
    raise Exception(f"invalid operands to '{sym}'")

def check_add(e):
    return check_inttype(e, "+")

def check_sub(e):
    return check_inttype(e, "-")

def check_mul(e):
    return check_inttype(e, "*")

def check_div(e):
    return check_inttype(e, "/")

def check_neg(e):
    if is_int(e1):
        return intType
    raise Exception("invalid operands to '-'")

def check_mod(e):
    return check_inttype(e, "%")

# checking relational operators

def check_relational(e, sym):
    if is_int(e.lhs) and is_int(e.rhs):
        return boolType
    raise Exception(f"invalid operands to '{sym}'")

def check_eq(e):
    return check_relational(e, "==")

def check_ne(e):
    return check_relational(e, "!=")

def check_lt(e):
    return check_relational(e, "<")

def check_gt(e):
    return check_relational(e, ">")

def check_le(e):
    return check_relational(e, "<=")

def check_ge(e):
    return check_relational(e, ">=")

# checking equal operator

def check_eq(e):
    if is_same_type(check(e.lhs), check(e.rhs)):
        return boolType
    raise Exception("invalid operands to '=='")

def check_tuple(e):
    return TupleType

def check_record(e):
    return RecordType

def check_variant(e):
    return VariantType
