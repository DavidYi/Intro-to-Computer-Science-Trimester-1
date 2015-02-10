#Unit 1-Formatting Miles and Kilometers
#David Yi
x=1
y=0
y2=20
x2=0

print("%5s%15s%20s%20s" %("Miles", "Kilometers", "Kilometers", "Miles"))

while (x<20 and y2<66):
    y=x*1.609
    x2=y2/1.609

    print("%-10d%-18.3f%12d%20.2f" %(x,y,y2,x2))
    x+=2
    y2+=5