counter=1
counter2=0
x=int(input("Tell me any positive integer."))

while (counter<=x):
    
    while (counter2<counter):
        print ("%-d" %(0), end="")
        counter2+=1
    print()
    counter2=0
    counter +=1