a= float(input("Enter a real number: "))
b= float(input("Enter another real number: "))
c= float(input("Enter another real number: "))

import math
d= math.sqrt((b**2)-(4*a*c))
print("The determinant is "+str(d)+" ")
print("Roots of the quadratic equation are: "+str((-b+d)/(2*a))+" "+str((-b-d)/(2*a))+" ")
