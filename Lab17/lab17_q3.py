# check if a number is prime
n=int(input("Enter a number: "))
isPrime=True
if n<=1: isPrime=False
for divisor in range (2,int(n/2)+1):
    if n%divisor==0:
        isPrime=False
        break

if isPrime: print("The number", n, "is a prime number.")
else: print("The number", n, "is not a prime number")