# convert a tuple of angles into a list of tuples with each tuple containing the sine and cosine of an angle

#long format
import math
angle=(0,30,45,60,90)
def f(angle):
    x=math.sin(math.radians(angle))
    y=math.cos(math.radians(angle))
    return (x,y)

print(list(map(f,angle)))

#using lambda expression
print(list(map(lambda angle: (math.sin(math.radians(angle)),math.cos(math.radians(angle))),angle)))

