
from lang import *
import copy

a = TupleExpr([BoolExpr(True), BoolExpr(True)])
b = TupleExpr([IntExpr(4), BoolExpr(False)])
c = RecordExpr({"first":a, "second":IntExpr(51)})
d = VariantExpr("first", {"second":BoolExpr(False), "third":BoolExpr(False)})

print(a)
print(b)
print(c)
print(d)
