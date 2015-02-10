'''
Write a function mean that takes a parameter my_list, containing numbers. The 
function returns the arithmetic mean of the numbers in the list. 
For example, the list [14, 20, 22, 17] should return 18.25
'''
def mean(my_list):
    numofnum=len(my_list)
    total=0
    for num in my_list:
        total+=num
    mean=total/numofnum
    return mean
def main():
    lists=[14, 20, 22, 17]
    print(mean(lists))

main()