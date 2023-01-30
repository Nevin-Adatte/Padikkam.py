import random
print("Rules 📜")
print("Guess the correct number in between 1-99")
print("5 chances are given")
print("Hints are provided")
print(" ")
print("--Lets Begin the Game--")
print(" ")
while True:
    guess = random.randint(1,99)
    for i in range(5):
        print("Chance: "+ str(i+1))
        n = int(input("Enter your guess: "))
        if(guess == n):
            print("Correct answer " + str(n)  + " ✔️")
            break
        else:
            print("Wrong answer " + str(n) + " ❌")
            if(guess < n):
                print("Answer is less than the guess value")
            else:
                print("Answer is greater than the guess value")
            print("")
    print("Game Over")
    if(guess != n):
        print("Better lick next time")
    else:
        print("Excellent playing")
    print("")
    cond = input("Do you want to play again(y/n)")
    if(cond == "n"):
        break