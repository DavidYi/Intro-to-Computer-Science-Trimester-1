import random

# Dictionary of the valid quizzes available to the user.
# The key is the label and the value is the data file name.
data_files = {"East": "states_east.txt",
              "West": "states_west.txt",
              "South": "states_south.txt",
              "Central": "states_central.txt",
              "All": "states_all.txt"
              }    

def read_states_into_dict (file_name):
    """
    Loads the specified text file.  
    There is one State / Capital combination per line.
    The state and capital are separated by a tab character.

    Hint: It is advisable to call strip() on the capital string prior to adding 
    it to the dictionary to remove the new line character.
    """
    text_file= open (file_name, "r")
    #Opens file and sets it to read
    my_dict={}
    #Empty dictionary
    
    for line in text_file:
        #goes through each line in the file
        info= line.split("\t")
        #Splits the state and its capital if there is a tab between them into lists
        state = info[0]
        #Since state is the first one in the line it is going to be the first element in the list, info
        capital = info[1].strip("\n")
        #Since the capital is the second one one the line, it is going to be the second element in the list
        #you can strip and split new lines and tabs by typing in the shortcuts like \t or \n.
        my_dict[state] = capital
        #This adds state and its corresponding capital to the dictionary
        
    return my_dict

def quiz (my_dict):
    """ 
    This method implements a loop that will continue to quiz the user until the user types
    "quit" or correctly identifies all of the capitals in the list.

    Each time the user identifies a capital, it is removed from the list.

    At the end, the function will report how many guesses were required by the user.
    """
    print("\nLet's begin the quiz. Once you get a state correct, I will remove it from the list.",\
    "Let's play until you get them all correct. \nOr, if you grow tired, enter quit to exit at any time. Good luck!")
    my_list= list(my_dict.keys())
    #Changes the keys into lists
    answer=" "
    #This is the answer that the player will give and will also allow it to go in the while loop
    correct=[]
    #Creates empty list that will hold all the states that the player answered correctly
    guesses=0
    #The number of guesses so far
    finished=len(my_list)
    #This is the number of states/capitals in the file the player chose
    hopefully=len(correct)
    #This is going to be zero, it is only here to allow us to go in the while loop
    
    while ((answer!="quit") and (hopefully!=finished)):
        #only if the answer is not equal to the string 'quit' and the variable hopefully is not equal to finished
        state= random.randrange(finished)
        #This finds a random number that corresponds to my_list and assigns it to state, since the list is full of states
        question=my_list[state]
        #This finds the name of the state according to the number that was assigned to the variable, state,
        correctanswer=my_dict[question]
        #This finds the correct answer, which is the capital
        
        if state not in correct:
            #Only if the number corresponding to the state is not in the list, correct
            answer= input("What is the capital of " + question + "?")
            #This assigns what the player inputs and assigns it to answer.
            # The input will be what the player thinks is the capital to the state that is not in the list, correct 
            if (answer == correctanswer):
                #Only if the answer is the correct answer
                print("Correct!")
                correct.append(state)
                #Adds the state to the list, correct, because the player got it right and according to the rules, it will no longer show up
                hopefully=len(correct)
                #This finds how many elements there are in correct. Also, this is the ticket out of the while loop.
            
            elif ((answer!=correctanswer) and (answer!="quit")):
                #Only If the answer is incorrect and the player doesn't ask to quit
                print("Incorrect! The capital is", correctanswer)
                #Prints the correct answer
            
            if (answer!="quit"):
                #Only if the player doesn't ask to quit
                guesses+=1
                #Adds one to the number of guesses
    
    if (answer!="quit"):
        #Only if the player didn't ask to quit
        print("Wow! You got all", finished, "correct in", guesses, "guesses!")
        #Prints how many states/capitals were in the file the player wanted and the number of guesses it took to get every capital correct.
    print("Play again next time!!!")
    
def get_datafile_choice():
    """ 
    Asks the user to select a data file to use for the quiz.  The function makes sure the 
    user makes a valid selection.  
    The function returns the filename selected by the user.
    """
    state_list= list(data_files.keys())
    #Makes a list out of the keys of the data_files, in this case, a certain group of states
    text_file="no"
    #This is to allow the while loop to start
    #This is to make it easier. Basically says that the input that the player inputed is not valid
    while (text_file=="no"):
        #Only if the text_file doesn't equal 'no'
        print("Which data file would you like to load?")
        
        for f in state_list:
            #Goes through every group in the list
            print(f, end=" ")
            #Prints out all the group, or options
        choice=input()
        #The next input is the choice that the player chose
        text_file = data_files.get(choice.capitalize(), "no")
        #If the choice is a key in the dictionary defined before, then it lists the value of the key, or the file that is to be used
        #If the choice is not a key, then it equals no, which will repeat until a valid choice is inputed
        
        if (text_file == "no"):
            #Only if the the choice is not a valid choice
            print(choice, "does not exist.")
            #Then notifies that the choice the player inputed does not exist and not valid
    
    return text_file

def main ():
    
    file_name = get_datafile_choice()
    #Calls upon the function get_datafile_choice and finds what the file that will be used is
    my_dict = read_states_into_dict (file_name)
    #Uses the file that will be used and makes a dictionary of the file that will be used in the quiz
    quiz (my_dict)
    #Just goes to the function and runs it

main()