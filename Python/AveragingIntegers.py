#Unit 1- Averaging Integers
#David Yi

#Sentry variable
average=0
total=0
counter=0
x=1
neg=0
pos=0
#Print instruction
print("Enter a list of int values, the program exits if the input is 0:")
#While loop that stops when the input is 0 as said before
while (x!=0):
#Everytime the while loops the number is inputed and added to the total before it is rewritten and counts how many numbers there are
    x=int(input())
    total+=x
    if x!=0:
        counter+=1
    if x<0:
        pos+=1
    elif x>0:
        neg+=1
#Calculates the average and prints it as well as the number of negaitve, positive numbers, and the the total    
print("The number of positive number is", str(pos) + ".\nThe number of negative number is", str(neg)+".\nThe total is", str(total)+".")
average=total/counter
print("The average is", str(average)+".")