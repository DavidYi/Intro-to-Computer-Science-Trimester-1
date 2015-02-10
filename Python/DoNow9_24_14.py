import random
n=1 #LOOp counter
HEADS=1 #constant
TAILS=2 #constant
h=0 #number of heads
t=0 #number of tails

lastcoin= -1#last coin flipped
lastcoincounter=0#counter of doubles

while n<=1000:
    coin=random.randint(1,2)
    n+=1
    if (coin==HEADS):
        h+=1
    elif (coin==TAILS):
        t+=1
    else:
        print("big problem. Coin=", coin)
    if (lastcoin==coin):
        lastcoincounter+=1
    lastcoin=coin    
        
print("Out of the thousand coin toss, ", h,"was heads and ", t, "was tails.")
print("last coin counter=", lastcoincounter)
input("Press enter to exit.")