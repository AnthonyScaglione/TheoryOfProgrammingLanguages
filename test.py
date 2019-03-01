from project3 import *

land = AbsExpr("q", AbsExpr("q", AppExpr(AppExpr(IdExpr("p"), IdExpr("q")), IdExpr("p"))))

id = AbsExpr(VarDecl("x"), IdExpr("x"))

print(land)
print(id)









