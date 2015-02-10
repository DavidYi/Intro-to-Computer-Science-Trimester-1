#Formating exercise 2
#David Yi
p=900
y=1
r=.0875
pastinter=0
print("%-10s%10s%15s" %("Year", "Interest", "Balance"))

while y!=31:
    total= p*((1+r)**y)
    inter= total-p
    inter= inter- pastinter
    print("%-10d%10.2f%15.2f" %(y, inter, total))
    y+=1
    pastinter+=inter
