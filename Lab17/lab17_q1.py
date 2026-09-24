#script to convert binary to decimal

binary=input("Enter a binary number: ")
decimal=0
l=len(binary)
for i in range(l):
    digit=int(binary[i])
    n=l-i-1
    decimal+=digit*(2**n)
print(decimal)
