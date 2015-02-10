for i in range(18, -10, -2):

    print ("%3d" % (i), end=" ")
    if (i % 5 == 0):
        print ()
#Rewrite this using while loop
print("\n\nRewriting using while loop.\n")

x= 18

while x>-10:
    print ("%3d" % (x), end=" ")
    if (x % 5 == 0):
        print ()
    x-=2