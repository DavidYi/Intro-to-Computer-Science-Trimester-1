'''
Write a function position_of_largest that takes a parameter my_list, containing a list 
of numbers. The function returns the position of the largest number in the list. If the 
largest number appears multiple times in the list, the position of the first occurrence is 
returned.
Example 1: For the list [12,5,19,1,4,7], the function would return 2. 
Example 2: For the list [25, 4, 5, 25,3], the function returns 0.
'''

def position_of_largest(my_list):
    position=0
    n=0
    for num in my_list:
        if num> my_list[position]:
            position=n
        n+=1
    return position
def main():
    my_list=[25, 4, 5, 25,3]
    print(position_of_largest(my_list))
main()