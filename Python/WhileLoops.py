#While demo

import random
roll = random.randint(1,6)
times = 1
#== is equal != is not equal
while roll !=6:
    print("you rolled a", roll)
    roll = random.randint(1,6)
    times +=1
    
print("you rolled a six in", times,"times")

