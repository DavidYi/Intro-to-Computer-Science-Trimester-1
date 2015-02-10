print("I will be guessing a number that you choose between 1 and 100.\n Please think of a number.")

guess= 50
answer2="no"
n=1
increase=50
decrease=50
while answer2!="yes":
    answer2=input("Guess"+str(n)+"--Is the number "+str(guess)+"? yes/no")
    while answer2!="yes" and answer2!="no":
        answer2=input("Invalid input... Is the number"+str(guess)+"? yes/no")
    answer=input("Is the correct number higher or lower?")
    while answer!="higher" and answer!="lower":
        answer=input("Invalid input... Is the correct number higher or lower?")
    if guess!=50:
        increase= guess-increase
        decrease-=guess
    
    if answer=="lower":
        
    elif answer=="higher":
        
    n+=1
    
print("Yes! I guessed the number,", guess, "in", n,"guesses!")

input("Please play again!")