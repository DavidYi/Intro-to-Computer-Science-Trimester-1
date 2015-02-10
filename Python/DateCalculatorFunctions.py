DAYSOFWEEKS= ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
#This is a tuple
#Tuple is a list that can't be changed, it is static. It has the same functions as a list except append and replace (anything that changes it)
def is_leap_year(year):
#Finds if the year is a leap year or not
#We can make the conditions continue on the bottom to make it cleaner and more organizer
    if ((year%400==0) or 
        ((year%4==0) and (year%100!=0))):
        return True
    else:
        return False

def get_days_in_month (month,year):
    #Finds how many days are in the month
    days=0
    
    if (month in(9,4,6,11)):
        days=30
    #This is for months with 30 days
    elif (month in(1,3,5,7,8,10,12)):
        days=31
    #This is the months with 31 days
    elif (month == 2):
        if (is_leap_year(year)):
        #If the function returns true, then it is 29 days
            days=29
        else:
        #If the function returns false, then it is 28 days
            days=28
    else:
    #This is if they made a mistake
        print("Bad month!", month)
    return days

def gets_days_in_months(start_month, end_month, year):
    #Find the total number of days in the months you are looking for
    total=0
    for m in range(start_month, end_month, 1):
    #goes through each year between start and end month
        total+=get_days_in_month(m,year)
    #Finds the total number of days in the certain month per year and then adds it to the total number of days between the two month
    return total

def get_days_in_years(start_year, end_year):
    #Find the total number of days between the two years
    total=0
    for y in range(start_year, end_year, 1):
    #goes through every number of days between the two years inclusive
        if (is_leap_year(y)):
        #If the function returns true they add the number of days in the leap year to the total
            total+=366
        else:
        #if other than true then it adds the number of days in a regular year to the total
            total+=365
    return total
def get_day_of_week(day, month, year):
    #Finds what day of the week it is
    elapsed =get_days_in_years(1004,year)
    #calls upon the function above and inputs 1004 as the starting year and find how many days are between them and assigns it to the variable
    elapsed += gets_days_in_months(1, month, year)
    #Then find the days in the month between January to whatever month and adds it to the variable
    elapsed+= day-1
    #Adds the day subtracted by one because we have to include 0, but this doesn't include 0, so we subtract it by 1
    dayofweek = elapsed%7
    #Finds the remainder of the variable divided by 7
    return DAYSOFWEEKS[dayofweek]
    #Uses it to find what day it is using a slice

#If you define a variable inside a function, then it only lives inside the function it is defined in
def main():
    print("We will find the day of the date you input please input the following information about the day of the date you want:")
    year=int(input("Year? e.g.2014"))
    month= int(input("Month? e.g. 12"))
    day = int(input("Day? e.g. 31"))
    
    print(get_day_of_week(day, month, year))
main()
