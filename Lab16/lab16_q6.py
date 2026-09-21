n=int(input("Enter a number:"))
s=0
while n>0:
    d=n%10
    s+=d
    n//=10

print ("The sum of the digits of the number "+str(n)+" is "+str(s)+"")
