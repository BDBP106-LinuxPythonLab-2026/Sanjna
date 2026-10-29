#remove duplicates from a sentence using a dictionary
s=input("Enter a sentence: ")
D=dict([])
a=s.split()


i=1
for word in s.split( ):
    D[word]=i
    i+=1
uniq_s=(D.keys())
print("The sentence without duplicates is: ", " ".join(uniq_s))