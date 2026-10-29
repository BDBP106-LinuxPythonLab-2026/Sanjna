# number classifier

n=int(input("Enter a number: "))
if n>0:
    if n%2: print("Positive, Odd!")
    else: print("Positive, Even!")
elif n<0:
    if n%2: print("Negative, Odd!")
    else: print("Negative, Even!")
else: print("Zero!")

if n%3==0 and n%5==0: print("FizzBuzz number!")