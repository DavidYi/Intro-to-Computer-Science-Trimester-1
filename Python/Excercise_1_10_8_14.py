
x = 1

while (x <=100):
#end does not put ANY spaces between the x's
    print("%4d" %(x), end="")
    
#this shows that x is divisible by 10
    if (x%10==0):
        print()
        
    x+=1