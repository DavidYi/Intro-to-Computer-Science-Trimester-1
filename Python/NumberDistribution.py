def readfile(my_file):
    #Reads and counts the number of time the integer occurs in the text file
    textfile=open(my_file, "r")
    my_dict={}
    my_list=[]
    #Creates empty dictionary and list
    for line in textfile:
        integer= line.split()
        my_list+=integer
    #Gets rid of all the spaces
    for line in my_list:
        currentnumber = my_dict.get(line, 0)
        currentnumber+=1
        my_dict[line]=currentnumber
    #Finds the number of time they occur and sets the number to the number of times they occur
    return my_dict
def main():
    my_dict= readfile("num_dist_1.txt")
    #Calls the function and uses the txt file as the parameters and passes it through as my_file
    my_keylist=list(my_dict.keys())
    #Makes a list of all the keys of the dictionary, the value of the keys are not saved in any way in the list
    my_keylist.sort()
    #Sorts the list
    for num in my_keylist:
        #Goes through ever key or element in the list
        if my_dict[num]==1:
            #If there is only one of the number, then it puts time in past tense
            print("%s: %d time" %(num, my_dict[num]))
            #Prints the number out along with however many it has
        elif my_dict[num]>1:
            #If the number is greater than one then prints the same thing as before but changing it to plural
            print("%s: %d times" %(num, my_dict[num]))
        else:
            print("Invalid Choice. There are no negative amount of one thing")
            #This is for negative number of times
main()