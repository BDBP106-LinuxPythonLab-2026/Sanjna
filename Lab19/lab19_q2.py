a=[i for i in range(1,51)]

#find sum of elements in a
sum=0
for n in a: sum+=n
print(sum)

#define list containing prime numbers

b = [x for x in a if all(x%d!=0 for d in range(2, int(x ** 0.5) + 1))]
print(b)

#collect all common numbers from a and b into new list c

c=[]
for x in a:
    if x in b:
        c.append(x)
print(c)