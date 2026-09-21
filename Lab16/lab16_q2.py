p=float(input("Enter principal amount: "))
r=float(input("Enter the rate of interest in percentage per annum: "))
t=int(input("Enter the time in years: "))

import math
i= (p*r*t)/100
total= p+i
print("The simple interest calculated is "+str(i)+"")
print("The total amount at the end of "+str(t)+" is "+str(total)+"")
