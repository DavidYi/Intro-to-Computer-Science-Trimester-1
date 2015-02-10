"""
Write a program using a for loop to create the following table. Be sure to match the 
number of decimal places and the alignment of the output. (1 inch = 2.54 centimeter). 
Inches Centimeters
     5        12.7
    14        35.6
    23        58.4
    32        81.3
    41       104.1
    50       127.0
    59       149.9
    68       172.7
    77       195.6
    86       218.4
    95       241.3
"""
print("%s%18s" %("Inches","Centimeters"))
for inches in range(5, 96, 7):
    cm= inches*2.54
    print("%6d%18.1f" %(inches,cm))