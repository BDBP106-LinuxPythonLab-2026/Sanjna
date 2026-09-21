x1=float(input("Enter x-coordinate of first point: "))
y1=float(input("Enter y-coordinate of first point: "))
x2=float(input("Enter x-coordinate of second point: "))
y2=float(input("Enter y-coordinate of second point: "))

import math
distance=math.sqrt(((x2-x1)**2)+((y2-y1)**2))

print ("The distance between the points is "+str(distance)+" units")