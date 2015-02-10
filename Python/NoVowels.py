VOWELS="aeiou"
#ususally puts the variable in caps in order to tell others that it is a constant meaning not changing
n= input("Enter a string.")
output=""
for c in n:
#It is basicly saying go through every element in c, in this case, letters
    if (c.lower() not in VOWELS):
#In means like in logic, where if an element of c is not an element of VOWELS
        output+=c
#What this does is that if it is not a vowel, then adds it to the variable output. E.G. ("r"+"w"+"f"+"r")
        
print(output)