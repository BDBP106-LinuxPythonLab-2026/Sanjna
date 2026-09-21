a=float(input("Enter length of side of triangle: "))
b=float(input("Enter length of side of triangle: "))
c=float(input("Enter length of side of triangle: "))

if a==b or a==c or c==b: print ("It is an isosceles triangle")
if a!=b and b!=c and a!=c : print ("It is a scalene triangle")