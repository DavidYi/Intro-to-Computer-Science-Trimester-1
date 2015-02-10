def max(a,b):
    if (a>b):
        return a
    else:
        return b
def longer(a,b):
    if (len(a)>len(b)):
        return a
    elif (len(b)>len(a)):
        return b
    else:
        c= print("They are both of equal length")
        return c
def main():
    print (max(12,3))
    print(max(-3,-2))
    
    print(longer("what", "WOw"))
main()