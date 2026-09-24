#extract words beginning with k from a list L
string=input("Enter a string: ")
L=string.split( )
print(L)
for word in L:
    if word.startswith("k"): print(word)