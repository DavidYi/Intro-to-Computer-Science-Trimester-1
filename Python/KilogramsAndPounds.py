#Unit 1-Kilograms and Pounds
#David Yi


print("Kilograms\tPounds")
#This variable acts as the counter as well as the kilograms
x=1

while (x<200):
#This variable is the pounds and it converts whatever x kg is to lbs. The following equations puts the decimal up to the tenths place
    y=10*(x*(2.2))
    y//=1
    y/=10
#This makes it so that it only prints odd integers of x
    if (x%2==1):
        print(x,"\t\t",y)
#Acts as the counter so that the while loop can end at one point and it is used as kg
    x+=1