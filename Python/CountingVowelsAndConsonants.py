VOWELS="aeiou"
CONSONANTS="qwrtypsdfghjklzxcvbnm"
def count_consonants (my_str):
    return counter(my_str,CONSONANTS)

def count_vowels (my_str):
    return counter(my_str, VOWELS)

def counter(my_str,my_str2):
    counter=0
    for c in my_str:
        if (c.lower() in my_str2):
            counter+=1
    return counter
    
def main ():
    x=str(input("Enter a string please."))
    a=count_consonants(x)
    b=count_vowels(x)
    print("There are ", a,"consonants and", b,"vowels")
    return x

main()
