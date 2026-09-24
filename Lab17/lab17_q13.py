#extract elements of a list, if it occurs more than k times
s=input("Enter numbers: ")
L=s.split( )
k=int(input("Enter number of occurences: "))
for i in set(L):
    if L.count(i)>k:
        print(i, end=" ")
