'''
Write a function count_vowels that takes a string my_str and returns a count of the 
number of vowels in the string.
Following are some example results of the function:
Hello: 2
This is fun: 3
sdghj: 0
'''
VOWELS=["a","e","i","o","u"]
def count_vowels(my_str):
    numofvowels=0
    for letter in my_str:
        if letter in VOWELS:
            numofvowels+=1
    return numofvowels
def main():
    my_str=input("Input in the string.")
    vowels=count_vowels(my_str)
    print(my_str+":",vowels)
main()