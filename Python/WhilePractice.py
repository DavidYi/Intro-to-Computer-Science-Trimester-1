a = int(input("Please input a number from 0 through 10 inclusive."))

while (a<0 or a>10):
    print("Why did you not listen to me.")
    a= int(input("Please input a number from 0 through 10 inclusive this time."))

b= int(input("Please include a number from" + str(a) + "to 100 exclusive."))

while (b>=100 or b<=a):
    print("Why did you not listen to me.")
    b= int(input("Please input a number from "+ str(a) + "through 100 exclusive this time."))
    
#Sentry variable
total=0
n=1

while (a<=b):
    total+=a
    a+=1
    print("The total after", n, "times is", total)
    n+=1
print("This is the total,", total)