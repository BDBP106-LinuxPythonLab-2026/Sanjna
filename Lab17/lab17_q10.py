#find even numbers in a list
s=input("Enter numbers: ")
L=s.split( )
print(L)
print("The following numbers are even:")
for n in L:
    if int(n)%2==0: print(n, end=" ")
