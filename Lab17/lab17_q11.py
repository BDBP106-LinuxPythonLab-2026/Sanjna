#print duplicate elements in a list L

s=input("Enter numbers: ")
L=s.split( )
duplicates=[]
print("The duplicate elements are:")
for i in L:
    if L.count(i)>1 and i not in duplicates:
        print(i, end=" ")
        duplicates.append(i)