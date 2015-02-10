#Unit 1- Interest Calculater
#David Yi

print("In order to help you finding the amount of money in a number of years, I ask of \
you to give me your bank info.")
#This prints out what a welcome and what will be required in general

p= float(input("What is your principal?"))
r= float(input("What is your annual interest rate?"))
t= float(input("How far away from today in years are do you want to find out about?"))
n= int(input("How many times will your account compound per year?"))
#This stores what the "customer" inputed in a different variable each
r/=100
#This is to change the percentage into decimal
s=(p+(p*r*t))
c=(p*((1+r/n)**(n*t)))
#This is the calculation of Simple and coumpound interest respectively.
c= (c*100)//1/100
print("The final value with simple interest is $" + str(s))
print("The final value with compund interest is $" + str(c))
#This prints the two interest according to what the user inputed. Changes the float to a string
print("Thank you for trying David Yi's Interest Calculator. \n Come again next time!")
