'''
Write a function get_scores that takes no parameters and that returns a dictionary.   
The function asks the user to enter a list of names and scores.
The function will add each name and score to the dictionary as the user enters them.
The name is the "key" for the dictionary and the score is the "value" for the dictionary.  
The score should be stored as an integer.  When the user enters a blank line, the function will exit and return the dictionary.  
Following is the sample run of the program.   
Enter the name/score pairs separated by a space. 
Sam 87 
Grace 78 
Bryan 85 
Olivia 92   
This run would produce the following dictionary: {'Grace': '78', 'Bryan': '85', 'Olivia': '92', 'Sam': '87'} 
'''

def get_scores():
    print("Enter a list of names and scores scores like so, Grace 78 Sam 87...etc.")
    score_input="k"
    scores_dict={}
    while score_input!="":
        score_input=input()
        if score_input=="":
            break
        score_input= score_input.split(" ")
        name=score_input[0]
        score=score_input[1].strip("\n")
        scores_dict[name]=int(score)
    
    return scores_dict

def main():
    my_dict=get_scores()
    print(my_dict)
main()