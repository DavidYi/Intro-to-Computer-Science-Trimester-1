def sum_of_digits(num):
    answer=0
    while (num>0):
#The print statements within the while loop is used to debug my statement
        print("num=", num)
        digit=num%10
        print("digit=", digit)
        num//=10
        print("num=", num)
        answer+=digit
        print("answer=",answer)
    return answer
#This goes back and runs the definition of the sum_of_digits using what the user will input, which is assigned to variable, num. We then convert it to an integer.
sum_of_digits(int(input("Please enter a positive integer and I will add the sums of each digits.")))
