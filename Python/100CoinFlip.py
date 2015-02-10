import random

times=1
heads=0
tails=0

while times<=100:
    flip= random.randint(1,2)
    
    if flip == 1:
        heads+=1
    
    else:
        tails+=1
    
    times+=1

print("In the 100 coin flips, ", heads, "was heads and ", tails,"was tails.")

input("Press enter to exit.")