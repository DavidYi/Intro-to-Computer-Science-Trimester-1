#Unit 1 - Electronic Piggy Bank
#David Yi

print("Hello, I will count how much you deposit each time and your total in your piggy bank.")
start =input("How much money is the piggy bank so far?")
#This stores the amount in the piggy bank already in a variable
print("The menu to input your coins is:\n\t(p) - Deposit a penny\n\t(n) - Deposit a nickel\n\t(d) - Deposit a dime\n\t\
(q) - Deposit a quarter\n\t(e) - Exit program and give balance.")
dec=input("What will you deposit?")
#prints the menu and stores what will be deposited first
dep=0
p=0
n=0
q=0
d=0
#This is the sentry variables that I will use
while dec!="e":
    if dec=="p":
        p=+1
    #This only happens if they press p as in penny and it adds 1 (cent) to the variable p 
    elif dec=="n":
        n=+5
    #This only happens if they press n as in nickel and it adds 5 (cents) to the variable n
    elif dec=="d":
        d=+10
    #This only happens if they press d as in dime and it adds 10 (cents) to the variable d
    elif dec=="q":
        q=+25
    #This only happens if they press q as in quarter and it adds 25 (cents) to the variable q
    else:
        print("Invalid option. Try again.")
    #The else is for any letters that was not in the options
    dec=input("What will you input next?")
#This exits the loop when "e" is pressed. Stores the value of each coin in a variable that was assigned to a specific coin    
dep=p+q+n+d
dep/=100
#This is used to find the total amount that was deposited and put in to decimal form
total= float(start) + dep
#This is used to find the total value inside the piggy bank
print("Thank you for using the Electronic Piggy Bank. You have deposited $"+ str(dep), ". ", "You have a total of $"+ \
      str(total))
#the total value in general and deposited is printed.