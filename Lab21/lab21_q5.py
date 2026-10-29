# find sum of elements in a list using lambda and reduce functions
from functools import reduce

print(reduce(lambda x,y: int(x)+int(y), input("Enter elements of list: ").split()))