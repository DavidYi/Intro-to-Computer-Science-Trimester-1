sentence = input("Enter a sentence: ")
#Split makes the string spit into more strings of each word (defined by a white space)
mylist= sentence.split()

mylist.reverse()
#This prints each string in the list without any spaces
for w in mylist:
    print(w, end= "")

#Using numbers. This is how you change to integers
nums= input("Please enter a list of numbers.")
numslist= nums.split()
#The list is still characters and the for loop changes it to an integer. The increment is 1 when it does not have an increment stated
for i in range(0,len(numslist)):
    numslist[i] = int(numslist[i])
numslist.sort()

print(numslist)