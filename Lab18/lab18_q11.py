#magic date
months=dict([("January", 1), ("February", 2),   ("March", 3),   ("April", 4),   ("May", 5),   ("June", 6),   ("July", 7),   ("August", 8),   ("September", 9),   ("October", 10),   ("November", 11),   ("December", 12)])
#for n,m in months(): if

def mdate(d,m,y):
    n=int(months[m])
    if int(y[2:4])==d*n: print(f"Magic Date is {d},{m},{y}")
    else: print("Not a Magic Date")

"""
d=int(input("Enter date: "))
m=input("Enter month: ")
y=input("Enter year: ")
mdate(d,m,y)"""

for y in range(1900,2000):
    for n in range(1,13):
        for d in range(1,32):
            mdate(d,n,str(y))
