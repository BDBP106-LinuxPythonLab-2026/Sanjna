#iterate over a dictionary and print the key value pairs
D=dict([])
n=int(input("Enter number of elements: "))
for i in range(0,n):
    i=input("Enter key: ")
    v=input("Enter value: ")
    D[i]=v
print(D)

for key,value in D.items(): print(key,value)