# guess the number

n=20
count=0
while True:
    g = int(input("Guess the number between 1 and 50: "))
    count+=1

    if g==n:
        print("Correct!\nAttempts taken to guess:", count)
        break
    elif g>n:
        print("Too High!")
    else:
        print("Too Low!")
    if count==7:
        print("You have run out of guesses! The number is", n)
        break