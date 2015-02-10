print("%-10s%7s" %("Dollars","Euros"))

for n in range(25,500,75):
#(what n =s (start) , n<whatever(exit), increments by whatever)
#defines n
    e=n/1.28
    print("%-10s%7.2f"%(n, e))