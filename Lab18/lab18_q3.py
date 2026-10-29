#find the maximum and minimum values in a dictionary
n=int(input("Enter number of elements: "))
D=dict([])

for k in range(0,n):
    k=input("Enter key: ")
    v=int(input("Enter value: "))
    D[k]=v

minimum=min (D.values())
maximum=max (D.values())
print(f"The maximum is {maximum} and the minimum is {minimum}")



