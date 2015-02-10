import math

#To change to the option of directly inputing the numbers, go to the function main and delete the '#' symbol in the my_list definition where
#it calls the function read_numbers and add the symbol to the other my_list definition

def read_numbers_from_file1(file_name):
    text_file= open(file_name, "r")
#The r tells it to read it. this opens the file_name and assigns the open file to text_file
    numofnumbers = int(text_file.readline())
#Reads the line and in this case the number will show how many because of what goes first in the function, readnumbers
    num_list=[]
    for i in range(0, numofnumbers):
        nextnum=int(text_file.readline())
        #The next read line starts the move down to the next line that has a character
        num_list.append(nextnum)
    num_list.sort()
    #Sorts the number lower to highest
    return num_list

def read_numbers_from_file2(file_name):
    text_file= open(file_name, "r")
#The r tells it to read it. this opens the file_name and assigns the open file to text_file
    numofnumbers = int(text_file.readline())
#Reads the line and in this case the number will show how many because of what goes first in the function, readnumbers
    num_list=[]
    for i in range(0, numofnumbers):
        nextnum=int(text_file.readline())
        #The next read line starts the move down to the next line that has a character
        num_list.append(nextnum)
    num_list.sort()
    #Sorts the number lower to highest
    return num_list

def read_numbers ():
    x=1
    n=int(input("How many numbers will you put in?"))
    lists=[]
    while x<=n:
        y=input()
        lists.append(y)
        x+=1
    lists.sort()
    return lists

def get_mean (num_list):
    """ Returns the statistical mean of the numbers in the list """
    x=0
    #This variable is to find the total value of all the element in the list 
    count=0
    #This variable is to find out how many numbers are in the list
    for c in num_list:
        x+=int(c)
        #Changes c into an int and adds it every time
        count+=1
        #This allows us to find how many elements are in the list
    mean= x/count
    #This finds the mean
    return mean

def get_range (num_list):
    """ Returns the statistical range of the numbers in the list """
    y=int(min(num_list))
    x=int(max(num_list))
    #Gets the min and max and converts to integers
    myrange = x-y
    #Gets the range of it
    return myrange

def get_median(num_list):
    x= len(num_list)
    #Finds the number of element in the list
    if x%2==0:
    #If the number of element in the list is even...
        mednum1= int(num_list[x//2])
        mednum2= int(num_list[x//2-1])
    #Find the 2 median, which is found by doing integer division 2 and again minus 1 for the two median
        median= (mednum1+mednum2)/2
    #Then you find the average of two median and the result is the real median
    else:
    #If the number of element in the list is odd...
        median=num_list[x//2]
    #Just find the middle number, which is found using integer division
    return median

def get_std_dev(num_list):
    mean=get_mean(num_list)
    #Calls the function get_mean and assigns the result to mean
    x=[]
    #Empty list
    for c in num_list:
        y=(mean-int(c))**2
    #This finds the value of the mean subtracted by each element in the list and squares it. Always positive 
        x.append(y)
    #This adds the value to the list x
    mean2 = get_mean(x)
    #With the list of y, we find the mean of it
    stddev=math.sqrt(mean2)
    #Then we find the square root of it
    return stddev

def get_mode(num_list):
    mode=[]
    #Empty list
    mode_count=0
    #This counts the number of times the mode is occurs in the list
    for c in num_list:
        if c not in mode:
        #Uses this, so there is no more repeat of the same value of c
            ccount=num_list.count(c)
        #Finds the number the element c is found in the list
            if (ccount==mode_count):
        #If the number the element c is found in list is equal to the how much times the current mode occurs in the list
                mode.append(c)
        #Then it adds the element to the list because they both have the same amount of times that it occurs
            elif (ccount > mode_count):
        #This option is when the number of times the element c occurs is greater than the current mode 
                mode=[]
        #Redefines mode into empty list meaning there is no element inside it
                mode.append(c)
        #Adds the element c because that is the current mode
                mode_count=ccount
        #This makes what the number of times the current mode occurs in the list 
    return mode

def main ():
    my_list = read_numbers()
    #my_list= read_numbers_from_file1("test_num_1.txt")
    #my_list = read_numbers_from_file2("test_num_2.txt")
#To switch the text file erase the '#' symbol above and add it to the other my_list definition 
#this is to test the program
    print("List:", my_list)
    print("Minimum:", min(my_list))
    print("Maximum:", max(my_list)) 
    print("Range:", get_range(my_list))
    print("Median:", get_median(my_list))
    print("Mean:", get_mean(my_list))
    print("Standard Deviation:", get_std_dev(my_list))
    print("Mode:", get_mode(my_list))
#Goes through all the function and prints the result
main()