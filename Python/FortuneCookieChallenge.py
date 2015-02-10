import random

dec=input("Shall I open your fortune cookie?")
if dec != "no":
    fortune= random.randint(1,5)

    if fortune==1:
        print("The fortune reads: You will do well in academics.")
    elif fortune==2:
        print("The fortune reads: You have great luck for the rest of the day.")
    elif fortune==3:
        print("The fortune reads: You will fail your next big test.")
    elif fortune==4:
        print("The fortune reads: You have terrible luck for the rest of the day.")
    else:
        print("The fortune reads: Nothing good or bad will happen to you for the rest of the day.")

input("Come again next time")