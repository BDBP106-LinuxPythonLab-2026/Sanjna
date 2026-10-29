import math, time

def measure_time(func):
    def wrapper(*args, **kwargs):
        begin=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        print("Time taken is: ", end-begin, "seconds.")
        return result
    return wrapper

@measure_time
def population_growth(i,r,t):
    def exponential_growth():
        return i*((math.e)**(r*t))
    for _ in range(1000000):
        n = exponential_growth()
    print(f"The population after time {t} is {round(n)}")

i=int(input("Enter initial population: "))
r=float(input("Enter rate of population growth: "))
t=int(input("Enter time period: "))

population_growth(i, r, t)

