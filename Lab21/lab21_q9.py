#Write a function population_growth(initial,rate, time) that defines an inner func-
#tion exponential_growth() using the formula N(t) = N0 + exp(rate ∗ time) where N0
#represents the initial population and N(t) is population after time t. The inner function
#returns the population after time, and the outer function rounds and prints it.

import math
def population_growth(i,r,t):
    def exponential_growth():
        return i * math.exp(r * t)
    print(f"The population after time {t} is {round(exponential_growth())}")

population_growth(float(input("Enter initial population: ")), float(input("Enter rate of population growth: ")), float(input("Enter time period: ")))


# rounding off to how many decimal places