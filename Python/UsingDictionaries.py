def load_file(file_name):
    text_file= open (file_name, "r")
    
    my_dict={}
    for line in text_file:
        #this goes through every line in the text_file
        acronym= line.split(":")
        """plits the line if there is a colon between, so if it was gfgf: hai. then the it would split it into lists. 
        list[0] would be "gfgf" since it was before the : and list [1] would be " hai" because there is a space between the colon and hai
        """
        the_name= acronym[0]
        #This is the key
        the_def = acronym[1].strip()
        #This is the definition of the key and also strips it of the space, since there is nothing in the parameter
        my_dict[the_name]= the_def
        #This makes a dictionary of it
    return my_dict

def get_user_next_choice(key_list):
    print ("Which definition would you like to see? (type \"quit\" to exit)")
    for w in key_list:
        print (w, end=" ")
        #This prints out each keys and gets rid of the white spaces
    return input()
    #This returns the input of what they listed
def main():
    my_dict = load_file("definitions.txt")
    #Calls upon the function
    key_list = list(my_dict.keys())
    #This makes a list of the dictionary's keys
    key_list.sort()
    #This sorts the list
    choice= get_user_next_choice(key_list)
    #This calls upon the function passing the key list as the parameter and the it is defined by the input
    while (choice!="quit"):
        word_def = my_dict.get(choice, "Your selection is not in the dictionary")
        #This finds if the choice is in the dictionary and if it is, it calls upon the definition of the dictionary.
        #If the key is not a choice in the definition, then the word_def is equal to your selection is not in the dictionary
        print(word_def + "\n\n")
        #Thens prints whatever value it is
        choice= get_user_next_choice(key_list)
        #finds what the next choice is
main()