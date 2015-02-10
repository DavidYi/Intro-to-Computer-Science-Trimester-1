n=25
print("%-10s%7s" %("Dollars","Euros"))
while n<500:
    e=n/1.28
    
    print("%-10s%7.2f"%(n, e))
    n+=75