#Unit 1- Company Invoice
#David Yi
print("Welcome to Calculating Total. Please input the following information")

i= input("What item do you want to purchase?")
#item
p= input("\nHow much is it each?")
#price
a= input("\nHow many did you get?")
#amount

i2= input("\nWhat item do you want to purchase?")
p2= input("\nHow much is it each?")
a2= input("\nHow many did you get?")
#This stores the info in the respective variable

t= float(p)*float(a)
t2= float(p2)*float(a2)
g= t+t2
#This calculates the total cost for the respective item and the grand total

print("\n\nItem 1:\n\t", str(a), str(i), ", $" + str(p), "each\n\t", "Total Cost:", t )
print("\nItem 2:\n\t", str(a2), str(i2), ", $" + str(p2), "each", "\n\tTotal Cost:", t2)

print("\n\n\t\tThe grand total is:", g)
#This prints all the information inputed earlier and the total cost as well as the grand total
print("Thank you for using Calculating Total. Please come again")
