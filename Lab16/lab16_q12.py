w=str(input("Enter a word: "))
rev=""
for i in range(len(w)-1,-1,-1):
    rev=rev+w[i]
if w==rev: print("It is a palindrome")
else: print("It is not a palindrome")