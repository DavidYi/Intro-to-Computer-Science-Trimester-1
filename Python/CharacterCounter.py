
def readfile(file_name):
    text_file= open(file_name, "r")
    
    my_dict={}
    for line in text_file:
        for char in line:
            #goes through every character in the line
            char=char.lower()
            if (char.isalpha()):
                #This finds if the character is really a character
                currentchar = my_dict.get(char, 0)
                '''This finds how value of the letter found in the dictionary. If the letter does not exist in the dictionary, they make a new key and the value becomes 
                zero. If there is the character then, they the current character is equal to however many there was'''
                currentchar += 1
                #This adds one to the how many character there are. Since the value would be the past number or 0
                my_dict[char]=currentchar
                #This then adds the new number of character to the key defined my the character it corresponds to.
    return my_dict
def main():
    my_dict= readfile("story.txt")
    
    char_list=list(my_dict.keys())
    #This makes a list of the keys, not the value of it
    #In order to go and use the value of the key, you have to use the dictionary, not the list
    char_list.sort()
    for c in char_list:
        print("%s: occurs %d times" %(c, my_dict[c]))
main()