#Unit 1 - Rock, Paper, Scissors
#David Yi

#This lets me use commands from the random library
import random
#sentry variables 
dec="y"
win=0
lose=0
tie=0

#Tells what this program is about
print("We will be playing Rock, Paper, Scissors.The game will end when someone reaches 5 wins. Best of luck!")

#Since dec already equals y and win doesn't equal 0, the while loop is first started
while (dec=="y" and (win!=5 or lose!=5)):
#This is what the computer will use and it generates a number from 1 to 3
    comp= random.randint(1,3)
#From the number, I created a way to change the number 1, 2, and 3 for r, p, and s respectively
    if comp==1:
        comp= "r"
    elif comp==2:
        comp= "p"
    elif comp==3:
        comp= "s" 

#This lets the player choose which chose he wants
    turn=input("What do you want to choose? r for rock, p for paper ,or s for scissors.")

#This statement is to ensure that the player chooses a valid choice. If he does then it continues on with the program
    if (turn=="r" or turn=="p" or turn=="s"):
        pass
    
    else:
        while (turn!="r" and turn!="p" and turn!="s"):
            turn=input("I'm sorry but that is not a valid choice. Please choose r for rock, p for paper, or s.")

#This situation is when the computer wins. This adds 1 to loss and prints out that you lost and how many win/loss/tie you have
    if ((comp=="r" and turn=="s")or(comp=="s"and turn=="p")or(comp=="p"and turn=="r")):
        lose+=1
        print("You lost. You chose", turn,". The computer chose", comp,".\n\n The score is now:\nWin:",win,"\nLoss:",lose, "\nTie:", tie)

#This situation is when the computer loses. This adds 1 to win and prints out that you won and how many win/loss/tie you have
    elif ((comp=="r" and turn=="p")or(comp=="p" and turn=="s")or(comp=="s" and turn=="r")):    
        win+=1
        print("You won. You chose", turn,". The computer chose", comp,".\n\n The score is now:\nWin:",win,"\nLoss:",lose,"\nTie:", tie )

#This situation is for all cases that the comp and turn is the same. This adds 1 to tie and prints out that you tied and how many win/loss/tie you have
    else:
        tie+=1
        print("You tied. You chose", turn,". The computer chose", comp,".\n\n The score is now:\nWin:",win,"\nLoss:",lose,"\nTie:", tie )

#This is for those who got five wins and tells how many times they lost and tied and won. It says great job and exits the while loop.
    if win==5:
        print("Well done!!!! You got", win,"wins with ", lose,"loss and", tie,"ties! Let's play again next time!")
        break
#This is when you lost 5 times
    if lose==5:
        print("Nice try. I am a black belt master when it comes to Rock Paper Scissors.")
#This asks if it wants to play again and if it is no then it prints out the score that they currently have when they decided to leave and leaves the while loop
    dec=input("Shall we play again? y/n")
    while (dec!="n"and dec!="y"):
        print("That is an invalid key.")
        dec=input("Shall we play again? y/n") 
    if dec=="n":
        print("Wow. I wanted to play more with you, but you had", win, "wins", lose,"loss, and", tie,"ties")
    
print("Thanks for playing. Let's play again next time!")
