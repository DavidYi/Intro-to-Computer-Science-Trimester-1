x = int(input("What number would you like to count from?"))
y= int(input("What number would you like to count to?"))
z= int(input("What number would you like your increment by?"))
counter=1

for i in range(x,y,z):
    print("%4d"%(i), end="")
    if (counter%5==0):
        print()
    counter+=1