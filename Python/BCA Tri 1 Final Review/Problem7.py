'''
Write a function order_names that does the following:
1) Asks the user how many names he / she will enter.
2) Reads in the names, one per line, from the user into a list.
3) Sorts the names.
4) Prints the names, one per line, to the output.
Following is a sample run of the program:
How many names will you enter?4
Enter the names, one per line.
Sam
Grace
Matthew
Mansi
Grace
Mansi
Matthew
Sam
'''
def order_names():
    numofnames=int(input("How many names will you enter?\n"))
    my_list=[]
    print("Enter the names, one per line.")
    for names in range(0,numofnames,1):
        name=input()
        my_list.append(name)
    my_list.sort()
    for names in my_list:
        print(names)
order_names()
    