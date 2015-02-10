#This defines the function valid_choice
def valid_choice(question, choices):
    choice= input(question)
#This bugs the user until the user prints a real choice
    while choice not in  choices:
        print("Invalid choice! Please re-enter.")
        choice= input(question)
    return choice
#Defines function, main
def main():
    bglist=("boy","girl")
#This assigns the variable for question and choices respectively
    bg=valid_choice("Are a boy or a girl?", bglist)
    print("You are a "+ bg)
#Reassigns the variable for question and choices respectively, goes back to the definition of the function, valid_choice
    fflist=("McDonalds","Burger Kings")
    ff= valid_choice("You prefer 'McDonalds' or 'Burger Kings'?", fflist)
    print("You prefer"+ff)
#Runs main, which is whatever it is defined.
main()