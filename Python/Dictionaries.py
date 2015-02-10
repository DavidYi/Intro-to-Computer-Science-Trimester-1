test_dict= {}
#Makes empty dictionary
test_dict["yankees"] = 80
test_dict["red soxes"] = 100
test_dict["blue jays"] = 95
"""instead of a list where everything are defined by 0, 1, 2,...,n and u call them like list[0], you define them to whatever like this where
where the "0" can become"""
print("The yankees won", test_dict["yankees"], "games.")
#print("The phillies won", test_dict["phillies"], "games.")
#This alone is going to cause an error because there is no key for it and it prints out KeyError: 'phillies'
games= test_dict.get("phillies", -10)
"""However, you can use this and it says that if there is no key, 'phillies', then -10 will be the value of the key. 
Does not add this to the dictionary"""
print("The phillies won", games, "games.")

key_lists= list(test_dict.keys())
#This converts all the keys to a list ***Not the value of the key the NAME***
key_lists.sort()
for team in key_lists:
    #Finds the lists of the
    print(team+" won", test_dict[team], "games.")