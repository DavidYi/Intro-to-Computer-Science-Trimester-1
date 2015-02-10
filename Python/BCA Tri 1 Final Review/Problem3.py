'''
Write a function called largest that takes 3 parameters a, b, c which are all numbers. 
The function returns the largest value of the 3 parameters. For example, calling
largest (19, 17, 19) would return 19 and the calling largest (513, 600, 54) would return 
600.
'''

def main():
    a=input("Input a number")
    b=input("Input a number")
    c=input("Input a number")
    largestnum=largest(a,b,c)
    
    print(largestnum)
def largest(a,b,c):
    if (a>b and a>c):
        return a
    if (b>a and b>c):
        return b
    if (c>a and b>a):
        return c
main()