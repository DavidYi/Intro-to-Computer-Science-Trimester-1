#Unit 1- High Scores
#David Yi

x=0
x2=0
y=0
y2=0
z=0
z2=0
counter=2

dec=int(input("How many scores do you want to enter?"))


x2=input("What was the name?")
x=int(input("What was the score?"))
y2=input("What was the name?")
y=int(input("What was the score?"))
if (counter<dec):
    z2=input("What was the name?")
    z=int(input("What was the score?"))
    counter+=1
while (counter<dec):
    if (x<y and x<z):
        x2=input("What was the name?")
        x=int(input("What was the score?"))
    elif (y<x and y<z):
        y2=input("What was the name?")
        y=int(input("What was the score?"))
    elif (z<x and z<y):
        z2=input("What was the name?")
        z= int(input("What was the score?"))
    counter+=1
#For first place
if (x>y and x>z):
    print("1st place:", x2)
elif (y>x and y>z):
    print("1st place:", y2)    
elif (z>x and z>y):
    print("1st place:", z2)
#for 2nd place    
if ((x>y and x<z)or(x<y and x>z)):
    print("2nd place:", x2)
elif ((y>x and y<z)or(y<x and y>z)):
    print("2nd place:", y2)    
elif ((z>x and z<y)or(z<x and z>y)):
    print("2nd place:", z2)    