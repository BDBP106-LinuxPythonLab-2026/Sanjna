n=int(input("Enter a number: "))
rev=0
temp=n
while n>0:
    rev=(rev*10+(n%10))
    n=n//10
if temp==rev:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")