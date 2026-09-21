a=float(input("Enter coefficient of x^2:"))
b=float(input("Enter coefficient of x:"))
c=float(input("Enter constant:"))

import math
if (b**2)>=(4*a*c):
    print("The determinant is "+str(math.sqrt((b**2)-(4*a*c)))+" ")
    print("Roots of the quadratic equation are: "+str((-b+d)/(2*a))+" and "+str((-b-d)/(2*a))+" . ")
else: print ("Error: Complex root")