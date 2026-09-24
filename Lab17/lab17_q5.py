#print the first half of a string
s=str(input("Enter a string: "))
n=len(s)
print(s[:n//2])

#using a for loop
for i in range(n//2):
    print(s[i], end="")