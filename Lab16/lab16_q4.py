degree=float(input("Enter an angle in degrees: "))

import math
rad=math.radians(degree)



print ("The value of sin "+str(degree)+" is "+str(math.sin(rad))+"")
print ("The value of cos "+str(degree)+" is "+str(math.cos(rad))+"")
print ("The value of tan "+str(degree)+" is "+str(math.tan(rad))+"")
print ("The value of cosec "+str(degree)+" is "+str(1/(math.sin(rad)))+"")
print ("The value of sec "+str(degree)+" is "+str(1/(math.cos(rad)))+"")
print ("The value of cot "+str(degree)+" is "+str(1/(math.tan(rad)))+"")

