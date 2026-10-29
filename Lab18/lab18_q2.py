#sum all the values in a dictionary
n=int(input("Enter number of elements: "))
D=dict([])
sum=0
for k in range(0,n):
    k=input("Enter key: ")
    v=int(input("Enter value: "))
    D[k]=v
    sum+=v
print(f"The sum of all values in the dictionary {D} is {sum}")