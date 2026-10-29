# multiplication table grid

n=int(input("Enter a number: "))

width = len(str(n*n)) + 1

print(" " * len(str(n)), end="")
for j in range(1, n+1):
    print(str(j).rjust(width), end="")
print()

for i in range(1, n+1):
    print(str(i).rjust(len(str(n))), end="")
    for j in range(1, n+1):
        print(str(i * j).rjust(width), end="")
    print()