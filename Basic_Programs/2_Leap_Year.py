'''@Author: Jayesh Patil


@Date: 2024-12-08 


@Last Modified by: Jayesh Patil


@Last Modified time: 2024-12-08 


@Title : Leap Year
'''
"""
Description:

    The `leap_year` function checks whether a given year is a leap year or not. 

Parameters:

    year (int):
        - The year that you want to check.
        - It should be a four-digit number (between 1001 and 9999). 

Returns:

    None:
        - This function doesn't return any values.
        - Instead, it prints whether the given year is a leap year or not.
"""


def leap_year(year):
    """This function is use for finding leap year"""
    if year<=1000 or year>=9999:
        print("Enter in Must be Four Digit Number ")
        return

    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is Leap Year")
    else:
        print(f"{year} is not a Leap Year")

year = int(input("Enter the Year"))
#call the Function 
leap_year(year)

