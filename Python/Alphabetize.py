text_file= open("words.txt", "r")
#If in current working directory just put in the file like above 
mylist=[]
print(text_file)
for line in text_file:
    print("line:", line)
    words= line.split()
    print("words: ",words)
    mylist+=words
    print("mylist:", mylist)
#This adds the string words to the end of words
#The for loop 
mylist.sort()
#Uppercase letters are first. Lowercase letters are next. They sort by askee number assigned to the
print(mylist)