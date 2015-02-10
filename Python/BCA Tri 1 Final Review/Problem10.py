'''
Given the dictionary definition of 
state_birds = {"NJ":"American goldfinch",
 "NY":"Eastern bluebird",
 "CT":"American robin",
 "PA":"Ruffed grouse"}
Write a program that lists the states from the dictionary on one line, separated by 
spaces. (No hard-coding, you must iterate through the list.)
Then prompt the user to select a state.
Finally, print out the state bird for the state entered. If the user enters a state not in the 
list, print "Your choice was not in the list."
Following is a sample run of the program:
Please enter one of the following states.
NY NJ CT PA 
NJ
The state bird of NJ is the American goldfinch
'''

state_birds = {"NJ":"American goldfinch",
 "NY":"Eastern bluebird",
 "CT":"American robin",
 "PA":"Ruffed grouse"}
def get_input(states):
    print("Please enter one of the following states.")
    for state in states:
        print(state, end=" ")
    
    choice= input("\n")
    while choice not in states:
        print("Your choice was not in the list.")
        choice=input("Please enter a valid state")
    return choice

def main():
    my_states=list(state_birds.keys())
    statechoice=get_input(my_states)
    print("The state bird of", statechoice, "is the", state_birds[statechoice])
main()

    
