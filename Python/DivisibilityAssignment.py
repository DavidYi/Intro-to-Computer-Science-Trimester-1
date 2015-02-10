#Unit 1- Divisibility
#David Yi
x=100
count=0
while (x<=1000):
    if (x%6==0 and x%5==0):
        print("%5d" %(x), end="")
        count+=1
        if (count%10==0):
            print()
    x+=1