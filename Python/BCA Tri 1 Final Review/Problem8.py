'''
Write a program to create the following table. Be sure to match the number of decimal 
places and the alignment of the output. (1 km = 0.62 miles). 
Miles     Km          Km     Miles
    5    8.1           3      1.86
   15   24.2           7      4.34
   25   40.3          11      6.82
   35   56.5          15      9.30
   45   72.6          19     11.78
   55   88.7          23     14.26
   65  104.8          27     16.74
   75  121.0          31     19.22
   85  137.1          35     21.70
   95  153.2          39     24.18
'''
print("%5s%7s%12s%10s" %("Miles","Km","Km","Miles"))
km2=3
for miles in range(5,96,10):
    km=miles/0.62 
    miles2=km2*0.62
    print("%5d%7.1f%12d%10.2f" %(miles,km,km2,miles2))
    km2+=4