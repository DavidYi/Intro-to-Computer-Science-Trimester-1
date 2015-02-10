#Formating exercise 1 
#David Yi
miles=1
print("%0s%22s" %("Miles","Kilometers"))

while (miles!=11):
    kilom=miles*1.609
    print("%-6d %20.3f" %(miles, kilom))
    miles+=1