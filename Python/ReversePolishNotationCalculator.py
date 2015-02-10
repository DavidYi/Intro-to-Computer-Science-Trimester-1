#Unit 1- Reverse Polish Notation Calculator
#David Yi

#Sentry Variables/ variables I will use
#Operands
x=0
y=0
#Operators
z=""

#This prints out something and finds what x and y equals
print("Input:")
x=float(input())
y=float(input())

#This makes a loop
while (y!='='):
#This finds what the operator the user would like to use and stores it
    z=input()
#This is to use the operator and operand and find the current total and make sure the key wasn't invalid
    if (z=='+'):
        x+=float(y)
    elif (z=='-'):
        x-=float(y)
    elif (z=='/'):
        x/=float(y)
    elif (z=='*'):
        x*=float(y)
    else:
        raise SyntaxError("Read token%s, expected operator" %z)
#This finds what the next number will be or if they want to find the total because it loops again
    y=input()

#This prints out output and the total with it rounded to the nearest hundreths 
print("Output:")
print("%.2f" %(x))