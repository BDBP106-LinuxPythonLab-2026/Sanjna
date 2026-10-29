#function to calculate the area of a triangle
import math
def area (a,b,c):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of the triangle is", area, "square units")
a=int(input("Enter length of a: "))
b=int(input("Enter length of b: "))
c=int(input("Enter length of c: "))
area(a,b,c)