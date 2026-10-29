#program to filter out the odd elements of the Fibonacci series

fib=[0,1]
i=1
for i in range(2,50):
    fib.append(fib[i-1]+fib[i-2])
print(fib)

print(list(filter(lambda x: x%2,fib)))