import math
radius = 2

print ("%-10s%16s%16s" % ("Radius", "Circumference", "Area"))

while radius <= 17:
    circum = radius * 2 * math.pi
    area = radius ** 2 * math.pi

    print ("%-10d%16.1f%16.2f" % (radius, circum, area))

    radius += 3
#Rewrite using for loops

print("\nRewriting using For Loops.\n")
print ("%-10s%16s%16s" % ("Radius", "Circumference", "Area"))
for radius in range(2, 18, 3):
    circum = radius * 2 * math.pi
    area = radius ** 2 * math.pi

    print ("%-10d%16.1f%16.2f" % (radius, circum, area))