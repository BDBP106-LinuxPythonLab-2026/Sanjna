# Write a program to concatenate a list of strings to make a sentence using reduce function.

s_list=["This", "is", "a", "list", "of", "strings", "to", "be", "converted", "into", "a", "sentence."]
from functools import reduce
print(reduce(lambda x,y: x + " " + y, s_list))
