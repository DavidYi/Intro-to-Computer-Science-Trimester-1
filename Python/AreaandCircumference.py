import math
radius = 1

print("%10s%16s%16s" %("Radius", "Circumference", "Area"))
while (radius<20):
    circum=2*math.pi*radius
    area= (radius**2)*math.pi
    print("%10d%16.1f%16.2e" %(radius, circum, area))
    radius+=1
    