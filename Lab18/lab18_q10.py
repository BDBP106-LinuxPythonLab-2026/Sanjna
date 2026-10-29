#finding a prime number greater than n

def isPrime(n):
    i=n+1
    while i>n:
        for d in range(2, (i//2)+1):
            if i%d==0: break
        else: return i
        i+=1
print(isPrime(int(input("Enter a number: "))))