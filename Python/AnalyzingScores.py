def readinput():
    numbers=input("Enter some numbers: ")
    lists=numbers.split()
    return lists
def findmean(numlist):
    total=0
    counter=0
    for num in numlist:
        total+=int(num)
        counter+=1
    mean= total/counter
    return mean
def findifgreater(numlist, mean):
    x=0
    #This variable will be used to count if the number is greater or equal to the mean
    for num in numlist:
    #This will cause num to go through every element in numlist 
        if (int(num)>=mean):
            x+=1
        #This adds one to y if the num is equal to or greater than the mean
    return x
    #returns the variables
def findiflesser(numlist, mean):
    x=0
    #This variable will be used to count if the number is less than the mean
    for num in numlist:
        if (int(num) < mean):
            x+=1
        #This adds one to x if the num is less than the mean 
    return x   
def main():
    mylist=readinput()
    mymean=findmean(mylist)
    greater= findifgreater(mylist, mymean)
    lesser=findiflesser(mylist, mymean)
    print("The list of numbers are:", mylist)
    print("The mean of these numbers is:", mymean)
    print("The number of values equal to or greater than the mean is:", greater)
    print("The number of values less than the mean is:", lesser)
    #Calls all the functions and prints them out
main()