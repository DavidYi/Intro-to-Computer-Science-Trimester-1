import random

n= random.randint(0,100)

print(n)

#red makes sure that it is a multiple of 2, 5, or 10
red= n%2==0 or n%5==0
#blue makes sure that the number is in 20-30 inclusive
blue= n>=20 and n<=30
#purple is true if both red and blue is true
purple= red and blue

if purple:
    print("The number is either a multiple of 2, 5, or both. The number is also in the range of 20 and 30, so the color will be purple")
elif red:
    print("The number is either a multiple of 2, 5 or both. Red")
elif blue:
    print("The number is in the range of 20 and 30. Blue")