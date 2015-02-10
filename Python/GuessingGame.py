import random
import sys

small = int(input("What do you want as the minimum possible number?"))
big = int(input("What do you want as the maximum possible number?"))

print("You have 10 guesses to guess a number according to your range you have inputed.")

if small==big:
    print("YOU CHEATED!!!!")
    sys.exit()
else:   
    answer= random.randint(small,big)
    guess= int(input("What is your guess?\n\n"))
    n = 1
#tracks total guesses

    
    while guess!=answer and n<=9:
        if guess<answer:
            print("Too low.")
        else:
            print("Too high.")
        guess=int(input("Try again."))
        n+=1
    if guess==answer:   
        print("Well done!!! You guessed", answer,"in", n,"guesses", sep=" ")
    else:
        print("I'm sorry, you have not been able to guess the number within 10 guesses.")