def get_numbers():
    numbers = input("Enter the numbers: ")
    numberlist= numbers.split()
    for c in range(0,len(numberlist)):
        numberlist[c] = int(numberlist[c])
    numberlist.sort()
    return numberlist
def get_distnumber(numbers):
    distinct= []
    for c in numbers:
        if c not in distinct:
            distinct.append(c)
    distinct.sort()
    return distinct
def main():
    x= get_numbers()
    distinct= get_distnumber(x)
    print("The distinct numbers are: ", distinct)
main()