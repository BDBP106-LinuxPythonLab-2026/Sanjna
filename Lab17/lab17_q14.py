#remove all occurences of an element from a list
s=input("Enter numbers: ")
L=s.split( )
e=(input("Enter number to be removed: "))

while L.count(e) > 0:
    L.remove(e)
print("The updated list is: ", L)