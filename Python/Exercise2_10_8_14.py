x=1

print ("%-5s%5s%7s" %("x","3x","5x-1"))

while (x<=28):
    if (x%2==0):
        print("%-5d%5d%7d" %(x, 3*x, 5*x-1))
    x+=1