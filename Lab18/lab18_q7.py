#find type of triangle
def type (a,b,c):
    if a==b and b==c: print("It is an equilateral triangle")
    elif a!=b and b!=c and c!=a: print("It is a scalene triangle")
    else: print("It is an isosceles triangle")

type(1,2,3)
