x=int(input("Input a positive integer."))
counter=0
counter2=1
while (counter<=x):
    while (counter2<=counter):
        print()
        print("%-d" %(counter2)*counter2, end="")
        
        counter2+=1
    counter+=1

counter-=1
counter2-=1
while (counter!=0):
    while (counter2>counter):
        counter2-=1
        print("%-d" %(counter2)*counter2, end="")
    print()
    counter-=1