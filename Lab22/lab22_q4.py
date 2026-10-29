#Write a decorator called check_positive that checks whether the argument passed to
#a function is positive. If it is positive, execute the function; otherwise, print
#"Number must be positive".
import math
def check_positive(func):
    def wrapper(n):
        if n>0:
            return func(n)
        print("Number must be positive!")
    return wrapper

@check_positive
def fact(n):
    return math.factorial(n)

n = int(input("Enter a number: "))
result = fact(n)
if result is not None:
    print(f"The result of {n}! is {result}")