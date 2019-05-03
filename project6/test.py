from lang import *
from lookup import *
import copy

clone = copy.deepcopy

a = resolve(IntType())
b = resolve(BoolType())
c = resolve(TupleType([BoolType,IntType()]))

print(a)
print(b)
print(c)
