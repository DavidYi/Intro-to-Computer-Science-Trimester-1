'''
Write a program that does the following:
1) Asks the user to enter a list of floating point numbers on one line.
2) Reads the numbers, all from the same line, and sums them.
3) Prints the sum of the numbers.
Following is a sample run of the program:
Please enter a list of numbers on one line.
12.1 14.5 7
The sum is 33.6
'''
def findfloats():
    floatinput=input("Please enter a list of numbers on one line (can be floats).\n")
    floatlist=floatinput.split()
    n=0
    for num in floatlist:
        floatlist[n]= float(num)
        n+=1
    return floatlist
def findsum(floatlist):
    total=0
    for floats in floatlist:
        total+=floats
    print(total)
def main():
    lists=findfloats()
    findsum(lists)
main()