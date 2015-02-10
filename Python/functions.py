#These just define, not run. It stores this in the memory
def f(x):
    return 2*x-3
def g(x):
    return x**2 -1
def h(x,y):
    return x*y +1
#This is stored and when we call for the main(), then this is runned. 
def main():
#This goes back to the definition of f(x) and plugs in 4 for x and prints the answer
    print (f(4))
#This goes back to the definition of g(x) and plugs in 12 for x. Saves the answer in the variable
    output= g(12)
#Prints the variable output 
    print(output)
#This one goes first and uses the main we defined above
main()
