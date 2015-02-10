import random

options=('rock','paper','scissors')

#goes through the every element in options
for a in options:
    print(a)

#finds a random choice in the list in options
#Like logic where options has a list of numbers
print(random.choice(options))
